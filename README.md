# Sims Handheld Speedrun Helper
Program with useful information for practicing Sims handheld speedruns. Requires Python 3.12 or higher.

* Note: This program is still in VERY early development, and currently only shows locations for NPCs in  The Sims Bustin' Out GBA & The Urbz GBA. Will be greatly expanded in the future.

## Required packages

* [SQLAlchemy 2](https://www.sqlalchemy.org/) - SQL wrapper for Python
* [tkinter](https://tkdocs.com/) - Cross-platform graphical user interface toolkit

## How to run

Install SQLAlchemy & tkinter if you don't have them already:

`pip install sqlalchemy`

`apt-get install python3-tk`

Run the program from the top-level directory:

`python3 main.py`

## Compiling the NPC schedule database

The NPC schedule .csv files and databases have already been provided for you, but if you need to rebuild them, you can do so with make_npc_schedules_db.py

1. Make edits to your .csv file and place it in the npc_schedules directory with these parameters:

    - Filename - \<**sbo** OR **urbz**\>_npc_schedules.csv
    - Row format - \<NPC name\>,location1,location2,...,location168

    Example Filename: `urbz_npc_schedules.csv`

    Example Row: `Berkeley Clodd,Urbania,Glasstown,Carnival,...,Urbania`

2. Open a terminal and run:

    `python3 make_npc_schedules_db.py`
    
    from within the npc_schedules directory.
