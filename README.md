# 🚢 Python Console Battleship Game

A classic two-player turn-based **Battleship** game implemented in Python for the command-line interface (CLI).

---

## 📌 Features

- **2-Player Local Gameplay:** Pass-and-play mechanic with terminal screen clearing (`\n` padding) to hide setup and board states from opponent.
- **Customizable Fleet Setup:** Includes standard fleet layout with 5 ships of varying lengths (5, 4, 3, 2, 2).
- **Validation Rules:**
  - Out-of-bounds error handling.
  - Prevents ship overlap.
  - Enforces a **1-cell buffer distance** around placed ships (no adjacent touching).
- **Interactive Battle Mechanism:**
  - Fog-of-war for enemy target boards.
  - Immediate extra turn upon landing a successful **Hit (`X`)**.
  - Automatic reveal/marking of surrounding area (`O`) once a ship is fully **sunk**.

---

## 🎮 Board Legend

| Symbol | Description |
| :---: | :--- |
| `~` | Water / Unexplored area |
| `S` | Your Ship position *(hidden from opponent)* |
| `X` | **Hit** target / Damaged ship coordinate |
| `O` | **Miss** / Sunk ship safe margin |

---

## 🛠️ Requirements & Installation

No external dependencies or standard packages are required! Built strictly using core Python modules.

1. **Prerequisites:** Python 3.x installed.
2. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/battleship-cli.git](https://github.com/your-username/battleship-cli.git)
   cd battleship-cli
