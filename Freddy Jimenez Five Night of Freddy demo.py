'''world_map = {
    'WESTHOUSE': {
        'MAME': 'West of House',
        'DESCRIPTION':'You are west of a whit house',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'

        }
    },
    'SOUTHHOUSE': {
        'NAME': 'South of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'North of House',
        'DESCRIPTION': "Insert Description here",
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}'''

Five_Night_Freddy = {
    'ENTRANCE': {
        'NAME': 'FreddyFazbear Entrance',
        'DESCRIPTION': 'Your at the entrance of the new place where your going to work. The place is called '
                       'FreddyFazbear pizzaera',
        'PATHS': {
            'EAST': 'SECURITY PUPPET ROOM',
            'NORTH': 'WAITING ROOM'
         }
    },
    'SECURITY PUPPET ROOM': {
        'NAME': 'Security Puppet Room',
        'DESCRIPTION': 'This room will protect children who are trying to leave without their parent.',
        'PATHS': {
            'WEST': 'ENTRANCE'
        }
    },
    'WAITING ROOM': {
        'NAME': 'Waiting Room',
        'DESCRIPTION': 'This place is were people will wait until they could get a bracelet.',
        'PATHS': {
            'NORTH': 'DINNING ROOM',
            'WEST': 'BATHROOM',
            'EAST': 'OFFICE ROOM',
            'SOUTH': 'ENTRANCE'
        }
    },
    'OFFICE ROOM': {
        'NAME': 'Office Room',
        'DESCRIPTION': 'This place is were the manger will work. maybe',
        'PATHS': {
            'WEST': 'WAITING ROOM',
            'EAST': 'DATA BASE'
        }
    },
    'BATHROOM': {
        'NAME': 'Bathroom',
        'DESCRIPTION': "You know why you're here.",
        'PATHS': {
            'EAST': 'WAITING ROOM',
            'DOWN': 'BELOW BUILDING'
        }
    },

    'DINNING ROOM': {
        'NAME': 'Dinning Room',
        'DESCRIPTION': 'Here were your going to eat after or before you go into the buffet.',
        'PATHS': {
            'NORTH': 'STAGE',
            'WEST': 'GAME ROOM',
            'EAST': 'FOOD ROOM',
            'SOUTH': 'WAITING ROOM'
        }
    },
    'GAME ROOM': {
        'NAME': 'Game Room',
        'DESCRIPTION': 'This place is were your children going to play games.',
        'PATHS': {
            'WEST': 'FOXY ROOM',
            'EAST': 'DINNING ROOM'
        }
    },
    'FOXY ROOM': {
        'NAME': 'Foxy Room',
        'DESCRIPTION': 'Foxy is the most lovable character',
        'PATHS': {
            'EAST': 'GAME ROOM'
        }
    },
    'FOOD ROOM': {
        'NAME': 'Food Room',
        'DESCRIPTION': 'Do you not known why we use this place.',
        'PATHS': {
            'WEST': 'DINNING ROOM'
        }
    },
    'STAGE': {
        'NAME': 'Stage',
        'DESCRIPTION': 'This is were the animatronic is going to perform',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING',
            'WEST': 'STORAGE ROOM',
            'SOUTH': 'DINNING ROOM'
        }
    },
    'STORAGE ROOM': {
        'NAME': 'Storage Room',
        'DESCRIPTION': 'This is were we keep extras stuff. Like a dead bo- dead battery.',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING ',
            'EAST': 'STAGE'
        }
    },
    'BACK OF THE BUILDING': {
        'NAME': 'Back of the building',
        'DESCRIPTION': 'There nothing here but blo- balloons',
        'PATHS': {
            'NORTH': 'SECURITY ROOM',
            'WEST': 'STORAGE ROOM',
            'EAST': 'STAFF ROOM',
            'SOUTH': 'STORAGE ROOM'
        }
    },
    'SECURITY ROOM': {
        'NAME': 'Security Room',
        'DESCRIPTION': 'This is were your going to work',
        'PATHS': {
            'SOUTH': 'BACK OF THE BUILDING'
        }
    },
    'STAFF ROOM': {
        'NAME': 'Staff Room',
        'DESCRIPTION': 'Other staff will take a break in here',
        'PATHS': {
            'NORTH': 'BACK OF THE BUILDING',
            'EAST': 'ANIMATRONICS'
        }
    },
    'ANIMATRONICS': {
        'NAME': 'Animatronics room',
        'DESCRIPTION': "There are 4 animatronics that are a work in progress.",
        'PATHS': {
            'WEST': 'STAFF ROOM',
            'SOUTH': 'DATA BASE'
        }
    },
    'DATA BASE': {
        'NAME': 'Data base',
        'DESCRIPTION': 'This is were we controlled the animatronics',
        'PATHS': {
            'NORTH': 'ANIMATRONICS ROOM',
            'SOUTH': 'OFFICE'
        }
    },
    'BELOW BUILDING': {
        'NAME': 'Below building',
        'DESCRIPTION': 'You fell and found a strange place',
        'PATHS': {
            'UP': 'BATHROOM',
            'EAST': 'ELEVATOR'
        }
    },
    'ELEVATOR': {
        'NAME': 'Elevator',
        'DESCRIPTION': 'It seem the elevator take you below or up. Would you like to go up or down?',
        'PATHS': {
            'NORTH': 'CONTROL ROOM',
            'WEST': 'BELOW BUILDING',
            'EAST': 'NOTHING',
            'up': 'BATHROOM',
            'down': 'CONTROL PANEL'
        }
    },
    'NOTHING': {
        'NAME': 'Nothing',
        'DESCRIPTION': 'There nothing here but rocks.',
        'PATHS': {
            'WEST': 'ELEVATOR'
        }
    },
    'CONTROL PANEL': {
        'NAME': 'Control panel',
        'DESCRIPTION': 'There seem to be a button that does something.',
        'PATHS': {
            'NORTH': 'CONTROL PANEL 2',
            'EAST': 'BALLORA AUDITORIUM',
            'SOUTH': 'ELEVATOR'
        }
    },
    'BALLORA AUDITORIUM': {
        'NAME': 'Ballora Auditorium',
        'DESCRIPTION': "'There seem to be something there but can't make out what it is.",
        'PATHS': {
            'NORTH': 'FUNTIME AUDITORIUM',
            'WEST': 'CONTROL PANEL'
        }
    },
    'FUNTIME AUDITORIUM': {
        'NAME': 'Fun time Auditorium',
        'DESCRIPTION': "There also something there but can't make out what it is",
        'PATHS': {
            'WEST': 'FOXY AUDITORIUM',
            'SOUTH': 'BALLORA AUDITORIUM'
        }
    },
    'FOXY AUDITORIUM': {
        'NAME': 'Foxy Auditorium',
        'DESCRIPTION': 'You hear something but was to fainted to figure out',
        'PATHS': {
            'EAST': 'FUNTIME AUDITORIUM'
        }
    },
    'CONTROL PANEL 2': {
        'NAME': 'Control Panel for Baby',
        'DESCRIPTION': 'There are a lot of button that does something. but what?',
        'PATHS': {
            'SOUTH': 'CONTROL PANEL',
            'NORTH': 'BABY AUDITORIUM'
        }
    },
    'BABY AUDITORIUM': {
        'NAME': 'Baby Auditorium',
        'DESCRIPTION': 'you find something very odd, familiar, but    there something     very     disturbing. ',
        'PATHS': {
            'SOUTH': 'CONTROL PANEL 2'
        }
    },
}

current_node = Five_Night_Freddy['ENTRANCE']
direction = ['NORTH', 'SOUTH', 'EAST', 'WEST']
other_direction = ['UP', 'DOWN']
while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command == 'quit':
        quit(0)

    if command in direction and other_direction:
        try:
            name_of_node = current_node['PATHS'][command]
            print(name_of_node)
            current_node = Five_Night_Freddy[name_of_node]
        except KeyError:
            print("Are you a baka, there is nothing there")
    else:
        print("Command unknown, are you a baka")
