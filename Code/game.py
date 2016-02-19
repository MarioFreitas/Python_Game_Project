#  Import functions
from random import random

# Import Custom Functions
from c_functions import *

# Import Enemies
from enemies import *


# Define Character
class Character(object):
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
        return "Nome: %s\nVida: %.1f\nStamina: %.1f\n" % (self.name, self.hp, self.stamina)

    def status_repr(self):
        if self.status == []:
            return "Status: None"
        else:
            return "Status: " + str(self.status)

    def long_repr(self):
        return "Nome: %s\nHP: %.1f / %1.f\nStamina: %.1f / %1.f\nAtaque: %.1f / %1.f\nDefesa: %.1f / %1.f\nVelocidade: \
        %.1f / %1.f\nAgilidade: %.1f / %1.f\nResistencia a Fogo: %.1f / %1.f\nResistencia a Gelo: %.1f / \
        %1.f\nResistencia a Trovao: %.1f / %1.f"\
               % (self.name, self.hp, self.hp_max, self.stamina, self.stamina_max, self.attack_total, self.attack_orig,
                  self.defense_total, self.defense_orig, self.speed_total, self.speed_orig, self.agility_Total,
                  self.agility_orig, self.fire_res, self.fire_res_orig, self.ice_res, self.ice_res_orig,
                  self.thunder_res, self.thunder_res_orig)


# Define Equipment
class Equipment(object):
    def __init__(self, name, kind, attack, bleed, fire, ice, thunder, defense, speed, agility, description):
        self.name = name
        self.kind = kind
        self.attack = attack
        self.bleed = bleed
        self.fire = fire
        self.ice = ice
        self.thunder = thunder
        self.defense = defense
        self.speed = speed
        self.agility = agility
        self.description = description

    def __repr__(self):
        return "Nome: %s\nDescricao: %s" % (self.name, self.description)

    def long_repr(self):
        e_r_name = "Nome: %s\n" % self.name
        e_r_kind = "Tipo: %s\n" % self.kind
        e_r_attack = "Ataque: %.0f\n" % self.attack
        e_r_bleed = "Sangramento: %.2f\n" % self.bleed
        e_r_fire = "Fogo: %.2f\n" % self.fire
        e_r_ice = "Gelo: %.2f\n" % self.ice
        e_r_thunder = "Trovao: %.2f\n" % self.thunder
        e_r_defense = "Defesa: %.2f\n" % self.defense
        e_r_speed = "Velocidade: %.2f\n" % self.speed
        e_r_agility = "Agilidade: %.2f\n" % self.agility
        e_r_description = "Descricao: %s\n" % self.description

        e_r_string = e_r_name + e_r_kind + e_r_attack + e_r_bleed + e_r_fire + e_r_ice + e_r_thunder + e_r_defense
        e_r_string = e_r_string + e_r_speed + e_r_agility + e_r_description
        return e_r_string


# Define Atacks
class Atacks(object):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def __repr__(self):
        return "Nome: %s\nPoder: %.1f\n" % (self.name, self.power)


# Initialize Equipments
# equipment = Equipment(name, kind, attack, bleed, fire, ice, thunder, defense, speed, agility, description)
dumb_equip = Equipment("Nada", "", 0, 0, 0, 0, 0, 0, 0, 0, "")
wooden_sword = Equipment("Wooden Sword", "Mao Direita", 10, 0, 0, 0, 0, 5, 0, 0, "Espada de madeira.")

# Initialize Hero
# hero = Character(name, hp, stamina, attack, defense, speed, agility, fire_res, ice_res, thunder_res)
hero = Character("Warrick Southwood", 100, 100, 10, 5, 10, 10, 0, 0, 0)  # Warrick > 'Town Warrior'
hero.lvl = 1
hero.exp = 0
hero.head = dumb_equip
hero.torso = dumb_equip
hero.left_hand = dumb_equip
hero.right_hand = dumb_equip
hero.feet = dumb_equip
hero.attack_total = hero.attack_orig = hero.attack + hero.head.attack + hero.torso.attack + hero.left_hand.attack + \
                                       hero.right_hand.attack + hero.feet.attack
