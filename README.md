# Console Game 2048
The task is to create a console-based and web-based version of the popular 2048 game. Players will control the board using the arrow keys (or alternatives like W, A, S, D for up, left, down, and right).
## Description
1. Customizable Grid Size: TAt the start of the game, the user selects the grid size, ranging from 4x4 to 8x8. The gameplay mechanics adapt dynamically to the chosen grid size.
2. Starting Tiles: The game begins with two randomly placed tiles (2 or 4).
3. Player Input: Players can move the tiles in one of four directions:
	- W / Up Arrow: Move up
	- A / Left Arrow: Move left
	- S / Down Arrow: Move down
	- D / Right Arrow: Move right
4. Tile Movement: After each move:
	- All tiles slide in the chosen direction.
	- Identical tiles that collide merge into a single tile (e.g., 2+2=4).
	- A new tile (2 or 4) spawns in an empty cell.
5. Game Over: The game ends when no more moves are possible.
6. Winning Condition: The player wins upon reaching a tile with a value of 2048
## Project Structure
```
my_project/
├── README.md             # Documentation
├── main.py               # Entry point of the application
├── requirements.txt      # Requirements
├── controller/           # Controllers for handling logic
│   └── controller.py
├── model/                # Models for data handling
│   └── model.py
└── view/                 # Views for displaying data
    └── view.py
```
## Installation
1. Clone the repository:
```bash
   git clone https://github.com/Dayad1994/2048.git
   cd 2048
```
2. Install dependencies:
```bash
    pip install -r requirements.txt
```
3. Run the application:
```bash
    python main.py
```
## Usage

To run the application, execute:

```bash
python main.py
```
## Requirements

- Python 3.10 or higher
- Dependencies listed in `requirements.txt`
## License

This project is licensed under the MIT License. See the [LICENSE](https://mit-license.org/) file for details.
## Authors

- [Dayan Iskhakov](https://github.com/Dayad1994)
