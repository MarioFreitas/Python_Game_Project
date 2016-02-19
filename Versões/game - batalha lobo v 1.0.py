from random import random
from random import randint
import os
from time import sleep


# Clean Interpreeter Function
def clc():
    os.system('cls')
    # print '\n'*100


# Pause code
pause_option = True


def pause(seconds):
    if pause_option == True:
        sleep(seconds)


# Define Character
class Character(object):
    def __init__(self, Name, HP, Stamina, Attack, Defense, Speed, Agility, Fire_Res, Ice_Res, Lightining_Res):
        self.Name = Name
        self.HP = self.HP_Max = HP
        self.Stamina = self.Stamina_Max = Stamina
        self.Attack = self.Attack_Orig = Attack
        self.Defense = self.Defense_Orig = Defense
        self.Speed = self.Speed_Orig = Speed
        self.Agility = self.Agility_Orig = Agility
        self.Fire_Res = self.Fire_Res_Orig = Fire_Res
        self.Ice_Res = self.Ice_Res_Orig = Ice_Res
        self.Lightining_Res = self.Lightining_Res_Orig = Lightining_Res
        self.Status = []

    def __repr__(self):
        return "Nome: %s\nVida: %.1f\nStamina: %.1f\n" % (self.Name, self.HP, self.Stamina)

    def status_repr(self):
        if self.Status == []:
            return "Status: None"
        else:
            return "Status: " + str(self.Status)

    def long_repr(self):
        return "Nome: %s\nHP: %.1f / %1.f\nStamina: %.1f / %1.f\nAtaque: %.1f / %1.f\nDefesa: %.1f / %1.f\n\
Velocidade: %.1f / %1.f\nAgilidade: %.1f / %1.f\nResistencia a Fogo: %.1f / %1.f\nResistencia a gelo: %.1f / %1.f\nResistencia a Trovao: %.1f / %1.f\
" % (self.Name, self.HP, self.HP_Max, self.Stamina, self.Stamina_Max, self.Attack_Total, self.Attack_Orig,
     self.Defense_Total, self.Defense_Orig, self.Speed_Total, self.Speed_Orig, self.Agility_Total, self.Agility_Orig,
     self.Fire_Res, self.Fire_Res_Orig, self.Ice_Res, self.Ice_Res_Orig, self.Lightining_Res, self.Lightining_Res_Orig)


# Define Equipment
class Equipment(object):
    def __init__(self, Name, Type, Attack, Bleed, Fire, Ice, Lightining, Defense, Speed, Agility, Description):
        self.Name = Name
        self.Type = Type
        self.Attack = Attack
        self.Bleed = Bleed
        self.Fire = Fire
        self.Ice = Ice
        self.Lightining = Lightining
        self.Defense = Defense
        self.Speed = Speed
        self.Agility = Agility
        self.Description = Description

    def __repr__(self):
        return "Nome: %s\nDescricao: %s" % (self.Name, self.Description)

    def long_repr(self):
        return "Nome: %s\nTipo: %s\nAtaque: %.0f\nSangramento: %.2f\nFogo: %.2f\nGelo: %.2f\nTrovao: %.2f\n\
Defesa: %.2f\nVelocidade: %.2f\nAgilidade: %.2f\nDescricao: %s\n\
" % (self.Name, self.Type, self.Attack, self.Bleed, self.Fire, self.Ice, self.Lightining, self.Defense, self.Speed,
     self.Agility, self.Description)


# Define Atacks
class Atacks(object):
    def __init__(self, Name, Power):
        self.Name = Name
        self.Power = Power

    def __repr__(self):
        return "Nome: %s\nPoder: %.1f\n" % (self.Name, self.Power)


# Initialize Equipments
# equipment = Equipment(Name, Type, Attack, Bleed, Fire, Ice, Lightining, Defense, Speed, Agility, Description)
dumb_equip = Equipment("Nada", "", 0, 0, 0, 0, 0, 0, 0, 0, "")
wooden_sword = Equipment("Wooden Sword", "Mao Direita", 10, 0, 0, 0, 0, 5, 0, 0, "Espada de madeira.")

