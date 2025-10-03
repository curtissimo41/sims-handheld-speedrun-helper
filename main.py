from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import select
from tkinter import *
from tkinter import ttk


days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

game_dict = {
    'The Urbz': 'urbz',
    'The Sims Bustin\' Out': 'sbo'
}

game_list = [
    'The Urbz',
    'The Sims Bustin\' Out'
]

sbo_npc_list = [
    'Bucki Brock', 'Chet R. Chase', 'Claire Clutterbell', 'Daddy Bigbucks', 'Daschell Swank',
    'Detective Dan D. Mann', 'Duane Doldrum', 'Dusty Hogg', 'Eddie Renaline', 'Ephram Earl',
    'Giuseppi Mezzoalto', 'Hester Primm', 'Lottie Cash', '\'Mad\' Willy Hurtzya',
    'Maximillion Moore', 'Mel Odious', 'Misty Waters', 'Nicki Knack', 'Nora Zeal-Ott',
    'O\' Phil McClean', 'Olde Salty', 'Uncle Hayseed', 'Vera Vex', 'Vernon Peeve', 'Velocirooster',
    'Heidi Shadows (Cheat Ninja)'
]

urbz_npc_list = [
    'Bayou Boo', 'Berkeley Clodd', 'Cannonball Coleman', 'Crawdad Clem', 'Crystal', 'Daddy Bigbucks',
    'Darius', 'Detective Dan D. Mann', 'Dusty Hogg', 'Ephram Earl', 'Ewan Watahmee',
    'Giuseppi Mezzoalto', 'Gramma Hattie', 'Harlan King', 'Kris Thistle', 'Lily Gates',
    'Lincoln Broadsheet', 'Lottie Cash', 'Luthor L. Bigbucks', 'Mambo Loa', 'Maximillian Moore',
    'Misty Waters', 'Olde Salty', 'Phoebe Twiddle', 'Polly Nomial', 'Pritchard Locksley',
    'Roxanna Moxie', 'Sue Pirnova', 'Theresa Bullhorn', 'Heidi Shadows (Cheat Ninja)'
]

club_xizzle_schedule = {
    0: ['Berkeley Clodd', 'Ephram Earl', 'Kris Thistle', 'Lottie Cash', 'Olde Salty', 'Phoebe Twiddle'],
    1: ['Crystal', 'Ewan Watahmee', 'Kris Thistle', 'Lily Gates', 'Roxanna Moxie'],
    2: ['Cannonball Coleman', 'Giuseppi Mezzoalto', 'Luthor L. Bigbucks', 'Maximillian Moore', 'Misty Waters'],
    3: ['Darius', 'Dusty Hogg', 'Polly Nomial', 'Pritchard Locksley', 'Sue Pirnova', 'Theresa Bullhorn']
}

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


