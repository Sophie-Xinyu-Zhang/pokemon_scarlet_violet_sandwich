class TypePower:
    def __init__(self, name, type_power_dict):
        self.name = name
        if len(type_power_dict.keys()) == 0:
            self.Normal = 0
            self.Fighting = 0
            self.Flying = 0
            self.Poison = 0
            self.Ground = 0
            self.Rock = 0
            self.Bug = 0
            self.Ghost = 0
            self.Steel = 0
            self.Fire = 0
            self.Water = 0
            self.Grass = 0
            self.Electric = 0
            self.Psychic = 0
            self.Ice = 0
            self.Dragon = 0
            self.Dark = 0
            self.Fairy = 0
        else:
            self.Normal = type_power_dict['Normal']
            self.Fighting = type_power_dict['Fighting']
            self.Flying = type_power_dict['Flying']
            self.Poison = type_power_dict['Poison']
            self.Ground = type_power_dict['Ground']
            self.Rock = type_power_dict['Rock']
            self.Bug = type_power_dict['Bug']
            self.Ghost = type_power_dict['Ghost']
            self.Steel = type_power_dict['Steel']
            self.Fire = type_power_dict['Fire']
            self.Water = type_power_dict['Water']
            self.Grass = type_power_dict['Grass']
            self.Electric = type_power_dict['Electric']
            self.Psychic = type_power_dict['Psychic']
            self.Ice = type_power_dict['Ice']
            self.Dragon = type_power_dict['Dragon']
            self.Dark = type_power_dict['Dark']
            self.Fairy = type_power_dict['Fairy']
    
    def __add__(self, other):
        return TypePower(name = f"{self.name} + {other.name}", type_power_dict = {
            'Normal': self.Normal + other.Normal,
            'Fighting': self.Fighting + other.Fighting,
            'Flying': self.Flying + other.Flying,
            'Poison': self.Poison + other.Poison,
            'Ground': self.Ground + other.Ground,
            'Rock': self.Rock + other.Rock,
            'Bug': self.Bug + other.Bug,
            'Ghost': self.Ghost + other.Ghost,
            'Steel': self.Steel + other.Steel,
            'Fire': self.Fire + other.Fire,
            'Water': self.Water + other.Water,
            'Grass': self.Grass + other.Grass,
            'Electric': self.Electric + other.Electric,
            'Psychic': self.Psychic + other.Psychic,
            'Ice': self.Ice + other.Ice,
            'Dragon': self.Dragon + other.Dragon,
            'Dark': self.Dark + other.Dark,
            'Fairy': self.Fairy + other.Fairy
        })

    def __repr__(self):
        return f"Normal: {self.Normal}\nFighting: {self.Fighting}\nFlying: {self.Flying}\nPoison: {self.Poison}\nGround: {self.Ground}\nRock: {self.Rock}\nBug: {self.Bug}\nGhost: {self.Ghost}\nSteel: {self.Steel}\nFire: {self.Fire}\nWater: {self.Water}\nGrass: {self.Grass}\nElectric: {self.Electric}\nPsychic: {self.Psychic}\nIce: {self.Ice}\nDragon: {self.Dragon}\nDark: {self.Dark}\nFairy: {self.Fairy}"







