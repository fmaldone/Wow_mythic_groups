

class myth_player:
    def __init__(self, player, *characters):
        self.name = player
        self.list_of_chars = characters

    def __str__(self):
        return self.name + " has the following characters: " + str(self.list_of_chars)

class wow_char:
    def __init__(self,name, char=dict):
        self.char_name = name
        self.key_level = char["level"]
        self.dungeon = char["dungeon"]
    
    def __str__(self):
        return ("\nCharacter name: " + self.char_name + "\nKey Level: " + str(self.key_level)
                + "\nDungeon: " + self.dungeon + "\n")

players_list = []
toon_list = []

keystone_dict = {"Jmartz": {"Calioma" : {"level": 7, "dungeon": "freehold"},
                            "Solemartz": {"level": 3, "dungeon": "Vortex Pinnacle"}},
                "Cardinal": {"Fluke" : {"level": 14, "dungeon": "Underrot"},
                             "Gael" : {"level": 10, "dungeon": "Brackenhide"}}}

for key, value in keystone_dict.items():
    toon_list_player = list(keystone_dict[key].keys())
    locals()[key] = myth_player(key, *toon_list_player)
    players_list.append(locals()[key])

for i in keystone_dict:
    char_list = list(keystone_dict[i].keys())
    for num in char_list:
        toon = wow_char(num, keystone_dict[i][num])
        toon_list.append(toon)

for i in range(len(players_list)):
    print(players_list[i])

for i in range(len(toon_list)):
    print(toon_list[i])

