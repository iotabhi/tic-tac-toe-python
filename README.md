# tic-tac-toe-python
A robust, console-based Tic-Tac-Toe game featuring smart AI logic and cross-platform support. Built with Python.
# 🎮 Tic-Tac-Toe in Python (v1.0)
![Status](https://img.shields.io/badge/status-stable-green?style=flat-square) ![Version](https://img.shields.io/badge/version-1.0-blue?style=flat-square) ![Language](https://img.shields.io/badge/language-Python_3-yellow?style=flat-square)

A robust, console-based implementation of the classic Tic-Tac-Toe game. This project demonstrates Python logic control, input validation, and basic game AI.

## 🚀 Features

* **Single Player Mode:** Play against the computer.
* **Smart(ish) AI:** The computer strategically starts in the center to maximize winning chances and blocks simple moves.
* **Robust Input Validation:** The game handles errors gracefully (prevents crashes if you type letters, symbols, or out-of-bounds numbers).
* **Cross-Platform UI:** Automatically detects your Operating System (Windows vs. Mac/Linux) to clear the terminal screen for a clean game experience.
* **Replayability:** Loop mechanism allows multiple rounds without restarting the script.

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Libraries:** `random`, `os` (Standard Library only, no external installations required)

## 📋 How to Run

1.  **Clone the repository** (or download the files):
    ```bash
    git clone [https://github.com/iotabhi/tic-tac-toe-python.git](https://github.com/iotabhi/tic-tac-toe-python.git)
    ```
2.  **Navigate to the folder:**
    ```bash
    cd tic-tac-toe-python
    ```
3.  **Run the game:**
    ```bash
    python tictactoe.py
    ```

## 🕹️ How to Play

The board is numbered **1-9** starting from the top-left:
+-------+-------+-------+
|   1   |   2   |   3   | 
+-------+-------+-------+ 
|   4   |   X   |   6   |
+-------+-------+-------+
|   7   |   8   |   9   | 
+-------+-------+-------+
* You play as **O**.
* The Computer plays as **X**.
* Enter the number corresponding to the square where you want to place your mark.

## 🧠 Logic Highlights

This project implements fundamental game logic concepts:
* **Victory Check:** A specialized function `victory_for()` uses Python's `all()` function to efficiently check rows, columns, and diagonals.
* **Turn Handling:** The `enter_move()` function ensures users cannot overwrite existing moves.
* **OS Interfacing:** Uses `os.system()` to manage the console display dynamically.

## 👤 Author

**[Abhilasha Manjeet]**
* Connect with me on [LinkedIn](https://www.linkedin.com/in/abhilasha-manjeet-339903243?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app )

---
*This project was created for educational purposes to master Python control flow and data structures.*
