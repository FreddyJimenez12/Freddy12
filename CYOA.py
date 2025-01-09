import random

inventory = []
invCapacity = 4
body = []
hand = []
used_item = []
direction = ['north', 'south', 'east', 'west', 'up', 'down']
short_direction = ['n', 's', 'e', 'w', 'u', 'd']
dead_body = []
open_door = []


class Item(object):
    def __init__(self, name, description, room):
        self.name = name
        self.description = description
        self.from_room = room
        self.isTaken = False

    def take(self):
        if bag_of_holding in inventory:
            inventory.append(self)
            used_item.append(self)
            self.isTaken = True
            print("You took the item")
        else:
            if len(inventory) == 4:
                print("You are holding too much stuff")
            else:
                inventory.append(self)
                used_item.append(self)
                self.isTaken = True
                print("You took the item")

    def drop(self):
        inventory.remove(self)
        self.isTaken = False
        print("You drop the item")

##


class Weapon(Item):
    def __init__(self, name, description, damage_ratio, room, magazine):
        super(Weapon, self).__init__(name, description, room)
        self.damage = damage_ratio
        self.magazine = magazine


##


class Consumable(Item):
    def __init__(self, name, description, room):
        super(Consumable, self).__init__(name, description, room)
        self.eaten = False


# Fix this


class Wearable(Item):
    def __init__(self, name, description, room, ):
        super(Wearable, self).__init__(name, description, room)
        self.Worn = False

    # method for wear

    # def wear(self):
    #     for Wearable.item in inventory:
    #         if Wearable.item in inventory:
    #             print("Would you want to wear the %s" % item.name)
    #         if Wearable.item not in inventory:
    #             print("there nothing you could wear")
    #         else:
    #             print("Would you want to wear the %s" % item.name)
    #         if command == "wear %s" % item.name:
    #             print("you wear the item")
    #             self.Worn = True


class Range(Weapon):
    def __init__(self, name, description, room, damage_ratio, magazine):
        super(Range, self).__init__(name, description, damage_ratio, room, magazine)
        self.magazine = magazine


class Arcade_machine(Item):
    def __init__(self, name, description, room, action, ):
        super(Arcade_machine, self).__init__(name, description, room)
        self.action = action

    def wear(self):
        print("you wear the arcade machine and you turn into one. You became Arcade man")


class Melee(Weapon):
    def __init__(self, name, description, room, damage_ratio):
        super(Melee, self).__init__(name, description, damage_ratio, room, None)


class Crowbar(Melee):
    def __init__(self, name, description, room, damage_ratio):
        super(Crowbar, self).__init__(name, description, room, damage_ratio)
        self.OpenHatch = False

    def cr_attack(self):
        if crowbar in command:
            print(crowbar.damage)


class Knife(Melee):
    def __init__(self, name, description, room, damage_ratio):
        super(Knife, self).__init__(name, description, room, damage_ratio)


class Flare_gun(Range):
    def __init__(self, name, description, room, damage_ratio, magazine):
        super(Flare_gun, self).__init__(name, description, room, damage_ratio, magazine)

    def signal(self):
        print("You shot at the sky to get signal your position. You're save")


class Flare_ammo(Item):
    def __init__(self, name, description, room, ammo):
        super(Flare_ammo, self).__init__(name, description, room)
        self.ammo = ammo


class Ball_pit(Item):
    def __init__(self, name, description, room):
        super(Ball_pit, self).__init__(name, description, room)


class Flashlight(Item):
    def __init__(self, name, description, room):
        super(Flashlight, self).__init__(name, description, room)

    def turn_on(self):
        print("You turn on the flashlight")

    def turn_off(self):
        print("You turn off your flashlight")


class Battery(Item):
    def __init__(self, name, description, room):
        super(Battery, self).__init__(name, description, room)

    def reload(self):
        print("you use the battery to charge your flashlight")


class Mic(Item):
    def __init__(self, name, description, room):
        super(Mic, self).__init__(name, description, room)


