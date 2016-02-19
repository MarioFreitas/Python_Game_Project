from random import random
from random import randint

def clc():
    print '\n'*100

#Define Monster
class Monster(object):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __repr__(self):
        return "Nome: %s\nVida: %.1f\n" % (self.name,self.health)

#Define Heroe
class Heroe(object):
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def __repr__(self):
        return "Nome: %s\nVida: %.1f\n" % (self.name,self.health)

#Initialize Monster and Heroe
ogre = Monster("Ogro", 120.0, 30.0, 10.0)
link = Heroe("Link", 120.0, 30.0, 10.0)

#Define Battle
def battle1(ver):
    while ver == True:
        #Print Battle Info
        print link
        print ogre

        #Player Turn
        choice = raw_input("O que voce quer fazer?\nAtacar [a] or Correr [r]? ")
        print "\n"*2
        if choice == 'a' or choice == 'A':
            atk_bns = float(1 + random())
            atk = float(link.attack * atk_bns)
            def_bns = float(1+ random())
            deff = float(ogre.defense * def_bns)         
            if atk > deff:
                ogre.health -= atk - deff
                s1 = "O monstro tomou %.1f de dano" % (atk-deff)
            else:
                s1 = "O monstor nao tomou dano"        
        if choice == 'r' or choice == 'R':
            r = randint(1,10)
            if r > 7:
                s1 = "Voce conseguiu fugir\nFIM!"
                break
            else:
                s1 = "Voce nao conseguiu fugir"

        #Verification
        if ogre.health <= 0:
            print "Voce venceu!"
            break
        
        #Monster Turn
        if link.health > 0:
            atk_bns = float(1 + random())
            atk = float(ogre.attack * atk_bns)
            def_bns = float(1+ random())
            deff = float(link.defense * def_bns)
            if atk > deff:
                link.health = float(link.health - (atk - deff))
                s2 = "Voce tomou %.1f de dano" % (atk-deff)

        print "\n"
        # Verification
        if link.health <= 0:
            print "Voce perdeu!"
            break

        clc()
        print s1
        print s2
        print ""
        

clc()
battle1(True)
                
raw_input("Aperte qualquer tecla para sair")
    
