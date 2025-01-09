class Room(object):
    def __init__(self, name, description, north, west, east, south, up, down):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down

    def move(self, directions):
        global current_node
        current_node = globals()[getattr(self, directions)]


ENTRANCE = Room('Freddy Fazbear Entrance',
                'Your at the entrance of the new place where your going to work. The place is called '
                'Freddy Fazbear pizzaera',
                'WAITING_ROOM', None, 'SECURITY_PUPPET_ROOM', None, None, None,)

SECURITY_PUPPET_ROOM = Room('security puppet room',
                            'This room will protect children who are trying to leave without their parent.',
                            None, 'ENTRANCE', None, None, None, None)
WAITING_ROOM = Room('Waiting Room',
                    'This place is were people will wait until they could get a bracelet to enter the playhouse.',
                    'DINNING_ROOM', 'BATHROOM', 'OFFICE_ROOM', 'ENTRANCE', None, None)
OFFICE_ROOM = Room('Office Room',
                   'This place is were the manger will work. maybe',
                   None, 'WAITING_ROOM', 'DATA_BASE', None, None, None)
BATHROOM = Room('Bathroom',
                "You know why you're here. There seem to be a hatch in one of the stalls. would you like to open it?",
                None, None, 'WAITING_ROOM', None, None, 'BELOW_BUILDING')
DINNING_ROOM = Room('Dinning Room',
                    'Here were your going to eat after or before you go into the buffet.',
                    'STAGE', 'GAME_ROOM', 'FOOD_ROOM', 'WAITING_ROOM', None, None)
GAME_ROOM = Room('Game Room',
                 'This place is were your children going to play games.',
                 None, 'FOXY_ROOM', 'DINNING_ROOM', None, None, None)
FOXY_ROOM = Room('Foxy Room',
                 'Foxy is the most lovable character.',
                 None, None, 'GAME_ROOM', None, None, None)
FOOD_ROOM = Room('Food Room',
                 'Do you not known why we use this place.',
                 None, 'DINNING_ROOM', None, None, None, None)
STAGE = Room('Stage',
             'This is were the animatronic is going to perform. We have Freddy, Bonnie, and chika.',
             'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None)
STORAGE_ROOM = Room('Stage',
                    'This is were we keep extras stuff. Like a dead bo- dead battery.',
                    'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None)
BACK_OF_THE_BUILDING = Room('Back of the building',
                            'There nothing here but blo- balloons.',
                            'SECURITY_ROOM', 'STORAGE_ROOM', 'STAFF_ROOM', 'STORAGE_ROOM', None, None)
SECURITY_ROOM = Room('Security Room',
                     'This is were your going to work.',
                     None, None, None, 'BACK_OF_THE_BUILDING', None, None)
STAFF_ROOM = Room('Staff Room',
                  'Other staff will take a break in here.',
                  'BACK_OF_THE_BUILDING', None, 'ANIMATRONICS', None, None, None)
ANIMATRONICS = Room('Animatronics room',
                    "There are 4 animatronics that are a work in progress.",
                    None, 'STAFF_ROOM', None, 'DATA_BASE', None, None)
DATA_BASE = Room('Data base',
                 'This is were we controlled the animatronics.',
                 'ANIMATRONICS', None, None, 'OFFICE', None, None)
BELOW_BUILDING = Room('Below building',
                      'You fell and found a strange place. it dark.',
                      None, None, 'ELEVATOR', None, 'BATHROOM', None)
ELEVATOR = Room('Elevator',
                'It seem the elevator take you below or up. Would you like to go up or down?',
                'CONTROL_ROOM', 'BELOW_BUILDING', 'NOTHING', None, 'BATHROOM', 'CONTROL_PANEL')
NOTHING = Room('Nothing',
               'There nothing here but rocks.',
               None, 'ELEVATOR', None, None, None, None)
CONTROL_PANEL = Room('Control panel',
                     'There seem to be a button that does something.',
                     'CONTROL_PANEL_2', None, 'BALLORA_AUDITORIUM', 'ELEVATOR', None, None)
BALLORA_AUDITORIUM = Room('Ballora Auditorium',
                          "'There seem to be something there but can't make out what it is.",
                          'FUN_TIME_AUDITORIUM', 'CONTROL_PANEL', None, None, None, None)
FUN_TIME_AUDITORIUM = Room('Fun time Auditorium',
                           "There also something there but can't make out what it is",
                           None, 'FOXY_AUDITORIUM', None, 'BALLORA_AUDITORIUM', None, None)
FOXY_AUDITORIUM = Room('Foxy Auditorium',
                       'You hear something but was to fainted to figure out.',
                       None, None, 'FUN_TIME_AUDITORIUM', None, None, None)
CONTROL_PANEL_2 = Room('Control Panel for Baby',
                       'There are a lot of button that does something. but what?',
                       None, None, None, 'CONTROL_PANEL', None, None)
BABY_AUDITORIUM = Room('Baby Auditorium',
                       'you find something very odd, familiar, but    there something     very     disturbing.',
                       None, None, None, 'CONTROL_PANEL_2', None, None)

current_node = ENTRANCE
direction = ['north', 'south', 'east', 'west', 'up', 'down']
short_direction = ['n', 's', 'e', 'w', 'u', 'd']

while True:
    print(current_node.name)
    print(current_node.description)
    command = input(':').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = direction[pos]
    if command in direction:
        try:
            current_node.move(command)
        except KeyError:
            print("Are you a baka, there is nothing there")
    else:
        print("Command unknown, are you a baka")