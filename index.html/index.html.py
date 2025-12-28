<!DOCTYPE html>
<html>
<head>
    <title>🌟 Звёздное Казино</title>
    <script src="https://telegram.org/js/telegram-web-app.js"></script>
    <style>
        body {
            background: #0a0e29;
            color: white;
            text-align: center;
            font-family: Arial, sans-serif;
            padding: 20px;
            background-image: url('https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?q=80&w=1471');
            background-size: cover;
        }
        .game-box {
            background: rgba(0, 0, 0, 0.8);
            border-radius: 15px;
            padding: 30px;
            margin: 30px auto;
            max-width: 400px;
            border: 3px solid #00eeff;
            box-shadow: 0 0 30px #00eeff;
        }
        button {
            background: #9d4edd;
            color: white;
            border: none;
            padding: 15px;
            margin: 10px;
            border-radius: 10px;
            font-size: 18px;
            cursor: pointer;
            width: 200px;
        }
        .balance {
            font-size: 28px;
            color: gold;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div class="game-box">
        <h1>✨ ЗВЁЗДНОЕ КАЗИНО ✨</h1>
        <div class="balance">✨ <span id="stars">1000</span></div>
        
        <button onclick="playGame()">🎰 КРУТИТЬ СЛОТЫ</button><br>
        <button onclick="playRoulette()">🎡 РУЛЕТКА 50/50</button><br>
        <button onclick="getFree()">🆓 БЕСПЛАТНО</button>
        
        <div id="result" style="margin-top: 20px; font-size: 20px;"></div>
    </div>

    <script>
        // Telegram
        let tg = window.Telegram.WebApp;
        tg.expand();
        
        // Игровая логика
        let stars = 1000;
        
        function playGame() {
            if(stars < 100) {
                showResult("❌ Мало звёзд!", "red");
                return;
            }
            stars -= 100;
            updateStars();
            
            if(Math.random() > 0.6) {
                stars += 300;
                showResult("🎉 ВЫИГРЫШ +300!", "lime");
            } else {
                showResult("💫 Попробуй ещё раз", "orange");
            }
            updateStars();
        }
        
        function playRoulette() {
            if(stars < 50) {
                showResult("❌ Мало звёзд!", "red");
                return;
            }
            stars -= 50;
            updateStars();
            
            let win = Math.random() > 0.5;
            if(win) {
                stars += 100;
                showResult("✅ ВЫИГРЫШ 50/50!", "lime");
            } else {
                showResult("❌ Проигрыш", "red");
            }
            updateStars();
        }
        
        function getFree() {
            stars += 200;
            updateStars();
            showResult("🎁 +200 звёзд!", "gold");
        }
        
        function updateStars() {
            document.getElementById('stars').innerText = stars;
        }
        
        function showResult(text, color) {
            let result = document.getElementById('result');
            result.innerHTML = text;
            result.style.color = color;
        }
    </script>
</body>
</html>