# Conway's Game Of Life
## An implementation of Conway's Game of Life in python using the pygame library.

Learn more about [Conway's Game of Life.](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

![appusage](/assets/appusage.gif)

The [gamelogic](./source/gamelogic.py) module deals strictly with the rules of the game. Lists are used as fields/state with 0/1 depicting dead/alive state of a cell. 

The [main](./source/main.py) module uses pygame to create the gui for the game, translating the logically generated states/fields from lists to graphical cells and keeps generating the next state/field based on the previous state/field. 

## How to run the game
You need to have python installed on your computer(obviously). I recommend running the game in a separate virtual environment.

#### Install the dependencies
``` pip install -r requirements.txt ```

### Run the main file
``` python ./source/main.py ```