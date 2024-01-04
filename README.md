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



Notes:
- eval_board() function was working as intended. It would sum up the piece values and their piece table value. However that doesnt consider the position of the pieces relative to each other so therefore it would not consider any moves that could capture back potentially. 
- Created search_all_captures() function to evaluate possible capturing moves at the end of the search. This slowed down the engine significantly. The engine tries to do knight moves and in the opening that would mean a lot of spaces where the pawn could capture the knight or a knight captures a pawn and can be taken back by multiple pieces. At this stage I would need to implement tree pruning techniques. 