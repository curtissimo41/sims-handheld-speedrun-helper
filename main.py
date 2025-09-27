from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.sql import select
from tkinter import *
from tkinter import ttk


engine = create_engine('sqlite:///urbz_npc_schedule.db')
meta = MetaData()

npc_list = [
    'Bayou Boo', 'Berkeley Clodd', 'Cannonball Coleman', 'Crawdad Clem', 'Crystal', 'Daddy Bigbucks',
    'Darius', 'Detective Dan D. Mann', 'Dusty Hogg', 'Ephram Earl', 'Ewan Watahmee',
    'Giuseppi Mezzoalto', 'Gramma Hattie', 'Harlan King', 'Kris Thistle', 'Lily Gates',
    'Lincoln Broadsheet', 'Lottie Cash', 'Luthor L. Bigbucks', 'Mambo Loa', 'Maximillian Moore',
    'Misty Waters', 'Olde Salty', 'Phoebe Twiddle', 'Polly Nomial', 'Pritchard Locksley',
    'Roxanna Moxie', 'Sue Pirnova', 'Theresa Bullhorn', 'Heidi Shadows (Cheat Ninja)'
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


def get_location(npc_name, day, hour):
    try:
        if npc_name == 'Heidi Shadows (Cheat Ninja)':
            npc_name = 'heidi_shadows'
        else:
            npc_name = ''.join(npc_name.split('.')).lower()  # remove the '.' first for Dan & Luthor
            npc_name = '_'.join(npc_name.split()).lower()
            print(npc_name)

        locations = Table(
            npc_name,
            meta,
            autoload = True,
            autoload_with = engine
        )

        s = select([locations]).where((locations.c.day == day) & (locations.c.hour == hour))
        result = engine.connect().execute(s).fetchall()[0][2]

        location.set(result)
    except:
        pass


if __name__ == '__main__':
    main = Tk()

    # window properties
    main.title('Sims Handheld Speedrun Helper')
    main.geometry('500x300')
    main.resizable(False, False)

    mainframe = ttk.Frame(main, padding=(3, 3, 12, 12))
    mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

    # NPC name entry row
    ttk.Label(mainframe, text='Urb Name: ').grid(column=1, row=1, sticky=W)
    npc_name = StringVar()
    npc_menu = ttk.Combobox(mainframe, state='readonly', values=npc_list, textvariable=npc_name)
    npc_menu.set('Select an Urb')
    npc_menu.grid(column=2, row=1, sticky=W)

    # Day of the week row
    ttk.Label(mainframe, text='Day of the Week: ').grid(column=1, row=2, sticky=W)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = StringVar()
    day_menu = ttk.Combobox(mainframe, state='readonly', values=days, textvariable=day)
    day_menu.set('Select a Day')
    day_menu.grid(column=2, row=2, sticky=W)

    # Hour of the day row
    ttk.Label(mainframe, text='Hour of the Day: ').grid(column=1, row=3, sticky=W)
    hour = StringVar()
    hour_menu = ttk.Combobox(mainframe, state='readonly', values=hours_list, textvariable=hour)
    hour_menu.set('Select an Hour')
    hour_menu.grid(column=2, row=3, sticky=W)

    # Location (output) row
    ttk.Label(mainframe, text='Location: ').grid(column=1, row=4, sticky=W)
    location = StringVar()
    ttk.Label(mainframe, textvariable=location).grid(column=2, row=4, sticky=W)

    npc_menu.bind(
        '<<ComboboxSelected>>',
        lambda event: get_location(npc_name.get(), day.get(), hours_dict[hour.get()])
    )
    day_menu.bind(
        '<<ComboboxSelected>>',
        lambda event: get_location(npc_name.get(), day.get(), hours_dict[hour.get()])
    )
    hour_menu.bind(
        '<<ComboboxSelected>>',
        lambda event: get_location(npc_name.get(), day.get(), hours_dict[hour.get()])
    )

    main.mainloop()
