# 🕹️ Hangman Game - Python CLI Edition

Welcome to the **Hangman Game**, a classic word-guessing challenge implemented in Python using clean and modular code. This terminal-based project tests your vocabulary and problem-solving skills in an interactive and engaging way. Designed with simplicity and educational value in mind, this game demonstrates file handling, modular programming, and control structures — making it an excellent portfolio piece for aspiring developers.

---

## 🚀 Features

- Terminal-based user interaction
- Dynamic word list loaded from external file (`words.py`)
- Clean UI with ASCII art for better gameplay experience
- Tracks number of incorrect guesses
- Case-insensitive input handling
- Modular and scalable design

---

## 🛠️ Technologies Used

- **Python 3.6+**
- Standard Python libraries: `random`, `string`

---

## 🗂️ Project Structure

hangman/
├── Hangman.py # Main script that runs the game logic
├── words.py # Word list module for fetching random words
└── README.md # Project documentation

---

## 🧑‍💻 How It Works

- A word is randomly selected from a predefined list.
- The player guesses one letter at a time.
- The game continues until the word is guessed or the maximum number of incorrect attempts is reached.
- Visual feedback via ASCII-based hangman stages helps the player track progress.

---

## 📸 Screenshots

![Screen Shot 2025-06-03 at 12 33 28 AM](https://github.com/user-attachments/assets/389cc970-ccf7-4e78-b8b1-89cbf72d6d93)
![Screen Shot 2025-06-03 at 12 33 46 AM](https://github.com/user-attachments/assets/23ba7b18-fdc5-4a44-809a-41b0c5b3d80f)
![Screen Shot 2025-06-03 at 12 34 51 AM](https://github.com/user-attachments/assets/ccfcb479-a095-48fb-b747-cbf9f1ab7c27)




---

## 📦 Installation

### Step 1: Clone the Repository
```bash
git clone https://github.com/your-username/hangman-python.git
cd hangman-python
```
###Step 2: Run the Game
```bash
python Hangman.py
```
---

## 🔧 Requirements

- Python 3.6 or higher
- No external dependencies required

---

## 🔮 Future Enhancements

- Add difficulty levels (easy/medium/hard)
- GUI version using tkinter or PyGame
- Multiplayer mode or leaderboard system
- Add sound effects and animations