class helper_gui:
    def __init__(self, main):
        self.main = main

        # window properties
        self.main.title('Sims Handheld Speedrun Helper')
        self.main.geometry('500x300')
        self.main.resizable(False, False)

        self.mainframe = ttk.Frame(main, padding=(3, 3, 12, 12))
        self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

        # Game selection row
        self.game_label = ttk.Label(self.mainframe, text='Game: ')
        self.game_name = StringVar()
        self.game_menu_dropdown = ttk.Combobox(self.mainframe, state='readonly', values=game_list,
                                               textvariable=self.game_name)
        self.game_menu_dropdown.set('Select a Game')

        self.game_label.grid(column=1, row=1, sticky=W)
        self.game_menu_dropdown.grid(column=2, row=1, sticky=W)
        self.game_menu_dropdown.bind(
            '<<ComboboxSelected>>',
            lambda event: self.generate_window(game_dict[self.game_name.get()])
        )

        # NPC name entry row
        self.npc_selection_label = ttk.Label(self.mainframe)
        self.npc_selection_label.grid(column=1, row=2, sticky=W)

        self.npc_name = StringVar()
        self.npc_menu_dropdown = ttk.Combobox(self.mainframe, state='readonly', textvariable=self.npc_name)
        self.npc_menu_dropdown.bind(
            '<<ComboboxSelected>>',
            lambda event: self.get_location(game_dict[self.game_name.get()], self.npc_name.get(), self.day.get(),
                                            hours_dict[self.hour.get()])
        )

        # Day of the week row
        self.day_label = ttk.Label(self.mainframe)
        self.day_label.grid(column=1, row=3, sticky=W)

        self.day = IntVar()
        self.day_entry = ttk.Entry(self.mainframe)

        # Hour of the day row
        self.hour_label = ttk.Label(self.mainframe)
        self.hour_label.grid(column=1, row=4, sticky=W)

        self.hour = StringVar()
        self.hour_menu = ttk.Combobox(self.mainframe, state='readonly', values=hours_list, textvariable=self.hour)
        self.hour_menu.bind(
            '<<ComboboxSelected>>',
            lambda event: self.get_location(game_dict[self.game_name.get()], self.npc_name.get(), self.day.get(),
                                            hours_dict[self.hour.get()])
        )

        # Location row
        self.location_label = ttk.Label(self.mainframe)
        self.location = ttk.Label(self.mainframe)

    def get_location(self, game, npc_name, day, hour):
        # check if NPC currently in Club Xizzle
        atClubXizzle = False
        xizzle_group, _ = divmod(hour, 6)
        if npc_name in club_xizzle_schedule[xizzle_group]:
            atClubXizzle = True

        # fix up NPC name
        if npc_name == 'Heidi Shadows (Cheat Ninja)':
            npc_name = 'heidi_shadows'
        else:
            npc_name = ''.join(npc_name.split('.')).lower() # remove the '.' first for Dan, Luthor, Chet, etc.
            npc_name = '_'.join(npc_name.split())

        # if SBO, convert number day to string day
        if game == 'sbo':
            try:
                if int(day) <= 0:
                    raise
                day = days[int(day) % 7 - 1]
            except:
                self.location['text'] = ''
                return

        try:
            engine = create_engine(f'sqlite:///npc_schedules/{game}_npc_schedules.db')
            meta = MetaData()

            locations = Table(npc_name, meta,
                Column('day', String),
                Column('hour', Integer),
                Column('location', String)
            )

            s = select(locations).where((locations.c.day == day) & (locations.c.hour == hour))
            result = engine.connect().execute(s).fetchall()[0][2]

            # add Club Xizzle to location accordingly
            if atClubXizzle:
                if result == 'UNAVAILABLE':
                    result = 'Club Xizzle'
                else:
                    result = result + ' + Club Xizzle'

            self.location['text'] = result
        except:
            pass

    def generate_window(self, game_name):
        # erase the location whenever the window is regenerated
        self.location['text'] = ''

        # NPC name entry row
        if game_name == 'sbo':
            self.npc_selection_label['text'] = 'Sim Name: '
            self.npc_menu_dropdown['values'] = sbo_npc_list
            self.npc_menu_dropdown.set('Select a Sim')
        elif game_name == 'urbz':
            self.npc_selection_label['text'] = 'Urb Name: '
            self.npc_menu_dropdown['values'] = urbz_npc_list
            self.npc_menu_dropdown.set('Select an Urb')
        self.npc_menu_dropdown.grid(column=2, row=2, sticky=W)

        # Day of the week row
        self.day_entry.grid_forget()
        self.day = StringVar()
        if game_name == 'sbo':
            self.day_label['text'] = 'Day #: '
            self.day_entry = ttk.Entry(self.mainframe, textvariable=self.day)
            self.day_entry.bind(
                '<KeyRelease>',
                lambda event: self.get_location(game_dict[self.game_name.get()], self.npc_name.get(), self.day.get(),
                                                hours_dict[self.hour.get()])
            )
        elif game_name == 'urbz':
            self.day_label['text'] = 'Day of the Week: '
            self.day_entry = ttk.Combobox(self.mainframe, state='readonly', values=days, textvariable=self.day)
            self.day_entry.set('Select a Day')
            self.day_entry.bind(
                '<<ComboboxSelected>>',
                lambda event: self.get_location(game_dict[self.game_name.get()], self.npc_name.get(), self.day.get(),
                                                hours_dict[self.hour.get()])
            )
        self.day_entry.grid(column=2, row=3, sticky=W)

        # Hour of the day row
        self.hour_label['text'] = 'Hour: '
        self.hour_menu.set('12 A.M. | 00:00')
        self.hour_menu.grid(column=2, row=4, sticky=W)

        # Location (output) row
        self.location_label['text'] = 'Location: '
        self.location_label.grid(column=1, row=5, sticky=W)
        self.location.grid(column=2, row=5, sticky=W)


if __name__ == '__main__':
    main = Tk()
    main_gui = helper_gui(main)
    main.mainloop()