class Cupcake_fake(Item):
    def __init__(self, name, description, room):
        super(Cupcake_fake, self).__init__(name, description, room)


class Guitar(Item):
    def __init__(self, name, description, room):
        super(Guitar, self).__init__(name, description, room)


class Bag_of_holding(Wearable):
    def __init__(self, name, description, room):
        super(Bag_of_holding, self).__init__(name, description, room)

    def wear(self):
        print("your able to hold unlimited thing for the cost of your life bw careful.")


class Pizza(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Pizza, self).__init__(name, description, room)

    def eat(self):
        print("You ate the pizza")
        self.eaten = True


class Cupcake(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Cupcake, self).__init__(name, description, room)

    def eat(self):
        print("You ate the cupcake, nothing happen what did you expected")
        self.eaten = True


class Water_bottle(Consumable):
    def __init__(self, name, description, room):
        self.eaten = False
        super(Water_bottle, self).__init__(name, description, room)

    def eat(self):
        print("You drink a water bottle, nothing happen")
        self.eaten = True


class Hat(Wearable):
    def __init__(self, name, description, room):
        super(Hat, self).__init__(name, description, room)

    def wear(self):
        print("You wore the hat you think your special, but your not, your going to die.")


class Cape(Wearable):
    def __init__(self, name, description, room):
        super(Cape, self).__init__(name, description, room)

    def wear(self):
        print("You feel invincible, but you hit you head on the roof and past out")
        print("You woke up second later.")


class Bloody_shirt(Item):
    def __init__(self, name, description, room):
        super(Bloody_shirt, self).__init__(name, description, room)

    def wear(self):
        print("you wear the bloody shirt, now you started to smell very weird")


class Telephone(Item):
    def __init__(self, name, description, room):
        super(Telephone, self).__init__(name, description, room)


class Hook(Melee):
    def __init__(self, name, description, damage_ratio):
        super(Hook, self).__init__(name, description, None, damage_ratio)


class Medkits(Item):
    def __init__(self, name, description, health_recover):
        super(Medkits, self).__init__(name, description, None)
        self.health_recover = health_recover


####


class Character(object):
    def __init__(self, name, description, inventory, stats, items, action, jump_scare, location=None):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.items = items
        self.action = action
        self.jump_scare = jump_scare
        self.location = location

    def move(self, directions):
        self.location.character.remove(self)
        try:
            self.location = globals()[getattr(self.location, directions)]
        except KeyError:
            pass
        self.location.character.append(self)


class Player(Character):
    def __init__(self, name, description, inventory, stats, items, action, jump_scare, location=None):
        super(Player, self).__init__(name, description, inventory, stats, items, action, jump_scare, location)

    def move(self, directions):
        try:
            self.location = globals()[getattr(self.location, directions)]
            print(person1.location.name)
            print(person1.location.description)

        except KeyError:
            print("Are you a baka, there is nothing there")


person1 = Player('Henry',
                 "you took this job because you needed money. Your wife and three kids just wanted to have a better "
                 "life."
                 "you found this job on ebay? what, What wrong with you ",
                 'Flashlight', 100, None, None, None)
Bonnie = Character('Bonnie',
                   "Bonnie is a fun bunny which bring joy around the pizzeria. But then again it smell like a dead bod-"
                   "something",
                   None, 50, 'guitar',
                   'play the guitar', "you become blind and paralyzed")
Freddy = Character('Freddy Fazbear',
                   "Freddy is the most lovable bear in the whole pizzeria. He liked the star of the band. But every"
                   "time he sing it sound like a dead man crying, trying to get out. but who knows.",
                   None,  50, 'Mic', 'Sing', "you become blind and paralyzed")
Chica = Character('Chica', "Chica is a duck like Animatronics who soul purpose is to give out cupcake. but we don't "
                           "know what inside of those cupcake maybe bloo-. its made organic.)",
                  None, 50, 'Cupcake', "give out cupcakes", "you become blind and paralyzed.")