#  Initialize Hero
#  hero = Character(Name, HP, Stamina, Attack, Defense, Speed, Agility, Fire_Res, Ice_Res, Lightining_Res)
hero = Character("Warrick Southwood", 100, 100, 10, 5, 10, 10, 0, 0, 0)  # Warrick > 'Town Warrior'
hero.LVL = 1
hero.EXP = 0
hero.Head = dumb_equip
hero.Torso = dumb_equip
hero.Left_Hand = dumb_equip
hero.Right_Hand = dumb_equip
hero.Foot = dumb_equip
hero.Attack_Total = hero.Attack_Orig = hero.Attack + hero.Head.Attack + hero.Torso.Attack + hero.Left_Hand.Attack + hero.Right_Hand.Attack + hero.Foot.Attack
hero.Defense_Total = hero.Defense_Orig = hero.Defense + hero.Head.Defense + hero.Torso.Defense + hero.Left_Hand.Defense + hero.Right_Hand.Defense + hero.Foot.Defense
hero.Speed_Total = hero.Speed_Orig = hero.Speed + hero.Head.Speed + hero.Torso.Speed + hero.Left_Hand.Speed + hero.Right_Hand.Speed + hero.Foot.Speed
hero.Agility_Total = hero.Agility_Orig = hero.Agility + hero.Head.Agility + hero.Torso.Agility + hero.Left_Hand.Agility + hero.Right_Hand.Agility + hero.Foot.Agility


def battle_reset():
    hero.Attack_Total = hero.Attack_Orig
    hero.Defense_Total = hero.Defense_Orig
    hero.Speed_Total = hero.Speed_Orig
    hero.Agility_Total = hero.Agility_Orig


def equip_reset():
    hero.Attack_Total = hero.Attack_Orig = hero.Attack + hero.Head.Attack + hero.Torso.Attack + hero.Left_Hand.Attack + hero.Right_Hand.Attack + hero.Foot.Attack
    hero.Defense_Total = hero.Defense_Orig = hero.Defense + hero.Head.Defense + hero.Torso.Defense + hero.Left_Hand.Defense + hero.Right_Hand.Defense + hero.Foot.Defense
    hero.Speed_Total = hero.Speed_Orig = hero.Speed + hero.Head.Speed + hero.Torso.Speed + hero.Left_Hand.Speed + hero.Right_Hand.Speed + hero.Foot.Speed
    hero.Agility_Total = hero.Agility_Orig = hero.Agility + hero.Head.Agility + hero.Torso.Agility + hero.Left_Hand.Agility + hero.Right_Hand.Agility + hero.Foot.Agility


def LVL_reset():
    hero.HP = 100 * (1 + (hero.LVL - 1) * 0.05)
    hero.Stamina = 100 * (1 + (hero.LVL - 1) * 0.05)
    hero.Attack = 10 * (1 + (hero.LVL - 1) * 0.05)
    hero.Defense = 5 * (1 + (hero.LVL - 1) * 0.05)
    hero.Speed = 10 * (1 + (hero.LVL - 1) * 0.05)
    hero.Agility = 10 * (1 + (hero.LVL - 1) * 0.05)


# Initialize Monsters
# monster = Character(Name, HP, Stamina, Attack, Defense, Speed, Agility, Fire_Res, Ice_Res, Lightining_Res)
wolf = Character("Lobo LVL 1", 140, 80, 30, 10, 10, 10, 0, 0, 0)


def c_input(text, str_list):
    while True:
        inp = raw_input(text)
        if inp in str_list:
            return inp
            break


