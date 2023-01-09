#!/usr/bin/env python3

"""Sarina Lyons | sarina.lyons@tlgcohort.com
   Dice Cheats - CHALLENGE"""


class CheatingDicePlayer(DicePlayer):
    def __init__(self, name, cheat_type):
        super().__init__(name)
        self.cheat_type = cheat_type
    
    def cheat(self):
        if self.cheat_type == "mulligan":
            return self.roll() if sum(self.roll()) < 9 else self.cheat()
        elif self.cheat_type == "extra_die":
            return self.roll() + [random.randint(1, 6)]
        elif self.cheat_type == "weighted_dice":
            return [max(3, random.randint(1, 6))] + self.roll()[1:]
        elif self.cheat_type == "sabotage":
            return [random.randint(1, 3)] * len(self.roll())
        else:
            return self.roll()