hero.defense_total = hero.defense_orig = hero.defense + hero.head.defense + hero.torso.defense + hero.left_hand.defense\
                                         + hero.right_hand.defense + hero.feet.defense
hero.speed_total = hero.speed_orig = hero.speed + hero.head.speed + hero.torso.speed + hero.left_hand.speed + \
                                     hero.right_hand.speed + hero.feet.speed
hero.agility_Total = hero.agility_orig = hero.agility + hero.head.agility + hero.torso.agility + hero.left_hand.agility\
                                         + hero.right_hand.agility + hero.feet.agility


def battle_reset():
    hero.attack_total = hero.attack_orig
    hero.defense_total = hero.defense_orig
    hero.speed_total = hero.speed_orig
    hero.agility_Total = hero.agility_orig


def equip_reset():
    hero.attack_total = hero.attack_orig = hero.attack + hero.head.attack + hero.torso.attack + hero.left_hand.attack +\
                                           hero.right_hand.attack + hero.feet.attack
    hero.defense_total = hero.defense_orig = hero.defense + hero.head.defense + hero.torso.defense +\
                                             hero.left_hand.defense + hero.right_hand.defense + hero.feet.defense
    hero.speed_total = hero.speed_orig = hero.speed + hero.head.speed + hero.torso.speed + hero.left_hand.speed +\
                                         hero.right_hand.speed + hero.feet.speed
    hero.agility_Total = hero.agility_orig = hero.agility + hero.head.agility + hero.torso.agility +\
                                             hero.left_hand.agility + hero.right_hand.agility + hero.feet.agility


def lvl_reset():
    hero.hp = 100 * (1 + (hero.lvl - 1) * 0.05)
    hero.stamina = 100 * (1 + (hero.lvl - 1) * 0.05)
    hero.attack = 10 * (1 + (hero.lvl - 1) * 0.05)
    hero.defense = 5 * (1 + (hero.lvl - 1) * 0.05)
    hero.speed = 10 * (1 + (hero.lvl - 1) * 0.05)
    hero.agility = 10 * (1 + (hero.lvl - 1) * 0.05)


# Initialize Monsters
# monster = Character(name, hp, stamina, attack, defense, speed, agility, fire_res, ice_res, thunder_res)
# wolf = Character("Lobo lvl 1", 140, 80, 30, 10, 0, 10, 0, 0, 0)
# print wolf