Foxy = Character('Foxy', "Foxy is in the back stage most of the time because he's shy. His fur is always red but it"
                         " used to be white. We think that an employee colored it red. But it started to smell.",
                 None, 50, "a Hook", None, "you become blind and paralyzed.")
Ballora = Character('Ballora', "She a fun charter, like to sing, dance, and to put on a show",
                    None, 50, None, "dance", "you become blind and paralyzed.")
Fun_time_Freddy = Character("Fun time Freddy",
                            "He's a lovable character which was used in the last pizzeria but run out"
                            "business because of a weird smell and a disappearance of children.",
                            None,  50, None, "play with children", "you become blind and paralyzed.")
Fun_time_Foxy = Character("Fun Time Foxy", "She's the sister of Foxy but have a few improvement over Foxy. But we "
                          "saw something very strange in the old security camera of a child disappearing and Fun time "
                          "Foxy came out.", None, 50, None, "Dance",
                          "you become blind and paralyzed.")
Baby = Character("Baby",
                 "Baby was made to take care and make kids happy. But they started to disappear when they go "
                 "and play with Baby.", None, 50, None,
                 "dance and sing", "you become blind and paralyzed.")
Puppet = Character("Puppet", "she going to protect all the children from harm, and from you", None, 50, None,
                   "roams around", None)


####


class Room(object):
    def __init__(self, name, description, north, west, east, south, up, down, items=None):
        if items is None:
            items = []
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.items = items
        self.character = []


####
person1 = person1
bonnie = Bonnie
freddy = Freddy
chica = Chica
foxy = Foxy
ballora = Ballora
fun_time_freddy = Fun_time_Freddy
fun_time_foxy = Fun_time_Foxy
baby = Baby
puppet = Puppet

list_of_chars = [bonnie, freddy, chica, foxy, ballora, fun_time_freddy, fun_time_foxy, baby, puppet]


def move_chars():
    for char in list_of_chars:
        rand_direction = random.choice(direction)
        try:
            char.move(rand_direction)
        except ValueError:
            print(char.name)
            print(char.location.name)
            print(char.location.character)
            print(rand_direction)
            quit(2)


arcade_machine = Arcade_machine("arcade machine", "This machine is out of order", None, "explode")

crowbar = Crowbar("crowbar", "You can use this to fight off thing, or open a hatch", None, 25)

knife = Knife("knife", "You use the knife to fight of thing or cook. tee-hee", None, 25)

flare_gun = Flare_gun("flare gun", "You can signal for help or light the way up.", None, '15', 4)

flare_ammo = Flare_ammo("flare ammo", "You can use this to reload your flare gun, There nothing else you can do with it"
                                      ".", None, 4)

ball_pit = Ball_pit("ball pit", " Kids love this ball pit, but for some reason kids are going missing.", None)

flashlight = Flashlight("flashlight", "The flashlight is use to light of the wae. It runs out real fast though", None)

battery = Battery("battery", "It a battery what else can you use it for", None)

mic = Mic("mic", "Property of Freddy", None)

cupcake_fake = Cupcake_fake("the plastic cupcake", "This is one of the missing cupcake of Chica collection."
                            "If you give it to her then you get a prized of dea-, of good things.",
                            None)

guitar = Guitar("guitar", "This guitar have something on it like blo- red paint.", None)


bag_of_holding = Bag_of_holding("bag of holding", "You could hold endless amount of item but at a cost of 10 health.",
                                None)

pizza = Pizza("pizza", "this pizza is made from the top chief in the garbage. *Don't eat it*", None)

cupcake = Cupcake("cupcake", "This is a very treat from the most lovable character in the pizzeria death", None)

water_bottle = Water_bottle("water bottle", "This is the most freshest water bottle you will every see in the world."
                                            "It's from our very own toilet. ", None)
hat = Hat("hat", "This hat said to belong to a child who have gone missing for a month. There even a name. *Run*", None)

