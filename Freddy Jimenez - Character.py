class Character(object):
    def __init__(self, name, description, inventory, stats, items, action, jump_scare):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.stats = stats
        self.items = items
        self.action = action
        self.jump_scare = jump_scare

    # def person(self, name):
    #     print("Your name is %s" % name)
    #
    # def profile(self):
    #    print("you took this job because you needed money. Your wife and three kids just wanted to have a better life."
    #           "you found this job on ebay? what. What wrong with you ")
    #
    # def thing(self):
    #     print("you only got a flashlight")


person1 = Character('Henry',
                    "you took this job because you needed money. Your wife and three kids just wanted to have a better "
                    "life."
                    "you found this job on ebay? what, What wrong with you ",
                    'Flashlight',
                    ' H = 100',
                    None, None, None)
Bonnie = Character('Bonnie',
                   "Bonnie is a fun bunny which bring joy around the pizzeria. But then again it smell like a dead bod-"
                   "something",
                   None, ' H = 100', 'guitar',
                   'play the guitar', "you become blind and paralyzed")
Freddy = Character('Freddy Fazbear',
                   "Freddy is the most lovable bear in the whole pizzeria. He liked the star of the band. But every"
                   "time he sing it sound like a dead man crying, trying to get out. but who knows.",
                   None, 'H = 100', 'Mic', 'Sing', "you become blind and paralyzed")
Chica = Character('Chica', "Chica is a duck like animatronics who soul purpose is to give out cupcake. but we don't "
                  "know what inside of those cupcake maybe bloo-. its made organic.;)",
                  None, 'H = 100', 'Cupcake', "give out cupcakes", "you become blind and paralyzed.")
Foxy = Character('Foxy', "Foxy is in the back stage most of the time because he's shy. His fur is always red but it"
                         " used to be white. We think that an employee colored it red. But it started to smell.",
                 None, 'H = 100', "a Hook", None, "you become blind and paralyzed.")
Ballora = Character('Ballora', "She a fun charter, like to sing, dance, and to put on a show",
                    None, "H = 100", None, "dance", "you become blind and paralyzed.")
Fun_time_Freddy = Character("Fun time Freddy", "He's a lovable character which was used in the last pizzeria but "
                            " run out"
                            "business because of a weird smell and a disappearance of children.",
                            None, "H = 100", None, "play with children", "you become blind and paralyzed.")
Fun_time_Foxy = Character("Fun Time Foxy", "She's the sister of Foxy but have a few improvement over Foxy. But we "
                          "saw something very strange in the old security camera of a child disappearing and Fun time "
                          "Foxy came out.", None, "H = 100", None, "Dance", "you become blind and paralyzed.")
Baby = Character("Baby", "Baby was made to take care and make kids happy. But they started to disappear when they go "
                         "and play with Baby.", None, "H = 100", None,
                 "dance and sing", "you become blind and paralyzed.")
baby = Baby

print(Freddy.description)
# print(person1.description)
# print(Foxy.items,)
# print(Chica.description)
# command = input(":")
