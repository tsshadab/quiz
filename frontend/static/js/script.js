document.addEventListener('DOMContentLoaded', async () => {
    const quizContainer = document.getElementById('quiz');
    const resultContainer = document.getElementById('result');
    let quizData;

    async function loadQuiz() {
        try {
            const backendURL = 'http://localhost:8000'; // Use the provided backend URL or default to localhost
            const response = await fetch(`${backendURL}/quiz/api/questions`);
            quizData = await response.json();
            displayQuiz();
        } catch (error) {
            console.error('Error fetching quiz data:', error);
        }
    }

    function displayQuiz() {
        quizContainer.innerHTML = ''; // Clear previous quiz content
        quizData.forEach((question, index) => {
            const questionElement = document.createElement('div');
            questionElement.classList.add('question');

            const questionTitle = document.createElement('h3');
            questionTitle.textContent = `${index + 1}. ${question.question}`;
            questionElement.appendChild(questionTitle);

            question.options.forEach(option => {
                const optionLabel = document.createElement('label');
                optionLabel.innerHTML = `
                    <input type="radio" name="question${index}" value="${option.option_key}">
                    ${option.option_text}
                `;
                questionElement.appendChild(optionLabel);
            });

            quizContainer.appendChild(questionElement);
        });
    }

    window.submitQuiz = async function() {
        const answers = quizData.map((question, index) => {
            const selectedOption = document.querySelector(`input[name="question${index}"]:checked`);
            return selectedOption ? {
                question_id: question.id,
                selected_option: selectedOption.value
            } : null;
        });

        const unansweredQuestions = answers.filter(answer => answer === null);
        if (unansweredQuestions.length > 0) {
            alert('Please answer all questions before submitting the quiz.');
            return;
        }

        try {
            const backendURL = process.env.BACKEND_URL || 'http://localhost:8000'; // Use the provided backend URL or default to localhost
            const response = await fetch(`${backendURL}/quiz/api/submit`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ answers })
            });
            if (!response.ok) {
                throw new Error(`Server responded with status ${response.status}`);
            }
            const result = await response.json();
            displayResult(result);
            await loadQuiz(); // Reload the quiz after restarting
        } catch (error) {
            console.error('Error submitting quiz:', error);
            resultContainer.innerHTML = `<p>Error submitting quiz: ${error.message}</p>`;
        }
    }

    function displayResult(result) {
        resultContainer.innerHTML = `<h2>Your Score: ${result.score}</h2>`;
        result.results.forEach(detail => {
            const detailElement = document.createElement('p');
            detailElement.textContent = `Question ${detail.question_id}: ${detail.correct ? 'Correct' : 'Incorrect'}`;
            resultContainer.appendChild(detailElement);
        });
    }

    window.restartQuiz = async function() {
        try {
            const backendURL = process.env.BACKEND_URL || 'http://localhost:8000'; // Use the provided backend URL or default to localhost
            const response = await fetch(`${backendURL}/quiz/api/restart`, {
                method: 'POST'
            });
            if (!response.ok) {
                throw new Error(`Server responded with status ${response.status}`);
            }
            const result = await response.json();
            alert(result.message); // Display restart message
            resultContainer.innerHTML = '';
            await loadQuiz(); // Reload the quiz after restarting
        } catch (error) {
            console.error('Error restarting quiz:', error);
            resultContainer.innerHTML = `<p>Error restarting quiz: ${error.message}</p>`;
        }
    }
    loadQuiz();
});
