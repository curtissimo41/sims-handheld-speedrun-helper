import csv
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert


if __name__ == "__main__":
    game = input('Enter game (sbo_gba/urbz_gba): ').lower()
    if game != 'sbo_gba' and game != 'urbz_gba':
        print('Invalid game.')
        exit()

    # remove old db file if one exists
    try:
        os.remove(f'{game}_npc_schedules.db')
    except:
        pass

    engine = create_engine(f'sqlite:///{game}_npc_schedules.db', echo = True)
    meta = MetaData()

    with open(f'{game}_npc_schedules.csv', newline='') as npc_schedule:
        reader = csv.reader(npc_schedule, delimiter=',')
        for row in reader:
            npc = '_'.join(row[0].split()).lower()
            new_npc_table = Table(
                npc, meta,
                Column('day', String),
                Column('hour', Integer),
                Column('location', String)
            )

            meta.create_all(engine)

            i = 0
            for location in row[1:]:
                day_int, hour = divmod(i, 24)
                day = ''
                match day_int:
                    case 0:
                        day = 'Monday'
                    case 1:
                        day = 'Tuesday'
                    case 2:
                        day = 'Wednesday'
                    case 3:
                        day = 'Thursday'
                    case 4:
                        day = 'Friday'
                    case 5:
                        day = 'Saturday'
                    case 6:
                        day = 'Sunday'
                    case _:
                        pass

                query = insert(new_npc_table).values(day=day, hour=hour, location=location)
                with engine.connect() as conn:
                    conn.execute(query)
                    conn.commit()

                i += 1
