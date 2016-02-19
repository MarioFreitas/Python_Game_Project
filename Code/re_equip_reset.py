class Equipment(object):
    def __init__(self, attack, defense, dodge):
        self.attack = attack
        self.defense = defense
        self.dodge = dodge


class Stats(object):
    def __init__(self, head, torso, left_hand, right_hand, foot):
        self.head = head
        self.torso = torso
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.foot = foot
        self.total = self.head + self.torso + self.left_hand + self.right_hand + self.foot

    def reset(self):
        self.total = self.head + self.torso + self.left_hand + self.right_hand + self.foot


capacete = Equipment(0,10,0)
armadura = Equipment(0,30,0)
escudo = Equipment(0,50,0)
espada = Equipment(30,10,0)
bota_leve = Equipment(0,10,50)

defense = Stats(capacete.defense,armadura.defense,escudo.defense,espada.defense,bota_leve.defense)
print defense.total
defense.head = 50
defense.reset()
print defense.total