cape = Cape("cape", "This 'cape' said to give you magical power but there just blood.", None)

bloody_shirt = Bloody_shirt("bloody shirt", "Who knows where this shirt came from.", None)

telephone = Telephone("telephone", "This telephone is my only way to escape. There seem to be a battery missing.", None)

hook = Hook("hook", "The hook was made from the dead bodies of children, what.", 25)

medkit = Medkits("medkit", "You use the medkit to refill all of your health bar", 20)


food_list = [cupcake, water_bottle, pizza, ]
weapon_list = [knife, crowbar, hook]
wear_list = [bloody_shirt, hat, cape, bag_of_holding, arcade_machine]
ammo = [flare_ammo, battery]

ENTRANCE = Room('Freddy Fazbear Entrance',
                'Your at the entrance of the new place where your going to work. The place is called '
                'Freddy Fazbear pizzeria',
                'WAITING_ROOM', None, 'SECURITY_PUPPET_ROOM', None, None, None, None)

SECURITY_PUPPET_ROOM = Room('security puppet room',
                            'This room will protect children who are trying to leave without their parent.',
                            None, 'ENTRANCE', None, None, None, None, [flashlight])
WAITING_ROOM = Room('Waiting Room',
                    'This place is where people will wait until they could get a bracelet to enter the playhouse.'
                    'the door closes behind you and its locked, find the key',
                    'DINNING_ROOM', 'BATHROOM', 'OFFICE_ROOM', 'ENTRANCE', None, None, [water_bottle])
OFFICE_ROOM = Room('Office Room',
                   'This place is were the manger is going work. maybe',
                   None, 'WAITING_ROOM', 'DATA_BASE', None, None, None, [knife])
BATHROOM = Room('Bathroom',
                "You know why you're here. There seem to be a open hatch in one of the stalls. would you like to go "
                "down?",
                None, None, 'WAITING_ROOM', None, None, 'BELOW_BUILDING', [flare_gun])
DINNING_ROOM = Room('Dinning Room',
                    'Here were your going to eat after or before you go into the buffet.',
                    'STAGE', 'GAME_ROOM', 'FOOD_ROOM', 'WAITING_ROOM', None, None, [pizza, cupcake])
GAME_ROOM = Room('Game Room',
                 'This place is were your children going to play games.',
                 None, 'FOXY_ROOM', 'DINNING_ROOM', None, None, None, [arcade_machine])
FOXY_ROOM = Room('Foxy Room',
                 'Foxy is the most lovable character.',
                 None, None, 'GAME_ROOM', None, None, None, [medkit])
FOOD_ROOM = Room('Food Room',
                 'Do you not known why we use this place.',
                 None, 'DINNING_ROOM', None, None, None, None, [water_bottle, cupcake_fake])
STAGE = Room('Stage',
             'This is were the animatronics is going to perform. We have Freddy, Bonnie, and chica. there a hat on the '
             'ground',
             'BACK_OF_THE_BUILDING', 'STORAGE_ROOM', None, 'DINNING_ROOM', None, None, [hat])
STORAGE_ROOM = Room('Storage Room',
                    'This is were we keep extras stuff. Like a dead bo- dead battery.',
                    'BACK_OF_THE_BUILDING', None, None, 'DINNING_ROOM', None, None, [crowbar])
CORNER = Room('The corner', 'Your at the corner of the building there nothing here', None, None, 'BACK_OF_THE_BUILDING',
              'STORAGE_ROOM', None, None, None)
BACK_OF_THE_BUILDING = Room('Back of the building',
                            'There nothing here but blo- balloons.',
                            'SECURITY_ROOM', 'CORNER', 'STAFF_ROOM', 'STAGE', None, None,
                            [bloody_shirt])
SECURITY_ROOM = Room('Security Room',
                     'This is were your going to work.',
                     None, None, None, 'BACK_OF_THE_BUILDING', None, None, [flashlight])
