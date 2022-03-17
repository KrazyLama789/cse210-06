
# cse210-6
Final Project design

casting:
classes: #Jennifer
    adventurer
    boss

    Advanced:
        chest
        items #keys?

images: #Camden
    adventurer
    boss
    background

    Advanced:
        chest
        key

script: #Mary
    display adventurer
    display mob
    display player stats
    walk from one screen to the next
    start combat when entering a room with a mob
    update player stuts
    combat sequence
    combat resolution

    when in combat:
        display mob stats
        choose an action
        update player stuts
        combat sequence
        combat resolution

    advanced:
        pick up items
        more complex combat action
        tresure chest

services: #Kosei
    - movement controlls (left and right)
    - interation (space bar)
    - choose action (1 2 3 4)

