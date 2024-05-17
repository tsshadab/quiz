import sqlite3
import json
from models.quiz_model import Question
from typing import Dict

DATABASE = 'utils/quiz.db'

def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db

def init_db():
    with sqlite3.connect(DATABASE) as db:
        c = db.cursor()
        # Create the questions table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                question TEXT NOT NULL,
                answerKey TEXT NOT NULL
            )
        ''')

        # Create the options table if it doesn't exist
        c.execute('''
            CREATE TABLE IF NOT EXISTS options (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question_id INTEGER,
                option_key TEXT NOT NULL,
                option_text TEXT NOT NULL,
                FOREIGN KEY(question_id) REFERENCES questions(id)
            )
        ''')

        # Clear existing data
        c.execute('DELETE FROM options')
        c.execute('DELETE FROM questions')

        # Load initial data from JSON file
        with open('utils/quiz_data.json') as f:
            quiz_data = json.load(f)
            for item in quiz_data:
                c.execute('''
                    INSERT INTO questions (id, question, answerKey)
                    VALUES (?, ?, ?)
                ''', (item['id'], item['question'], item['answerKey']))

                question_id = c.lastrowid
                for option in item['options']:
                    c.execute('''
                        INSERT INTO options (question_id, option_key, option_text)
                        VALUES (?, ?, ?)
                    ''', (item['id'], option['option_key'], option['option_text']))
        
        db.commit()

def get_quiz_data():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('''
        SELECT q.id, q.question, q.answerKey, o.option_key, o.option_text
        FROM questions q
        JOIN options o ON q.id = o.question_id
    ''')
    rows = cursor.fetchall()

    questions = {}
    for row in rows:
        question_id = row['id']
        if question_id not in questions:
            questions[question_id] = {
                'id': row['id'],
                'question': row['question'],
                'options': []
            }
        questions[question_id]['options'].append({
            'option_key': row['option_key'],
            'option_text': row['option_text']
        })

    return list(questions.values())

def evaluate_quiz(answers: Dict[int, str]):
    score = 0
    results = []
    
    # Fetch all questions
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT id, answerKey FROM questions")
        questions = c.fetchall()
        
    for question_id, correct_option in questions:
        user_answer = answers.get(question_id)
        if user_answer == correct_option:
            score += 1
            results.append({"question_id": question_id, "correct": True})
        else:
            results.append({"question_id": question_id, "correct": False})
    
    return score, results
