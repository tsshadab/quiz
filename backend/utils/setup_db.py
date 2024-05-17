import sqlite3
import json
import os

# Ensure the directory structure exists
if not os.path.exists('utils'):
    os.makedirs('utils')

# Connect to SQLite database (or create it)
conn = sqlite3.connect('utils/quiz.db')
c = conn.cursor()

# Create table for quiz questions
c.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY,
    question TEXT NOT NULL,
    answerKey TEXT NOT NULL
)
''')

# Create table for options
c.execute('''
CREATE TABLE IF NOT EXISTS options (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_id INTEGER NOT NULL,
    option_key TEXT NOT NULL,
    option_text TEXT NOT NULL,
    FOREIGN KEY (question_id) REFERENCES questions(id)
)
''')

# Insert data from JSON file into tables
with open('utils/quiz_data.json') as f:
    data = json.load(f)
    for item in data:
        c.execute('''
        INSERT INTO questions (id, question, answerKey) VALUES (?, ?, ?)
        ''', (item['id'], item['question'], item['answerKey']))
        for option in item['options']:
            c.execute('''
            INSERT INTO options (question_id, option_key, option_text) VALUES (?, ?, ?)
            ''', (item['id'], option['option_key'], option['text']))

# Commit changes and close connection
conn.commit()
conn.close()
