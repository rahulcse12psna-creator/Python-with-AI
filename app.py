from flask import Flask

app = Flask(__name__)

alphabet = [
    ("A", "Apple", "🍎"),
    ("B", "Ball", "⚽"),
    ("C", "Cat", "🐱"),
    ("D", "Dog", "🐶"),
    ("E", "Elephant", "🐘"),
    ("F", "Fish", "🐟"),
    ("G", "Guitar", "🎸"),
    ("H", "Horse", "🐴"),
    ("I", "Ice cream", "🍦"),
    ("J", "Juice", "🧃"),
    ("K", "Kite", "🪁"),
    ("L", "Lion", "🦁"),
    ("M", "Moon", "🌙"),
    ("N", "Nest", "🐦"),
    ("O", "Orange", "🍊"),
    ("P", "Panda", "🐼"),
    ("Q", "Queen", "👑"),
    ("R", "Rocket", "🚀"),
    ("S", "Sun", "☀️"),
    ("T", "Tree", "🌳"),
    ("U", "Umbrella", "☂️"),
    ("V", "Violin", "🎻"),
    ("W", "Watermelon", "🍉"),
    ("X", "Xylophone", "🎼"),
    ("Y", "Yarn", "🧶"),
    ("Z", "Zebra", "🦓"),
]


@app.route('/')
def home():
    cards = ''.join(
        f'''
        <div class="card">
            <div class="letter">{letter}</div>
            <div class="emoji">{emoji}</div>
            <div class="word">{word}</div>
            <button onclick="speak('{letter} for {word}')">🔊 Sound</button>
        </div>
        '''
        for letter, word, emoji in alphabet
    )

    return f'''
    <!doctype html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Alphabet Learning for Kids</title>
        <style>
            * {{ box-sizing: border-box; }}
            body {{
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #fff6a8, #b8ecff, #ffd6e8);
                color: #1d2b53;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 30px 20px 60px;
                text-align: center;
            }}
            h1 {{
                font-size: 3rem;
                color: #ff5a5f;
                margin-bottom: 10px;
            }}
            .subtitle {{
                font-size: 1.5rem;
                margin-bottom: 25px;
                color: #2d3a8c;
            }}
            .grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
                gap: 20px;
            }}
            .card {{
                background: rgba(255,255,255,0.8);
                border-radius: 18px;
                padding: 18px 12px;
                box-shadow: 0 8px 18px rgba(0,0,0,0.08);
                transition: transform 0.2s ease;
            }}
            .card:hover {{
                transform: translateY(-5px);
            }}
            .letter {{
                font-size: 2.8rem;
                font-weight: bold;
                color: #ff7f50;
                margin-bottom: 8px;
            }}
            .emoji {{
                font-size: 4rem;
                margin: 8px 0;
            }}
            .word {{
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 12px;
            }}
            button {{
                background: #4cc9f0;
                color: white;
                border: none;
                border-radius: 10px;
                padding: 10px 16px;
                font-size: 1rem;
                cursor: pointer;
                font-weight: bold;
            }}
            button:hover {{
                background: #3aa9d8;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ABCD</h1>
            <div class="subtitle">Learning for Kids</div>
            <div class="grid">
                {cards}
            </div>
        </div>

        <script>
            function speak(text) {{
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.rate = 0.8;
                utterance.pitch = 1.2;
                window.speechSynthesis.cancel();
                window.speechSynthesis.speak(utterance);
            }}
        </script>
    </body>
    </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
