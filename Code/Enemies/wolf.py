from random import random


# Define Enemy
class Enemy(object):
    def __init__(self, name, hp, stamina, attack, defense, speed, agility, fire_res, ice_res, thunder_res):
        self.name = name
        self.hp = self.hp_max = hp
        self.stamina = self.stamina_max = stamina
        self.attack = self.attack_orig = attack
        self.defense = self.defense_orig = defense
        self.speed = self.speed_orig = speed
        self.agility = self.agility_orig = agility
        self.fire_res = self.fire_res_orig = fire_res
        self.ice_res = self.ice_res_orig = ice_res
        self.thunder_res = self.thunder_res_orig = thunder_res
        self.status = []
        self.attack_total = 0
        self.defense_total = 0
        self.speed_total = 0
        self.agility_Total = 0

    def __repr__(self):
        return "Nome: %s\nVida: %.1f\nstamina: %.1f\n" % (self.name, self.hp, self.stamina)

    def status_repr(self):
        if self.status == []:
            return "Status: None"
        else:
            return "Status: " + str(self.status)

    def long_repr(self):
        return "Nome: %s\nhp: %.1f / %1.f\nstamina: %.1f / %1.f\nAtaque: %.1f / %1.f\nDefesa: %.1f / %1.f\nVelocidade: \
        %.1f / %1.f\nAgilidade: %.1f / %1.f\nResistencia a Fogo: %.1f / %1.f\nResistencia a Gelo: %.1f / \
        %1.f\nResistencia a Trovao: %.1f / %1.f" \
               % (self.name, self.hp, self.hp_max, self.stamina, self.stamina_max, self.attack_total, self.attack_orig,
                  self.defense_total, self.defense_orig, self.speed_total, self.speed_orig, self.agility_Total,
                  self.agility_orig, self.fire_res, self.fire_res_orig, self.ice_res, self.ice_res_orig,
                  self.thunder_res, self.thunder_res_orig)

    def choice(self):
        m_choice = random()
        if self.hp > 0.5 * self.hp_max:
            if self.stamina > 0.75 * self.stamina_max:
                if m_choice < 0.8:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.5 * self.stamina_max:
                if m_choice < 0.65:
                    m_choice = 1
                elif m_choice < 0.90:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.25 * self.stamina_max:
                if m_choice < 0.5:
                    m_choice = 1
                elif m_choice < 0.80:
                    m_choice = 4
                elif m_choice < 0.90:
                    m_choice = 5
                else:
                    m_choice = 6
            else:
                if m_choice < 0.10:
                    m_choice = 1
                elif m_choice < 0.25:
                    m_choice = 4
                elif m_choice < 0.50:
                    m_choice = 5
                else:
                    m_choice = 6
        elif self.hp > 0.20 * self.hp_max:
            if self.stamina > 0.75 * self.stamina_max:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.90:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.5 * self.stamina_max:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.80:
                    m_choice = 1
                elif m_choice < 0.90:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.25 * self.stamina_max:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.65:
                    m_choice = 1
                elif m_choice < 0.85:
                    m_choice = 4
                else:
                    m_choice = 5
            else:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.35:
                    m_choice = 1
                elif m_choice < 0.85:
                    m_choice = 4
                else:
                    m_choice = 5
        else:
            if self.stamina > 0.75 * self.stamina_max:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.90:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.5 * self.stamina_max:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.85:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif self.stamina > 0.25 * self.stamina_max:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.80:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            else:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.77:
                    m_choice = 1
                elif m_choice < 0.90:
                    m_choice = 4
                else:
                    m_choice = 5
        print m_choice
        return str(m_choice)


def choice_meaning(choice):
    if choice == '1':
        print 'Atacar'
    elif choice == '2':
        print 'Magia'
    elif choice == '3':
        print 'Item'
    elif choice == '4':
        print 'Defender'
    elif choice == '5':
        print 'Esquivar'
    elif choice == '6':
        print 'Descansar'
    elif choice == '7':
        print 'Fugir'


# Initialize Monsters
# monster = Character(Name, hp, stamina, attack, defense, speed, agility, fire_res, ice_res, thunder_res)

wolf = Enemy("Lobo LVL 1", 140, 80, 30, 10, 0, 10, 0, 0, 0)

"""
print wolf
wolf.hp -= 10
wolf.stamina -= 70
print wolf
n = wolf.choice()
choice_meaning(n)
"""
