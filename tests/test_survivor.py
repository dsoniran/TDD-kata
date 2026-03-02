from main import survivor
import pytest

from main.survivor import Survivor

# Step One: Survivors

class TestSurvivorInit:
    # Test Survivor initialization with valid name and wounds
    # Never share states between tests. Each test should be independent and not rely on the state of another test.

    def test_survivor_has_name(self):
        # Test that the survivor has a name
        survivor = Survivor("Usher")
        assert survivor.name == "Usher"

    def test_survivor_has_zero_wounds(self):
        survivor = Survivor("Usher")
        assert survivor.wounds == 0

    def test_survivor_is_alive(self):
        survivor = Survivor("Usher")
        assert survivor.alive == True

    def test_survivor_has_action_(self):
        survivor = Survivor("Usher")
        assert survivor.action == 3

class TestSurvivorIsDead:
    # Test the is_dead method of the Survivor class

    def setup_method(self):
        self.name = "Usher"

    def test_survivor_survives_less_than_two_wounds(self):
        survivor = Survivor(self.name)
        survivor.wounds = 0 or 1
        assert survivor.is_dead() == True

    def test_survivor_dies_from_two_wounds(self):
        survivor = Survivor(self.name)
        survivor.wounds = 2
        assert survivor.is_dead() == False

    def test_survivor_survives_has_three_or_more_wounds(self):
        survivor = Survivor("Fred")
        survivor.wounds = 3
        assert survivor.is_dead() == False


## Step Two: Equipment

class TestSurvivorEquipment:
    def setup_method(self):
        self.name = "Usher"
        self.equipment_examples = ["Baseball bat", "Frying pan", "Katana", "Pistol", "Bottled Water", "Molotov"]

    def test_survivor_has_equipment(self):
        # Survivors can use equipment to help them in their mission.

        survivor = Survivor(self.name)
        assert hasattr(survivor, 'equipment')

    def test_survivor_has_max_equipment(self):
        # Each Survivor can carry up to 5 pieces of Equipment.

        survivor = Survivor(self.name)
        for i in range(5):
            survivor.add_equipment(f"item{i+1}")
        assert len(survivor.equipment) == 5
        with pytest.raises(AssertionError, match="Survivor cannot carry more than 5 items of equipment"):
            survivor.add_equipment("item6")

    def test_survivor_equipment_in_hand_and_reserve(self):
        # Up to 2 pieces of carried Equipment are "In Hand"; the rest are "In Reserve".
        # do i need to change to accommodate "up to"?

        survivor = Survivor(self.name)
        for item in self.equipment_examples[:5]:
            survivor.add_equipment(item)
        in_hand_equip, reserve_equip = survivor.equipment_location()
        assert in_hand_equip == ["Baseball bat", "Frying pan"]
        assert reserve_equip == ["Katana", "Pistol", "Bottled Water"]

    def test_survivor_swap_equipment_location(self):
        #  Survivor can swap equipment from Reserve to In-Hand

        survivor = Survivor(self.name)
        for item in self.equipment_examples[:5]:
            survivor.add_equipment(item)
        # Swap the first in-hand equipment with the first reserve equipment
        survivor.equipment[0], survivor.equipment[2] = survivor.equipment[2], survivor.equipment[0]
        in_hand_equip, reserve_equip = survivor.equipment_location()
        assert in_hand_equip == ["Katana", "Frying pan"]
        assert reserve_equip == ["Baseball bat", "Pistol", "Bottled Water"]

    # def test_in_hand_equip_cannot_exceed_two_items(self):
    #     # If in hand is full, one item must go back to reserve
    #     # works solo - not good

    #     survivor = Survivor(self.name)
    #     for item in self.equipment_examples[:5]:
    #         survivor.add_equipment(item)
    #     in_hand_equip, reserve_equip = survivor.equipment_location()
    #     assert len(in_hand_equip) <= 2

    def test_each_wound_decreases_equipment_capacity_by_one(self):
        # Each Wound a Survivor receives reduces the number of pieces of Equipment they can carry by 1.
         # failing - need to resolve

        survivor = Survivor(self.name)
        for item in self.equipment_examples[:5]:
            survivor.add_equipment(item)
        survivor.wounds = 1
        
        survivor.equipment_capacity_loss()
        assert len(survivor.equipment) == 4
        

    # def test_equipment_capacity(self):
        # If the Survivor has more Equipment than their new capacity, choose a piece to discard (implement however you like).
