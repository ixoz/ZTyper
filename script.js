document.addEventListener('DOMContentLoaded', () => {
    const words = ['apple', 'pear', 'pair', 'mango', 'car', 'bike', 'cat', 'dog', 'horse', 'fan', 'air', 'blue', 'red', 'black', 'grey',
         'hair', 'sudden', 'karachi', 'for', 'today', 'that', 'yesterday', 'fork', 'door', 'color', 'floor', 'flour', 'grape',
         'duck', 'horn', 'crown', 'fish', 'fly', 'plain'];

    let timeleft = 60;
    let matched = 0;
    let not_matched = 0;
    let startTime, endTime;

    const wordElement = document.getElementById('word');
    const wordInput = document.getElementById('word-input');
    const timerCount = document.getElementById('timer-count');
    const scoreLabel = document.getElementById('score-label');
    const scoreCount = document.getElementById('score-count');
    const feedback = document.getElementById('feedback');
    const resultPopup = document.getElementById('result-popup');
    const typingSpeed = document.getElementById('typing-speed');
    const suggestionsList = document.getElementById('suggestions');

    function startGame() {
        document.getElementById('game-container').style.display = 'block';
        const randomIndex = Math.floor(Math.random() * words.length);
        wordElement.textContent = words[randomIndex];
        wordInput.value = '';
        wordInput.focus();

        if (timeleft === 60) {
            startTime = new Date().getTime();
            time();
        }
    }
    function openOffline() {
        window.location.href = 'file:///path/to/your/tkinter/file.py';
    }
    

    function time() {
        if (timeleft > 0) {
            timeleft--;
            timerCount.textContent = timeleft;
            setTimeout(time, 1000);
            if (timeleft < 11) {
                timerCount.style.color = "red";
                if (timeleft === 10) {
                    playSoundCountdown();
                }
            }
        } else {
            endTime = new Date().getTime();
            scoreCount.textContent = matched;
            scoreLabel.textContent = "Your typing speed: ";
            const elapsedTime = (endTime - startTime) / 1000;
            const typingSpeedValue = Math.round((matched / elapsedTime) * 60);
            typingSpeed.textContent = typingSpeedValue;

            if (typingSpeedValue >= 35 && typingSpeedValue <= 40) {
                feedback.textContent = "Average";
            } else if (typingSpeedValue >= 65) {
                feedback.textContent = "Above Average";
            } else {
                feedback.textContent = "Below Average";
            }

            resultPopup.style.display = 'block';
        }
    }

    function playSoundCountdown() {
        const audio = new Audio('buzzer1.mp3');
        audio.play();
    }

    function playSoundBuzzer() {
        const audio = new Audio('buzzer1.mp3');
        audio.play();
    }

    wordInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            if (wordInput.value.trim() === wordElement.textContent) {
                matched++;
            } else {
                not_matched++;
                playSoundBuzzer();
            }
            startGame();
        }
    });

    document.getElementById("start-button").addEventListener("click", function() {
        startGame();
    });
});