STAFF_ROOM = Room('Staff Room',
                  'Other staff will take a break in here.',
                  'BACK_OF_THE_BUILDING', None, 'ANIMATRONICS', None, None, None, [flare_ammo])
ANIMATRONICS = Room('Animatronics room',
                    "There are 4 animatronics that are a work in progress.",
                    None, 'STAFF_ROOM', None, 'DATA_BASE', None, None, [mic, battery])
DATA_BASE = Room('Data base',
                 'This is were we controlled the animatronics.',
                 'ANIMATRONICS', 'OFFICE', None, None, None, None, [hook])
BELOW_BUILDING = Room('Below building',
                      'You fell and found a strange place. its dark.',
                      None, None, 'ELEVATOR', None, 'BATHROOM', None, [flare_ammo, medkit])
ELEVATOR = Room('Elevator',
                'It seem the elevator take you below or up. Would you like to go up or down?',
                'CONTROL_ROOM', 'BELOW_BUILDING', 'NOTHING', None, 'BATHROOM', 'CONTROL_PANEL', None)
NOTHING = Room('Nothing',
               'There nothing here but rocks.',
               None, 'ELEVATOR', None, None, None, None, [bag_of_holding])
CONTROL_PANEL = Room('Control panel',
                     'There seem to be a button that does something.',
                     'CONTROL_PANEL_2', None, 'BALLORA_AUDITORIUM', 'ELEVATOR', None, None, [cape])
BALLORA_AUDITORIUM = Room('Ballora Auditorium',
                          "'There seem to be something there but can't make out what it is.",
                          'FUN_TIME_AUDITORIUM', 'CONTROL_PANEL', None, None, None, None, None)
FUN_TIME_AUDITORIUM = Room('Fun time Auditorium',
                           "There also something there but can't make out what it is",
                           None, 'FOXY_AUDITORIUM', None, 'BALLORA_AUDITORIUM', None, None, [guitar])
FOXY_AUDITORIUM = Room('Foxy Auditorium',
                       'You hear something but was to fainted to figure out.',
                       None, None, 'FUN_TIME_AUDITORIUM', None, None, None, None)
CONTROL_PANEL_2 = Room('Control Panel for Baby',
                       'There are a lot of button that does something. but what?',
                       None, None, None, 'CONTROL_PANEL', None, None, None)
BABY_AUDITORIUM = Room('Baby Auditorium',
                       'you find something very odd, familiar, but    there something     very     disturbing.',
                       None, None, None, 'CONTROL_PANEL_2', None, None, [telephone])

person1.location = ENTRANCE

list_of_rooms = [ELEVATOR, ENTRANCE, WAITING_ROOM, OFFICE_ROOM, ANIMATRONICS, SECURITY_PUPPET_ROOM, SECURITY_ROOM,
                 STAFF_ROOM, STAGE, STORAGE_ROOM, DATA_BASE, DINNING_ROOM, FOOD_ROOM, GAME_ROOM, FOXY_AUDITORIUM,
                 FOXY_ROOM, BATHROOM, BABY_AUDITORIUM, BALLORA_AUDITORIUM, BACK_OF_THE_BUILDING, BELOW_BUILDING,
                 CONTROL_PANEL_2, FUN_TIME_AUDITORIUM, CONTROL_PANEL, NOTHING]


def place_chars():
    for char in list_of_chars:
        room = random.choice(list_of_rooms)
        char.location = room
        room.character.append(char)


ii = isinstance
print("Your health is at the bottom")
print(person1.description)
print(person1.location.name)
print(person1.location.description)
place_chars()

