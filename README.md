Sources:
https://healeycodes.com/building-my-own-chess-engine
https://andreasstckl.medium.com/writing-a-chess-program-in-one-day-30daff4610ec


Bare minimum UCI commands for Lichess:
- uci
- isready
- quit
- go


Setup:
```venv\Scripts\activate```
```pip install -r requirements.txt```

To compile the engine
```pyinstaller main.py```

Copy everything in the dist folder into the lichess-bot repo engine directory


Steps:
1. Create UCI command loop
2. Create basic eval function
3. Create basic search function