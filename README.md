
# cse210-6
Final Project design

---
## casting:

### actors: #Jennifer

- adventurer
- demon

```
- Advanced:
  - chest
  - items #keys?
```

### images: #Camden
- adventurer
- demon
- background

```
- Advanced:
    - chest
    - key
```

---
## script: #Mary

- display adventurer
- display demon
- display player stats
- walk from one screen to the next
- start combat when entering a room with a demon
- update player stats
- combat sequence
- combat resolution

```
when in combat:
- display demon stats
- choose an action
- update player stats
- combat sequence
- combat resolution
```

```
Advanced:
- pick up items
- more complex combat action
- tresure chest
```

---
## services: #Kosei
- movement controls (left and right)
- interaction (space bar) -- not implemented
- choose action (1 2 3 4)

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 batter 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- batter              (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Matt Manley (manleym@byui.edu)

## sources:

Epic Demon Battle by Juhani Junkala | https://soundcloud.com/juhanijunkala
Music promoted by https://www.free-stock-music.com
Creative Commons Attribution 3.0 Unported License
https://creativecommons.org/licenses/by/3.0/deed.en_US

Sound Bites Provided by https://mixkit.co/free-stock-music

Font: https://vrtxrry.itch.io/dungeonfont