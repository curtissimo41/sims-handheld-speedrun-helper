# Sims Handheld Speedrun Helper
Program with useful information for practicing Sims handheld speedruns. Requires Python 3.

* Note: This program is still in VERY early development, and currently only shows locations for NPCs in  Urbz GBA. Will be greatly expanded in the future.

## Required packages

* [SQLAlchemy](https://www.sqlalchemy.org/) - SQL wrapper for Python

## How to run

Install SQLAlchemy if you don't have it already:

`pip install sqlalchemy`

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
