class Survivor:
    def __init__(self, name: str):
        self.name = name
        self.wounds = 0
        self.alive = True
        self.action = 3
        self.equipment = []  # in_hand_equip, reserve_equip
        # self.equipment_examples = ["Baseball bat", "Frying pan", "Katana", "Pistol", "Bottled Water", "Molotov"]

    def is_dead(self):
        if self.wounds < 2:
            return self.alive
        else:
            return not self.alive

    def add_equipment(self, item):
        if len(self.equipment) >= 5:
            raise AssertionError("Survivor cannot carry more than 5 items of equipment")
        self.equipment.append(item)

    def equipment_location(self):
        in_hand_equip = self.equipment[:2]
        reserve_equip = self.equipment[2:]
        return in_hand_equip, reserve_equip
    
    def equipment_capacity_loss(self):
        if self.wounds >= 1:
            return len(self.equipment) - self.wounds
        else:
            return len(self.equipment)
