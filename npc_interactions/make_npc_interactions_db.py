import csv
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert


urbz_interactions_list = [
    'Aliens', 'Annoy', 'Apologize', 'Art', 'Bad Pun', 'Bayou', 'Books', 'Brag', 'Call Name',
    'Carnival', 'Cars', 'Cheer Up', 'Coffee Shop', 'Complain', 'Compliment', 'Computers',
    'Construction', 'Cooking', 'Cosmos', 'Crime', 'Cry', 'Dancing', 'Entertain', 'Exercise',
    'Flirt', 'Games', 'Gossip', 'Graveyards', 'Health', 'Hobbies', 'Home', 'Home Decor', 'Hug',
    'Hygiene', 'Insult', 'Intimidate', 'Jail', 'Jibba Jabba', 'Jobs', 'Joke', 'Kiss', 'Law',
    'Lounge', 'Market', 'Miniopolis', 'Movies', 'Museum', 'Music', 'Nature', 'Newspaper', 'Ninjas',
    'Opinion', 'Politics', 'Rep Groups', 'River', 'Rude Gesture', 'Science', 'Secret', 'Shopping',
    'Simoleons', 'Sleep', 'Sports', 'Supernatural', 'Tease', 'TV', 'Theater', 'Travel',
    'University', 'Weather', 'Work', 'World'
]


if __name__ == "__main__":
    game = input('Enter game (sbo/urbz): ').lower()
    if game != 'sbo' and game != 'urbz':
        print('Invalid game.')
        exit()

    # remove old db file if one exists
    try:
        os.remove(f'{game}_npc_interactions.db')
    except:
        pass

    engine = create_engine(f'sqlite:///{game}_npc_interactions.db', echo = True)
    meta = MetaData()

    with open(f'{game}_npc_interactions.csv', newline='') as npc_interactions:
        reader = csv.reader(npc_interactions, delimiter=',')
        for row in reader:
            npc = '_'.join(row[0].split()).lower()
            new_npc_table = Table(
                npc,
                meta,
                Column('interaction', String),
                Column('result', Integer),
            )

            meta.create_all(engine)

            i = 0
            for result in row[1:]:
                interaction = urbz_interactions_list[i]
                query = insert(new_npc_table).values(interaction=interaction, result=result)
                with engine.connect() as conn:
                    conn.execute(query)
                    conn.commit()

                i += 1
