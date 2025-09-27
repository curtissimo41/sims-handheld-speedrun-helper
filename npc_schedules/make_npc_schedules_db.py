import csv
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert


if __name__ == "__main__":
    game = input('Enter game (sbo/urbz): ').lower()
    if game != 'sbo' and game != 'urbz':
        print('Invalid game.')
        exit()

    engine = create_engine(f'sqlite:///{game}_npc_schedules.db', echo = True)
    meta = MetaData()

    with open(f'{game}_npc_schedules.csv', newline='') as npc_schedule:
        reader = csv.reader(npc_schedule, delimiter=',')
        for row in reader:
            npc = '_'.join(row[0].lower().split())
            new_npc_table = Table(
                f'{npc}', meta,
                Column('day', String),
                Column('hour', Integer),
                Column('location', String)
            )

            try:
                new_npc_table.drop(engine)
            except:
                pass
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

                query = insert(new_npc_table).values(
                    day = day,
                    hour = hour,
                    location = location
                )

                engine.connect().execute(query)
                i += 1
