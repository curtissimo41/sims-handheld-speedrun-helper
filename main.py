from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
import tkinter as tk
from tkinter import ttk


club_xizzle_schedule = {
    0: ['Berkeley Clodd', 'Ephram Earl', 'Kris Thistle', 'Lottie Cash', 'Olde Salty',
        'Phoebe Twiddle'],
    1: ['Crystal', 'Ewan Watahmee', 'Kris Thistle', 'Lily Gates', 'Roxanna Moxie'],
    2: ['Cannonball Coleman', 'Giuseppi Mezzoalto', 'Luthor L. Bigbucks','Maximillian Moore',
        'Misty Waters'],
    3: ['Darius', 'Dusty Hogg', 'Polly Nomial', 'Pritchard Locksley', 'Sue Pirnova',
        'Theresa Bullhorn']
}

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

game_dict = {
    'The Sims Bustin\' Out (GBA)': 'sbo_gba',
    'The Urbz: Sims in the City (GBA)': 'urbz_gba'
}

game_list = [
    'The Sims Bustin\' Out (GBA)',
    'The Urbz: Sims in the City (GBA)'
]

hours_list = [
    '12 A.M. | 00:00', '1 A.M. | 01:00', '2 A.M. | 02:00', '3 A.M. | 03:00', '4 A.M. | 04:00',
    '5 A.M. | 05:00', '6 A.M. | 06:00', '7 A.M. | 07:00', '8 A.M. | 08:00', '9 A.M. | 09:00',
    '10 A.M. | 10:00', '11 A.M. | 11:00', '12 P.M. | 12:00', '1 P.M. | 13:00', '2 P.M. | 14:00',
    '3 P.M. | 15:00', '4 P.M. | 16:00', '5 P.M. | 17:00', '6 P.M. | 18:00', '7 P.M. | 19:00',
    '8 P.M. | 20:00', '9 P.M. | 21:00', '10 P.M. | 22:00', '11 P.M. | 23:00'
]

hours_dict = {
    hours_list[0]: 0, hours_list[1]: 1, hours_list[2]: 2, hours_list[3]: 3, hours_list[4]: 4,
    hours_list[5]: 5, hours_list[6]: 6, hours_list[7]: 7, hours_list[8]: 8, hours_list[9]: 9,
    hours_list[10]: 10, hours_list[11]: 11, hours_list[12]: 12, hours_list[13]: 13,
    hours_list[14]: 14, hours_list[15]: 15, hours_list[16]: 16, hours_list[17]: 17,
    hours_list[18]: 18, hours_list[19]: 19, hours_list[20]: 20, hours_list[21]: 21,
    hours_list[22]: 22, hours_list[23]: 23
}

sbo_npc_list = [
    'Bucki Brock', 'Chet R. Chase', 'Claire Clutterbell', 'Daddy Bigbucks', 'Daschell Swank',
    'Detective Dan D. Mann', 'Duane Doldrum', 'Dusty Hogg', 'Eddie Renaline', 'Ephram Earl',
    'Giuseppi Mezzoalto', 'Hester Primm', 'Lottie Cash', '`Mad` Willy Hurtzya',
    'Maximilian Moore', 'Mel Odious', 'Misty Waters', 'Nicki Knack', 'Nora Zeal-Ott',
    'O. Phil McClean', 'Olde Salty', 'Uncle Hayseed', 'Vera Vex', 'Vernon Peeve', 'Velocirooster',
    'Heidi Shadows (Cheat Ninja)'
]

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

urbz_npc_list = [
    'Bayou Boo (Chap. 1-4)', 'Bayou Boo (Vampire)', 'Bayou Boo (Chap. 5)', 'Berkeley Clodd',
    'Cannonball Coleman', 'Crawdad Clem', 'Crystal', 'Daddy Bigbucks', 'Darius',
    'Detective Dan D. Mann', 'Dusty Hogg', 'Ephram Earl', 'Ewan Watahmee', 'Giuseppi Mezzoalto',
    'Gramma Hattie', 'Harlan King', 'Kris Thistle', 'Lily Gates', 'Lincoln Broadsheet',
    'Lottie Cash', 'Luthor L. Bigbucks', 'Mambo Loa', 'Maximillian Moore', 'Misty Waters',
    'Olde Salty', 'Phoebe Twiddle', 'Polly Nomial', 'Pritchard Locksley', 'Roxanna Moxie',
    'Sue Pirnova', 'Theresa Bullhorn', 'Heidi Shadows (Cheat Ninja)'
]


