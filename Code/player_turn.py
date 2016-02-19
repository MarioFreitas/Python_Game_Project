from game import hero, battle_reset
from game import enemy
from c_functions import pause
from random import random


# Player Turn
def player_turn(h_choice, m_choice, h_atk, m_def):
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
            print 'O inimigo se defendeu. \nO inimigo recuperou um pouco de stamina. \nVoce causou %.1f de dano.' % \
                  (h_atk - m_def)
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
            return False
            # break
        else:
            print 'Voce tentou fugir e nao conseguiu.'

    # Battle Win Check
    if enemy.hp <= 0:
        print 'Voce venceu a batalha!'
        battle_reset()
        return False
        # break