while True:
    print("Health: %s" % person1.stats)

    random_number2 = random.randint(1, 2)
    random_number = random.randint(1, 3)
    random_number3 = (0, 2)

    for character in list_of_chars:
        if character.location != person1.location:
            pass
        else:
            print("you have come across with %s" % character.name)
            print("Health: %s" % character.stats)

    for character in list_of_chars:
        if random_number == 2:
            if character.location != person1.location:
                pass
            else:
                #
                print("it seem you have made %s angry" % character.name)
                print("%s" % character.name, "attack you")
                print("it dealt 20 damage")
                person1.stats -= 20

    # if person1.location.character is not None:
    #     for character in person1.location.character:
    #         print(character.name)

    for item in person1.location.items:
        if item is not False:
            if item not in inventory:
                if item.name in used_item:
                    pass
                else:
                    if item not in used_item:
                        print("There seem to be a %s" % item.name)

    command = input(':').lower().strip()
    if command == 'quit':
        quit(0)
    if command in short_direction:
        pos = short_direction.index(command)
        command = direction[pos]
    if command in direction:
        person1.move(command.lower())

    elif "turn on" in command:
        for item in person1.location.items:
            if item.name in command:
                item.turn_on()
                break

    elif "turn off" in command:
        for item in person1.location.items:
            if item.name in command:
                item.turn_off()
                break

    elif "take" in command:
        for item in person1.location.items:
            if item.name in command:
                item.take()
                break
            else:
                print("You can't take that.")
                break

    elif "drop" in command:
        if not inventory:
            print("There nothing in your inventory")
        else:
            for item in inventory:
                if item.name.lower() in command:
                    item.drop()
                else:
                    if item not in inventory:
                        print("what are you saying there nothing inside your inventory.")

                    # fix the drink, and eat
    elif "eat" in command:
        for food in inventory:
            if food.name.lower() in command:
                if issubclass(type(food), Consumable):
                    food.eat()
                    inventory.remove(food)
                    used_item.append(food)

                else:
                    print("You can't eat that.")
    elif "drink" in command:
        for food in inventory:
            if food.name.lower() in command:
                if issubclass(type(food), Consumable):
                    food.eat()
                    inventory.remove(food)
                    used_item.append(food)

                else:
                    print("You can't drink that.")

    elif "look at" in command:
        for item in inventory:
            if item.name in command:
                print(item.name)
                print(item.description)

    elif "wear" in command:
        for item in person1.location.items:
            wear_list = item
            if wear_list not in inventory:
                print("They're nothing to wear")
                item.isTaken = False
            for items in person1.location.items:
                if wear_list.name != items.name in command:
                    print("you can't wear that")
                else:
                    if wear_list.name.lower() in command:
                        print("You wear the item.")
                        if issubclass(type(wear_list), Wearable):
                            wear_list.wear()
                            inventory.remove(wear_list)
                            body.append(wear_list)
                        if arcade_machine.name in command:
                            arcade_machine.wear()
    #
    elif "attack" in command:
        for items in inventory:
            for character in person1.location.character:
                if random_number == 2:
                    print("You attack with %s" % items.name, "at %s" % character.name)
                    print("You able to hit %s" % character.name)
                    print("you deal %s" % items.damage)
                    character.stats -= items.damage
                else:
                    print("you missed")

    elif "equip" in command:
        for item in inventory:
            if str.lower(item.name) in command and item.isTaken:
                kn = Knife
                cr = Crowbar
                k = Hook

                if ii(item, kn) or ii(item, cr) or ii(item, k):
                    if hand is not None:
                        hand = None
                    else:
                        hand = item.name
                    print("You equipped the %s" % str.lower(item.name))

    # not sure if this needed
    # elif "unequipped" in command:
    #     for item in inventory:
    #         if str.lower(item.name) in command:
    #             kn = Knife
    #             cr = Crowbar
    #             k = Hook
    #
    #             if ii(item, kn) or ii(item, cr) or ii(item, k):
    #                 hand = None
    #             else:
    #                 print("You unequip the %s" % str.lower(item.name))

    elif command == "pick up all":
        for item in person1.location.items:
            inventory.append(item)
            item.isTaken = True
            print("You took everything")
    elif command == "win game":
        print("You won the game")
        break
    elif command == "look up":
        print("Type in win game")
    elif command == "inventory":
        for item in inventory:
            print(item.name)

    elif command == "heal":
        if medkit.name not in inventory:
            pass
        else:
            print("there nothing you could heal with")
        if person1.stats == 100:
            print("you're already at full hp")
        if person1.stats != 100:
            person1.stats += medkit.health_recover
            print("You heal yourself.")
            inventory.remove(medkit)
            used_item.append(medkit)
            if medkit.name in used_item:
                pass
    elif command == "shoot":
        if flare_gun not in inventory:
            print("you can't fire anything")
        for characters in person1.location.character:
            if random_number == 2:
                print("You're able to land a hit.")
                print("You hit %s" % characters.name)
                print("You dealt %s" % flare_gun.damage)
                characters.stats -= 15
                flare_gun.magazine -= 1
                print(characters.stats)
            else:
                print("you missed the shot.")
                flare_gun.magazine -= 1

            if flare_gun.magazine == 0:
                print("you ran out of ammo")

    elif command == "thanos":
        print("You snap you finger and all the animatronics had died.")
        print("you escape like nothing happen and started to have the feeling to destroy the universe")
        quit(0)

    elif command == "reload":
        for ammo in ammo:
            if flare_ammo not in inventory:
                print("You don't have ammo, go find some")
            if flare_gun.magazine == 0:
                print("You reloaded")
                flare_gun.magazine += flare_ammo.ammo
    elif command == "body":
        for item in body:
            print(item.name)
    elif "run" in command:
        if random_number == 2:
            print("You weren't able to escape")
            print("The animatronics were able to capture you and turn you into one of them.")
            print("You later barley escape, but war enable to move.")
            print("You couldn't escape and now you never escape.")

            quit(0)
        else:
            if random_number == 1 or 3:
                print("You successfully got away ")

    elif freddy.stats == 0:
        print("you killed Freddy Fazbear")
        print("How could you, just kidding")
        list_of_chars.remove(freddy)
        dead_body.append(freddy)
    elif bonnie.stats == 0:
        print("you killed Bonnie the most lovable character of all")
        print("lovable my ass she must dieeeeee")
        list_of_chars.remove(bonnie)
        dead_body.append(bonnie)
    elif chica.stats == 0:
        print("You killed me how dd d dd ddd  dddare you ")
        print("I cannot end thissssssssss")
        print("*dead*")
        list_of_chars.remove(chica)
        dead_body.append(chica)
        for item in chica.inventory:
            inventory.remove(item)
            print("There seem to be a key that drop from Chica")
    elif foxy.stats == 0:
        print("you killed foxy.")
        print("I'll come back for you u u u uuuu u u  uu u u u")
        print("You feel uneasy")
        list_of_chars.remove(foxy)
        dead_body.append(foxy)
    elif ballora.stats == 0:
        print("I will survivvveeee eevevev eeve e")
        list_of_chars.remove(ballora)
        dead_body.append(ballora)
    elif fun_time_freddy.stats == 0:
        print("bhaaaaaaaaaaa  aaaaa aaaaa ")
        print("you think this is the end ")
        print("just you wait and seeeee e i- *dead*")
        list_of_chars.remove(fun_time_freddy)
        dead_body.append(fun_time_freddy)
    elif fun_time_foxy.stats == 0:
        print("i wiilll find youuuu")
        print("AND I WILL KILL YOU! BHAAAAAAAAAAAA A AAA A AA A  *dead*")
        list_of_chars.remove(fun_time_foxy)
        dead_body.append(fun_time_foxy)
    elif baby.stats == 0:
        print("i thought you loved me *sob*")
        print("but your time is coming up as well")
        list_of_chars.remove(baby)
        dead_body.append(baby)
    elif puppet.stats == 0:
        print("why do I still live. just to suffer")
        print("omae wa mou shindeiru")
        print("*translate*", "you're already dead")

    elif command == "look":
        print(person1.location.name)
        print(person1.location.description)
    elif person1.stats == 0:
        print("you died")
        quit(0)
    else:
        print("Command unknown, are you a baka")
    move_chars()
