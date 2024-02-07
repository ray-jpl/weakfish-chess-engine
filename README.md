# Weakfish

A basic chess engine in Python that you can interact with via UCI commands.

The engine relies on the [python-chess](https://python-chess.readthedocs.io/en/latest/) package for move validation and board representation. 

Search utilises Alpha-Beta pruning and the evaluation function is based on piece value, piece positioning and move value. Move value is based on heuristics such as potential captures and promotions.  

## Setup

```venv\Scripts\activate```

```pip install -r requirements.txt```


To compile the engine

```pyinstaller main.py```


Copy everything in the dist folder into the [lichess-bot repo](https://github.com/lichess-bot-devs/lichess-bot) `\engine` directory


Resources:
- [Chess Programming Wiki](https://www.chessprogramming.org/Main_Page)
- [Healey Codes - Building my own chess engine](https://healeycodes.com/building-my-own-chess-engine)
- [Andreas Stockl - Writing a chess program in one day](https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec)
- [Sebastian Lague - Coding Adventure:Chess](https://youtu.be/U4ogK0MIzqk)
- [Sebastian Lague - Algorithms Explained – minimax and alpha-beta pruning](https://youtu.be/l-hh51ncgDI)