# Define Battle
def battle1(enemy):
    while True:
        # Print Battle Info
        print hero
        print enemy
        print

        # Player Choice
        h_choice = c_input("O que voce quer fazer?\nAtacar <1>, Magia <2>, Item <3>, Defender <4>, Esquivar <5>,\
Descansar <6> ou Fugir <7>? ", ['1', '2', '3', '4', '5', '6', '7'])

        # Monster Choice
        m_choice = random()
        if enemy.HP > 0.5 * enemy.HP_Max:
            if enemy.Stamina > 0.75 * enemy.Stamina_Max:
                if m_choice < 0.8:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.5 * enemy.Stamina_Max:
                if m_choice < 0.65:
                    m_choice = 1
                elif m_choice < 0.90:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.25 * enemy.Stamina_Max:
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
        elif enemy.HP > 0.20 * enemy.HP_Max:
            if enemy.Stamina > 0.75 * enemy.Stamina_Max:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.90:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.5 * enemy.Stamina_Max:
                if m_choice < 0.25:
                    m_choice = 3
                elif m_choice < 0.80:
                    m_choice = 1
                elif m_choice < 0.90:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.25 * enemy.Stamina_Max:
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
            if enemy.Stamina > 0.75 * enemy.Stamina_Max:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.90:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.5 * enemy.Stamina_Max:
                if m_choice < 0.75:
                    m_choice = 3
                elif m_choice < 0.85:
                    m_choice = 1
                elif m_choice < 0.95:
                    m_choice = 4
                else:
                    m_choice = 5
            elif enemy.Stamina > 0.25 * enemy.Stamina_Max:
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

        m_choice = str(m_choice)
        print "m_choice = %s" % m_choice
        h_atk = hero.Attack_Total * (1 + random() * 0.1)
        h_def = hero.Defense_Total * (1 + random() * 0.1)
        m_atk = enemy.Attack * (1 + random() * 0.1)
        m_def = enemy.Defense * (1 + random() * 0.1)
        if (hero.Speed * (1 + random() * 0.1)) >= (enemy.Speed * (1 + random() * 0.1)):  # Player goes first
            # Player Turn
            if h_choice == '1' and (m_choice != '4' and m_choice != '5'):
                enemy.HP -= h_atk
                print 'Voce causou %.1f de dano.' % h_atk
                hero.Stamina -= 30
                pause(2.2)
            elif h_choice == '1' and m_choice == '4':
                if h_atk <= m_def:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.2, enemy.Stamina_Max)
                    print 'O inimigo se defendeu. \nO inimigo recuperou stamina. \nVoce nao causou dano algum.'
                    hero.Stamina -= 30
                    pause(2.2)
                else:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.05, enemy.Stamina_Max)
                    enemy.HP -= (h_atk - m_def)
                    print 'O inimigo se defendeu. \nO inimigo recuperou um pouco de stamina. \nVoce causou %.1f de dano.' % (
                        h_atk - m_def)
                    hero.Stamina -= 30
                    pause(2.2)
            elif h_choice == '1' and m_choice == '5':
                if random() > (hero.Agility / enemy.Agility) * 0.5:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.5, enemy.Stamina_Max)
                    print 'O inimigo se esquivou. \nO inimigo recuperou bastante stamina.'
                    hero.Stamina -= 30
                    pause(2.2)
                else:
                    enemy.HP -= h_atk
                    print 'O inimigo tentou se esquivar e falhou. \nVoce causou %.1f de dano.' % h_atk
                    hero.Stamina -= 30
                    pause(2.2)
            elif h_choice == '3':
                hero.HP = min(hero.HP + hero.HP_Max * 0.75, hero.HP_Max)
                print 'Voce usou uma pocao e recuperou muito HP.'
                pause(2.2)
            elif h_choice == '6':
                hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.5, hero.Stamina_Max)
                print 'Voce descancou e recuperou bastante stamina.'
                pause(2.2)
            elif h_choice == '7':
                if random() > (enemy.Agility / hero.Agility) * 0.8:
                    print 'Voce conseguiu fugir da batalha'
                    break
                else:
                    print 'Voce tentou fugir e nao conseguiu.'

            # Battle Win Check
            if enemy.HP <= 0:
                print 'Voce venceu a batalha!'
                battle_reset()
                break

            # Enemy Turn
            if m_choice == '1' and (h_choice != '4' and h_choice != '5'):
                hero.HP -= m_atk
                print 'Voce levou %.1f de dano.' % m_atk
                enemy.Stamina -= 30
                pause(2.2)
            elif m_choice == '1' and h_choice == '4':
                if m_atk <= h_def:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.2, hero.Stamina_Max)
                    print 'Voce se defendeu. \nVoce recuperou stamina. \nO inimigo nao causou dano algum.'
                    enemy.Stamina -= 30
                    pause(2.2)
                else:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.05, hero.Stamina_Max)
                    hero.HP -= (m_atk - h_def)
                    print 'Voce se defendeu. \nVoce recuperou um pouco de stamina. \nVoce levou %.1f de dano.' % (
                        m_atk - h_def)
                    enemy.Stamina -= 30
                    pause(2.2)
            elif m_choice == '1' and h_choice == '5':
                if random() > (enemy.Agility / hero.Agility) * 0.5:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.5, hero.Stamina_Max)
                    print 'Voce se esquivou. \nVoce recuperou bastante stamina.'
                    enemy.Stamina -= 30
                    pause(2.2)
                else:
                    hero.HP -= m_atk
                    print 'Voce tentou se esquivar e falhou. \nVoce levou %.1f de dano.' % m_atk
                    enemy.Stamina -= 30
                    pause(2.2)
            elif m_choice == '3':
                enemy.HP = min(enemy.HP + enemy.HP_Max * 0.75, enemy.HP_Max)
                print 'O inimigo usou uma pocao e recuperou muito HP.'
                pause(2.2)
            elif m_choice == '6':
                enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.5, enemy.Stamina_Max)
                print 'O inimigo descancou e recuperou bastante stamina.'
                pause(2.2)
            elif m_choice == '7':
                if random() > (hero.Agility / enemy.Agility) * 0.8:
                    print 'O inimigo conseguiu fugir da batalha'
                    break
                else:
                    print 'O inimigo tentou fugir e nao conseguiu.'

            # Battle Loss Check
            if hero.HP <= 0:
                print 'Voce perdeu a batalha!'
                battle_reset()
                break

        else:  # Enemy goes first
            # Enemy Turn
            if m_choice == '1' and (h_choice != '4' and h_choice != '5'):
                hero.HP -= m_atk
                print 'Voce levou %.1f de dano.' % m_atk
                enemy.Stamina -= 30
                pause(2.2)
            elif m_choice == '1' and h_choice == '4':
                if m_atk <= h_def:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.2, hero.Stamina_Max)
                    print 'Voce se defendeu. \nVoce recuperou stamina. \nO inimigo nao causou dano algum.'
                    enemy.Stamina -= 30
                    pause(2.2)
                else:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.05, hero.Stamina_Max)
                    hero.HP -= (m_atk - h_def)
                    print 'Voce se defendeu. \nVoce recuperou um pouco de stamina. \nVoce levou %.1f de dano.' % (
                        m_atk - h_def)
                    enemy.Stamina -= 30
                    pause(2.2)
            elif m_choice == '1' and h_choice == '5':
                if random() > (enemy.Agility / hero.Agility) * 0.5:
                    hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.5, hero.Stamina_Max)
                    print 'Voce se esquivou. \nVoce recuperou bastante stamina.'
                    enemy.Stamina -= 30
                    pause(2.2)
                else:
                    hero.HP -= m_atk
                    print 'Voce tentou se esquivar e falhou. \nVoce levou %.1f de dano.' % m_atk
                    enemy.Stamina -= 30
                    pause(2.2)
            elif m_choice == '3':
                enemy.HP = min(enemy.HP + enemy.HP_Max * 0.75, enemy.HP_Max)
                print 'O inimigo usou uma pocao e recuperou muito HP.'
                pause(2.2)
            elif m_choice == '6':
                enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.5, enemy.Stamina_Max)
                print 'O inimigo descancou e recuperou bastante stamina.'
                pause(2.2)
            elif m_choice == '7':
                if random() > (hero.Agility / enemy.Agility) * 0.8:
                    print 'O inimigo conseguiu fugir da batalha'
                    break
                else:
                    print 'O inimigo tentou fugir e nao conseguiu.'

            # Battle Loss Check
            if hero.HP <= 0:
                print 'Voce perdeu a batalha!'
                battle_reset()
                break

            # Player Turn
            if h_choice == '1' and (m_choice != '4' and m_choice != '5'):
                enemy.HP -= h_atk
                print 'Voce causou %.1f de dano.' % h_atk
                hero.Stamina -= 30
                pause(2.2)
            elif h_choice == '1' and m_choice == '4':
                if h_atk <= m_def:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.2, enemy.Stamina_Max)
                    print 'O inimigo se defendeu. \nO inimigo recuperou stamina. \nVoce nao causou dano algum.'
                    hero.Stamina -= 30
                    pause(2.2)
                else:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.05, enemy.Stamina_Max)
                    enemy.HP -= (h_atk - m_def)
                    print 'O inimigo se defendeu. \nO inimigo recuperou um pouco de stamina. \nVoce causou %.1f de dano.' % (
                        h_atk - m_def)
                    hero.Stamina -= 30
                    pause(2.2)
            elif h_choice == '1' and m_choice == '5':
                if random() > (hero.Agility / enemy.Agility) * 0.5:
                    enemy.Stamina = min(enemy.Stamina + enemy.Stamina_Max * 0.5, enemy.Stamina_Max)
                    print 'O inimigo se esquivou. \nO inimigo recuperou bastante stamina.'
                    hero.Stamina -= 30
                    pause(2.2)
                else:
                    enemy.HP -= h_atk
                    print 'O inimigo tentou se esquivar e falhou. \nVoce causou %.1f de dano.' % h_atk
                    hero.Stamina -= 30
                    pause(2.2)
            elif h_choice == '3':
                hero.HP = min(hero.HP + hero.HP_Max * 0.75, hero.HP_Max)
                print 'Voce usou uma pocao e recuperou muito HP.'
                pause(2.2)
            elif h_choice == '6':
                hero.Stamina = min(hero.Stamina + hero.Stamina_Max * 0.5, hero.Stamina_Max)
                print 'Voce descancou e recuperou bastante stamina.'
                pause(2.2)
            elif h_choice == '7':
                if random() > (enemy.Agility / hero.Agility) * 0.8:
                    print 'Voce conseguiu fugir da batalha'
                    break
                else:
                    print 'Voce tentou fugir e nao conseguiu.'

            # Battle Win Check
            if enemy.HP <= 0:
                print 'Voce venceu a batalha!'
                battle_reset()
                break

        clc()


clc()
hero.Right_Hand = wooden_sword
equip_reset()
battle1(wolf)

raw_input("Aperte <Enter> para sair")