class helper_gui:
    def __init__(self, main):
        self.main = main

        # window properties
        self.main.title('Sims Handheld Speedrun Helper')
        self.main.geometry('850x760')
        self.main.resizable(False, False)

        # Game selection row
        self.titlegrid = ttk.Frame(self.main, padding=(3, 3, 3, 3))
        self.titlegrid.pack(side=tk.TOP)

        self.game_label = ttk.Label(self.titlegrid, text='Game: ')
        self.game_name = tk.StringVar()
        self.game_menu_dropdown = ttk.Combobox(
            self.titlegrid,
            state='readonly',
            values=game_list,
            textvariable=self.game_name,
            width=26
        )
        self.game_menu_dropdown.set('Select a Game')

        self.game_label.grid(column=0, row=0, sticky=tk.E)
        self.game_menu_dropdown.grid(column=1, row=0, sticky=tk.W)
        self.game_menu_dropdown.bind(
            '<<ComboboxSelected>>',
            lambda event: self.generate_npc_location_frame(game_dict[self.game_name.get()])
        )

        # horizontal separator under game choice
        self.separator_h1 = ttk.Separator(self.main, orient=tk.HORIZONTAL)
        self.separator_h1.pack(side=tk.TOP, fill=tk.X, pady=5)

        # initialize NPC location frame
        self.npc_location_frame = ttk.Frame(self.main)

        # horizontal separator under game frame
        self.separator_h2 = ttk.Separator(self.main, orient=tk.HORIZONTAL)

        # initialize NPC interactions frame
        self.interactions = []
        self.interactions_frame = ttk.Frame(self.main)

        self.separator_v1 = ttk.Separator(self.interactions_frame, orient=tk.VERTICAL)
        self.separator_v2 = ttk.Separator(self.interactions_frame, orient=tk.VERTICAL)

    def generate_npc_location_frame(self, game_name):
        # destroy old items, recreate new items
        self.npc_location_frame.destroy()
        self.separator_h2.destroy()
        self.interactions_frame.destroy()

        self.npc_location_frame = ttk.Frame(self.main)
        self.npc_location_frame.pack(side=tk.TOP, anchor=tk.NW)

        # NPC name entry row
        self.npc_selection_label = ttk.Label(self.npc_location_frame, width=15)
        self.npc_selection_label.grid(column=0, row=0, sticky=tk.W, padx=4, pady=4)

        self.npc_name = tk.StringVar()
        self.npc_menu_dropdown = ttk.Combobox(
            self.npc_location_frame,
            state='readonly',
            textvariable=self.npc_name,
            width=22
        )

        if game_name == 'sbo_gba':
            self.npc_selection_label['text'] = 'Sim Name: '
            self.npc_menu_dropdown['values'] = sbo_npc_list
            self.npc_menu_dropdown.set('Select a Sim')
            self.npc_menu_dropdown.bind(
                '<<ComboboxSelected>>',
                lambda event: self.sbo_gba_npc_update(
                    'sbo_gba',
                    self.npc_name.get(),
                    hours_dict[self.hour.get()]
                )
            )
        elif game_name == 'urbz_gba':
            self.npc_selection_label['text'] = 'Urb Name: '
            self.npc_menu_dropdown['values'] = urbz_npc_list
            self.npc_menu_dropdown.set('Select an Urb')
            self.npc_menu_dropdown.bind(
                '<<ComboboxSelected>>',
                lambda event: self.urbz_gba_npc_update(
                    'urbz_gba',
                    self.npc_name.get(),
                    self.day.get(),
                    hours_dict[self.hour.get()]
                )
            )
        self.npc_menu_dropdown.grid(column=1, row=0, sticky=tk.W)

        # Day of the week row
        self.day_label = ttk.Label(self.npc_location_frame, width=15)
        self.day_label.grid(column=0, row=1, sticky=tk.W, padx=4, pady=4)

        if game_name == 'sbo_gba':
            self.day_label['text'] = 'Day #: '
            self.day = tk.IntVar()
            self.day_entry = ttk.Entry(self.npc_location_frame, width=20, textvariable=self.day)
            self.day_entry.bind(
                '<KeyRelease>',
                lambda event: self.sbo_gba_get_location(
                    self.npc_name.get(),
                    hours_dict[self.hour.get()]
                )
            )
        elif game_name == 'urbz_gba':
            self.day_label['text'] = 'Day of the Week: '
            self.day = tk.StringVar()
            self.day_entry = ttk.Combobox(
                self.npc_location_frame,
                state='readonly',
                values=days,
                textvariable=self.day,
                width=22
            )
            self.day_entry.set('Select a Day')
            self.day_entry.bind(
                '<<ComboboxSelected>>',
                lambda event: self.urbz_gba_get_location(
                    self.npc_name.get(),
                    self.day.get(),
                    hours_dict[self.hour.get()]
                )
            )
        self.day_entry.grid(column=1, row=1, sticky=tk.W)

        # Hour of the day row
        self.hour_label = ttk.Label(self.npc_location_frame, width=15, text='Hour: ')
        self.hour_label.grid(column=0, row=2, sticky=tk.W, padx=4, pady=4)

        self.hour = tk.StringVar()
        self.hour_menu = ttk.Combobox(
            self.npc_location_frame,
            state='readonly',
            values=hours_list,
            textvariable=self.hour,
            width=22
        )
        if game_name == 'sbo_gba':
            self.hour_menu.bind(
                '<<ComboboxSelected>>',
                lambda event: self.sbo_gba_get_location(
                    self.npc_name.get(),
                    hours_dict[self.hour.get()]
                )
            )
        elif game_name == 'urbz_gba':
            self.hour_menu.bind(
                '<<ComboboxSelected>>',
                lambda event: self.urbz_gba_get_location(
                    self.npc_name.get(),
                    self.day.get(),
                    hours_dict[self.hour.get()]
                )
            )
        self.hour_menu.set('12 A.M. | 00:00')
        self.hour_menu.grid(column=1, row=2, sticky=tk.W)

        # Location row
        self.location_label = ttk.Label(self.npc_location_frame, width=15, text='Location: ')
        self.location_label.grid(column=0, row=3, sticky=tk.W, padx=4, pady=4)
        self.location = ttk.Label(self.npc_location_frame, width=50)
        self.location.grid(column=1, row=3, sticky=tk.W)

        # NPC image column
        self.npc_img = tk.PhotoImage()
        self.npc_img_label = tk.Label(self.npc_location_frame, image=self.npc_img)
        self.npc_img_label.grid(column=15, row=0, rowspan=6, sticky=tk.E)

        # second separator (only show once a game is chosen)
        self.separator_h2 = ttk.Separator(self.main, orient=tk.HORIZONTAL)
        self.separator_h2.pack(side=tk.TOP, fill=tk.X, pady=5)

        # Interactions grid
        self.interactions_frame = ttk.Frame(self.main)
        self.interactions_frame.pack(side=tk.TOP, anchor=tk.NW, padx=3)

    def sbo_gba_get_location(self, npc_name, hour):
        # Convert number day to string day
        try:
            day = self.day.get()
            if day <= 0:
                raise
            day = days[int(day) % 7 - 1]
        except:
            self.location['text'] = ''

        try:
            engine = create_engine(f'sqlite:///npc_schedules/sbo_gba_npc_schedules.db')
            meta = MetaData()

            locations = Table(
                self.make_npc_name_db_safe(npc_name),
                meta,
                Column('day', String),
                Column('hour', Integer),
                Column('location', String)
            )
            s = select(locations).where((locations.c.day == day) & (locations.c.hour == hour))
            result = engine.connect().execute(s).fetchall()[0][2]
            engine.dispose()

            self.location['text'] = result
        except:
            self.location['text'] = ''

    def sbo_gba_npc_update(self, game, npc_name, hour):
        # update NPC image
        self.get_npc_image(game, npc_name)

        # update NPC location
        self.sbo_gba_get_location(npc_name, hour)

        # update NPC interactions table (will be implemented later)
        # self.build_interactions_grid('urbz', npc_name)

    def sims2_gba_get_location(self, npc_name, episode, hour):
        pass

    def urbz_gba_get_location(self, npc_name, day, hour):
        try:
            engine = create_engine(f'sqlite:///npc_schedules/urbz_gba_npc_schedules.db')
            meta = MetaData()

            locations = Table(
                self.make_npc_name_db_safe(npc_name),
                meta,
                Column('day', String),
                Column('hour', Integer),
                Column('location', String)
            )
            s = select(locations).where((locations.c.day == day) & (locations.c.hour == hour))
            result = engine.connect().execute(s).fetchall()[0][2]
            engine.dispose()
        except:
            self.location['text'] = ''
            return

        # add Club Xizzle to location accordingly
        xizzle_group, _ = divmod(hour, 6)
        if npc_name in club_xizzle_schedule[xizzle_group]:
            if result == 'UNAVAILABLE':
                result = 'Club Xizzle'
            else:
                result += ' + Club Xizzle'

        self.location['text'] = result

    def urbz_gba_npc_update(self, game, npc_name, day, hour):
        # update NPC image
        self.get_npc_image(game, npc_name)

        # update NPC location
        self.urbz_gba_get_location(npc_name, day, hour)

        # update NPC interactions table
        self.build_interactions_grid('urbz_gba', npc_name)

    def build_interactions_grid(self, game, npc_name):
        npc_name = self.make_npc_name_db_safe(npc_name)

        # completely clear previous interactions grid to start
        self.interactions_frame.destroy()
        self.interactions_frame = ttk.Frame(self.main)
        self.separator_v1 = ttk.Separator(self.interactions_frame, orient=tk.VERTICAL)
        self.separator_v2 = ttk.Separator(self.interactions_frame, orient=tk.VERTICAL)
        pos_interactions_label = ttk.Label(self.interactions_frame, width=16,
                                           text='Positive Topics: ', foreground='darkgreen')
        pos_interactions_label.grid(column=0, row=0)
        neut_interactions_label = ttk.Label(self.interactions_frame, width=16,
                                            text='Neutral Topics: ', foreground='darkblue')
        neut_interactions_label.grid(column=3, row=0)
        neg_interactions_label = ttk.Label(self.interactions_frame, width=16,
                                           text='Negative Topics: ', foreground='darkred')
        neg_interactions_label.grid(column=6, row=0)

        if game == 'sbo_gba':
            return

        try:
            engine = create_engine(f'sqlite:///npc_interactions/{game}_npc_interactions.db')
            meta = MetaData()

            interactions = Table(
                npc_name,
                meta,
                Column('interaction', String),
                Column('result', Integer)
            )
            s = select(interactions)
            result = engine.connect().execute(s).fetchall()
            engine.dispose()
        except:
            return

        pos_count, neut_count, neg_count = 0, 0, 0
        for inter in result:
            if inter[1] > 0:
                text = f'{inter[0]} ({inter[1]})'
                row, column = divmod(pos_count, 2)
                pos_inter = ttk.Label(self.interactions_frame, width=15, text=text)
                pos_inter.grid(column=column, row=row+1, sticky=tk.W)
                pos_count += 1
            elif inter[1] == 0:
                text = f'{inter[0]} ({inter[1]})'
                row, column = divmod(neut_count, 2)
                neut_inter = ttk.Label(self.interactions_frame, width=16, text=text)
                neut_inter.grid(column=column+3, row=row+1, sticky=tk.W)
                neut_count += 1
            else:
                text = f'{inter[0]} ({inter[1]})'
                row, column = divmod(neg_count, 2)
                neg_inter = ttk.Label(self.interactions_frame, width=16, text=text)
                neg_inter.grid(column=column+6, row=row+1, sticky=tk.W)
                neg_count += 1
        self.separator_v1.grid(column=2, row=1, rowspan=-(neut_count//-2), sticky=tk.NS, padx=5)
        self.separator_v2.grid(column=5, row=1, rowspan=-(neg_count//-2), sticky=tk.NS, padx=5)

        self.interactions_frame.pack(side=tk.TOP, anchor=tk.N, padx=3, pady=3)

    def get_npc_image(self, game, npc_name):
        npc_name = self.make_npc_name_db_safe(npc_name)
        try:
            self.npc_img = tk.PhotoImage(file=f'resources/character_sprites/{game}/{npc_name}.png')
        except:
            self.npc_img = tk.PhotoImage(file=f'resources/character_sprites/{game}/UNKNOWN.png')
        self.npc_img_label = tk.Label(self.npc_location_frame, image=self.npc_img)
        self.npc_img_label.grid(column=6, row=0, rowspan=5, sticky=tk.W)

    def make_npc_name_db_safe(self, npc_name):
        if npc_name == 'Heidi Shadows (Cheat Ninja)':
            return 'heidi_shadows'
        else:
            return '_'.join(npc_name.split()).lower()


if __name__ == '__main__':
    main = tk.Tk()
    main_gui = helper_gui(main)
    main.mainloop()