# Define Battle
def battle1(enemy):
    ver = True
    while ver:
        # Print Battle Info
        print hero
        print enemy
        print

        # Player Choice
        h_choice = c_input("O que voce quer fazer?\nAtacar <1>, Magia <2>, Item <3>, Defender <4>, Esquivar <5>,\
Descansar <6> ou Fugir <7>? ", ['1', '2', '3', '4', '5', '6', '7'])

        # Monster Choice
        m_choice = enemy.choice()
        print "m_choice = %s" % m_choice

        # RNG Values
        h_atk = hero.attack_total * (1 + random() * 0.1)
        h_def = hero.defense_total * (1 + random() * 0.1)
        m_atk = enemy.attack * (1 + random() * 0.1)
        m_def = enemy.defense * (1 + random() * 0.1)
        if (hero.speed * (1 + random() * 0.1)) >= (enemy.speed * (1 + random() * 0.1)):  # Player goes first
            # Player Turn
            if h_choice == '1' and (m_choice != '4' and m_choice != '5'):
                enemy.hp -= h_atk
                print 'Voce causou %.1f de dano.' % h_atk
                hero.stamina -= 30
                pause(2.4)
            elif h_choice == '1' and m_choice == '4':
                if h_atk <= m_def:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.2, enemy.stamina_max)
                    print 'O inimigo se defendeu. \nO inimigo recuperou stamina. \nVoce nao causou dano algum.'
                    hero.stamina -= 30
                    pause(2.4)
                else:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.05, enemy.stamina_max)
                    enemy.hp -= (h_atk - m_def)
                    print 'O inimigo se defendeu. \nO inimigo recuperou um pouco de stamina. \nVoce causou %.1f de \
                    dano.' % (h_atk - m_def)
                    hero.stamina -= 30
                    pause(2.4)
            elif h_choice == '1' and m_choice == '5':
                if random() > (hero.agility / enemy.agility) * 0.5:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.5, enemy.stamina_max)
                    print 'O inimigo se esquivou. \nO inimigo recuperou bastante stamina.'
                    hero.stamina -= 30
                    pause(2.4)
                else:
                    enemy.hp -= h_atk
                    print 'O inimigo tentou se esquivar e falhou. \nVoce causou %.1f de dano.' % h_atk
                    hero.stamina -= 30
                    pause(2.4)
            elif h_choice == '3':
                hero.hp = min(hero.hp + hero.hp_max * 0.75, hero.hp_max)
                print 'Voce usou uma pocao e recuperou muito hp.'
                pause(2.4)
            elif h_choice == '6':
                hero.stamina = min(hero.stamina + hero.stamina_max * 0.5, hero.stamina_max)
                print 'Voce descancou e recuperou bastante stamina.'
                pause(2.4)
            elif h_choice == '7':
                if random() > (enemy.agility / hero.agility) * 0.8:
                    print 'Voce conseguiu fugir da batalha'
                    break
                else:
                    print 'Voce tentou fugir e nao conseguiu.'

            # Battle Win Check
            if enemy.hp <= 0:
                print 'Voce venceu a batalha!'
                battle_reset()
                break

            # Enemy Turn
            if m_choice == '1' and (h_choice != '4' and h_choice != '5'):
                hero.hp -= m_atk
                print 'Voce levou %.1f de dano.' % m_atk
                enemy.stamina -= 30
                pause(2.4)
            elif m_choice == '1' and h_choice == '4':
                if m_atk <= h_def:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.2, hero.stamina_max)
                    print 'Voce se defendeu. \nVoce recuperou stamina. \nO inimigo nao causou dano algum.'
                    enemy.stamina -= 30
                    pause(2.4)
                else:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.05, hero.stamina_max)
                    hero.hp -= (m_atk - h_def)
                    print 'Voce se defendeu. \nVoce recuperou um pouco de stamina. \nVoce levou %.1f de dano.' % (
                        m_atk - h_def)
                    enemy.stamina -= 30
                    pause(2.4)
            elif m_choice == '1' and h_choice == '5':
                if random() > (enemy.agility / hero.agility) * 0.5:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.5, hero.stamina_max)
                    print 'Voce se esquivou. \nVoce recuperou bastante stamina.'
                    enemy.stamina -= 30
                    pause(2.4)
                else:
                    hero.hp -= m_atk
                    print 'Voce tentou se esquivar e falhou. \nVoce levou %.1f de dano.' % m_atk
                    enemy.stamina -= 30
                    pause(2.4)
            elif m_choice == '3':
                enemy.hp = min(enemy.hp + enemy.hp_max * 0.75, enemy.hp_max)
                print 'O inimigo usou uma pocao e recuperou muito hp.'
                pause(2.4)
            elif m_choice == '6':
                enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.5, enemy.stamina_max)
                print 'O inimigo descancou e recuperou bastante stamina.'
                pause(2.4)
            elif m_choice == '7':
                if random() > (hero.agility / enemy.agility) * 0.8:
                    print 'O inimigo conseguiu fugir da batalha'
                    break
                else:
                    print 'O inimigo tentou fugir e nao conseguiu.'

            # Battle Loss Check
            if hero.hp <= 0:
                print 'Voce perdeu a batalha!'
                battle_reset()
                break

        else:  # Enemy goes first
            # Enemy Turn
            if m_choice == '1' and (h_choice != '4' and h_choice != '5'):
                hero.hp -= m_atk
                print 'Voce levou %.1f de dano.' % m_atk
                enemy.stamina -= 30
                pause(2.4)
            elif m_choice == '1' and h_choice == '4':
                if m_atk <= h_def:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.2, hero.stamina_max)
                    print 'Voce se defendeu. \nVoce recuperou stamina. \nO inimigo nao causou dano algum.'
                    enemy.stamina -= 30
                    pause(2.4)
                else:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.05, hero.stamina_max)
                    hero.hp -= (m_atk - h_def)
                    print 'Voce se defendeu. \nVoce recuperou um pouco de stamina. \nVoce levou %.1f de dano.' % (
                        m_atk - h_def)
                    enemy.stamina -= 30
                    pause(2.4)
            elif m_choice == '1' and h_choice == '5':
                if random() > (enemy.agility / hero.agility) * 0.5:
                    hero.stamina = min(hero.stamina + hero.stamina_max * 0.5, hero.stamina_max)
                    print 'Voce se esquivou. \nVoce recuperou bastante stamina.'
                    enemy.stamina -= 30
                    pause(2.4)
                else:
                    hero.hp -= m_atk
                    print 'Voce tentou se esquivar e falhou. \nVoce levou %.1f de dano.' % m_atk
                    enemy.stamina -= 30
                    pause(2.4)
            elif m_choice == '3':
                enemy.hp = min(enemy.hp + enemy.hp_max * 0.75, enemy.hp_max)
                print 'O inimigo usou uma pocao e recuperou muito hp.'
                pause(2.4)
            elif m_choice == '6':
                enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.5, enemy.stamina_max)
                print 'O inimigo descancou e recuperou bastante stamina.'
                pause(2.4)
            elif m_choice == '7':
                if random() > (hero.agility / enemy.agility) * 0.8:
                    print 'O inimigo conseguiu fugir da batalha'
                    break
                else:
                    print 'O inimigo tentou fugir e nao conseguiu.'

            # Battle Loss Check
            if hero.hp <= 0:
                print 'Voce perdeu a batalha!'
                battle_reset()
                break

            # Player Turn
            if h_choice == '1' and (m_choice != '4' and m_choice != '5'):
                enemy.hp -= h_atk
                print 'Voce causou %.1f de dano.' % h_atk
                hero.stamina -= 30
                pause(2.4)
            elif h_choice == '1' and m_choice == '4':
                if h_atk <= m_def:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.2, enemy.stamina_max)
                    print 'O inimigo se defendeu. \nO inimigo recuperou stamina. \nVoce nao causou dano algum.'
                    hero.stamina -= 30
                    pause(2.4)
                else:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.05, enemy.stamina_max)
                    enemy.hp -= (h_atk - m_def)
                    print 'O inimigo se defendeu. \nO inimigo recuperou um pouco de stamina. \nVoce causou %.1f de \
                    dano.' % (h_atk - m_def)
                    hero.stamina -= 30
                    pause(2.4)
            elif h_choice == '1' and m_choice == '5':
                if random() > (hero.agility / enemy.agility) * 0.5:
                    enemy.stamina = min(enemy.stamina + enemy.stamina_max * 0.5, enemy.stamina_max)
                    print 'O inimigo se esquivou. \nO inimigo recuperou bastante stamina.'
                    hero.stamina -= 30
                    pause(2.4)
                else:
                    enemy.hp -= h_atk
                    print 'O inimigo tentou se esquivar e falhou. \nVoce causou %.1f de dano.' % h_atk
                    hero.stamina -= 30
                    pause(2.4)
            elif h_choice == '3':
                hero.hp = min(hero.hp + hero.hp_max * 0.75, hero.hp_max)
                print 'Voce usou uma pocao e recuperou muito hp.'
                pause(2.4)
            elif h_choice == '6':
                hero.stamina = min(hero.stamina + hero.stamina_max * 0.5, hero.stamina_max)
                print 'Voce descancou e recuperou bastante stamina.'
                pause(2.4)
            elif h_choice == '7':
                if random() > (enemy.agility / hero.agility) * 0.8:
                    print 'Voce conseguiu fugir da batalha'
                    break
                else:
                    print 'Voce tentou fugir e nao conseguiu.'

            # Battle Win Check
            if enemy.hp <= 0:
                print 'Voce venceu a batalha!'
                battle_reset()
                break

        clc()


clc()
hero.right_hand = wooden_sword
equip_reset()
battle1(wolf)

raw_input("Aperte <Enter> para sair")
