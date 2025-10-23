# Sims Handheld Speedrun Helper
Program with useful information for practicing Sims handheld speedruns.

Requires Python 3.12 or
higher.

Games currently supported:

- The Sims Bustin' Out (GBA)
- The Urbz: Sims in the City (GBA)

Note: This program is still in VERY early development. Will be greatly expanded in the future.

## Required packages

* [SQLAlchemy 2](https://www.sqlalchemy.org/) - SQL wrapper for Python
* [tkinter](https://tkdocs.com/) - Cross-platform graphical user interface toolkit

## How to run

1. Install SQLAlchemy & tkinter if you don't have them already:

    `pip install sqlalchemy`

    `apt-get install python3-tk`

2. Run the program from the top-level directory:

    `python3 main.py`

## Compiling the NPC schedule databases (currently SBO [GBA] and Urbz [GBA] only)

The NPC schedule .csv files and databases have already been provided for you, but if you need to
make changes and rebuild them, you can do so with npc_schedules/make_npc_schedules_db.py

1. Make edits to your .csv file in the npc_schedules directory with these parameters:

    - Filename - \<**sbo** OR **urbz**\>_<**console**>_npc_schedules.csv
    - Row format - \<NPC name\>,location1,location2,...,location168

    Example Filename: `urbz_gba_npc_schedules.csv`

    Example Row: `Berkeley Clodd,Urbania,Glasstown,Carnival,...,Urbania`

2. Open a terminal and run:

    `python3 make_npc_schedules_db.py`
    
    from within the npc_schedules directory.

## Compiling the NPC interactions databases (currently Urbz [GBA] only)

The NPC interactions .csv files and databases have already been provided for you, but if you need to
make changes and rebuild them, you can do so with npc_interactions/make_npc_interactions_db.py

1. Make edits to your .csv file in the npc_interactions directory with these parameters:

    - Filename - \<**urbz**\>_<**console**>_npc_interactions.csv
    - Row format - \<NPC name\>,aliens,annoy,apologize...,world
        - Note: the interactions are handled in alphabetical order, from 'Aliens' to 'World'

    Example Filename: `urbz_gba_npc_interactions.csv`

    Example Row: `Berkeley Clodd,1,0,-2,...,0`

2. Open a terminal and run:

    `python3 make_npc_interactions_db.py`
    
    from within the npc_interactions directory.

## TODO

- Add `The Urbz: Sims in the City (DS)`:
    - figure out character schedules - some NPCs change locations after Splicer Island is fixed
    - add missing character portraits/sprites:
        - Bayou Boo (Vampire)
        - Ephram Earl (Alive)
        - Harlan King (Pre-Recorded Message)
        - Heidi Shadows (Cheat Ninja)
- Add `The Sims 2 (GBA)`:
    - add all character portraits
    - add locations for all characters on a per-episode basis
    - add interaction percentages for each character
    - add price ranges for collectibles
    - more TBD
- Add `The Sims 2 (DS)`:
    - finish a casual playthrough to see how the game works first...
    - add all character portraits
    - more TBD
- `The Sims Bustin' Out (GBA)`:
    - find a good way to add all interactions (dropdown to select which chapter you are in, maybe?)
    - add missing character portraits/sprites:
        - Daddy Bigbucks
        - 'Mad' Willy Hurtzya
        - Nicki Knack
        - Olde Salty
        - Velocirooster
        - Heidi Shadows (Cheat Ninja)
- `The Urbz: Sims in the City (GBA)`:
    - consider adding all hidden Xizzle Bead locations with screenshots
    - add missing character portraits/sprites:
        - Heidi Shadows (Cheat Ninja)
- Determine if there is any need to add `The Sims Bustin' Out (N-Gage)`
- more TBD