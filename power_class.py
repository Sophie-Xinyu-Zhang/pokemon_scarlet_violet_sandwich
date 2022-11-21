

class Power:
    def __init__(self, name, power_dict):
        if power_dict is None:
            power_dict = {}
        self.name = name
        if len(power_dict.keys()) == 0:
            self.egg = 0
            self.catching = 0
            self.exp_power = 0
            self.item_drop = 0
            self.raid = 0
            self.title = 0
            self.sparkling = 0
            self.humongo = 0
            self.teensy = 0
            self.encounter = 0
        else:
            self.egg = power_dict['Egg Power']
            self.catching = power_dict['Catching Power']
            self.exp_power = power_dict['Exp. Power']
            self.item_drop = power_dict['Item Drop Power']
            self.raid = power_dict['Raid Power']
            self.title = power_dict['Title Power']
            self.sparkling = power_dict['Sparkling Power']
            self.humongo = power_dict['Humongo Power']
            self.teensy = power_dict['Teensy Power']
            self.encounter = power_dict['Encounter Power']

    def __add__(self, other):
        power_dict = {
            'Egg Power': self.egg + other.egg,
            'Catching Power': self.catching + other.catching,
            'Exp. Power': self.exp_power + other.exp_power,
            'Item Drop Power': self.item_drop + other.item_drop,
            'Raid Power': self.raid + other.raid,
            'Title Power': self.title + other.title,
            'Sparkling Power': self.sparkling + other.sparkling,
            'Humongo Power': self.humongo + other.humongo,
            'Teensy Power': self.teensy + other.teensy,
            'Encounter Power': self.encounter + other.encounter
        }

        return Power(name = f"{self.name} + {other.name}", power_dict = power_dict)
    
    def __repr__(self):
        return f"Egg Power: {self.egg}\nCatching Power: {self.catching}\nExp. Power: {self.exp_power}\nItem Drop Power: {self.item_drop}\nRaid Power: {self.raid}\nTitle Power: {self.title}\nSparkling Power: {self.sparkling}\nHumongo Power: {self.humongo}\nTeensy Power: {self.teensy}\nEncounter Power: {self.encounter}"
