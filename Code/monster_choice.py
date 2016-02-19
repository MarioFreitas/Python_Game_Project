from random import random

def monster_choice(enemy):
    m_choice = random()
    if enemy.HP > 0.5*enemy.HP_Max:
        if enemy.Stamina > 0.75*enemy.Stamina_Max:
            if m_choice < 0.8:
                m_choice = 1
            elif m_choice < 0.95:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.5*enemy.Stamina_Max:
            if m_choice < 0.65:
                m_choice = 1
            elif m_choice < 0.90:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.25*enemy.Stamina_Max:
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
    elif enemy.HP > 0.20*enemy.HP_Max:
        if enemy.Stamina > 0.75*enemy.Stamina_Max:
            if m_choice < 0.25:
                m_choice = 3
            elif m_choice < 0.90:
                m_choice = 1
            elif m_choice < 0.95:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.5*enemy.Stamina_Max:
            if m_choice < 0.25:
                m_choice = 3
            elif m_choice < 0.80:
                m_choice = 1
            elif m_choice < 0.90:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.25*enemy.Stamina_Max:
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
        if enemy.Stamina > 0.75*enemy.Stamina_Max:
            if m_choice < 0.75:
                m_choice = 3
            elif m_choice < 0.90:
                m_choice = 1
            elif m_choice < 0.95:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.5*enemy.Stamina_Max:
            if m_choice < 0.75:
                m_choice = 3
            elif m_choice < 0.85:
                m_choice = 1
            elif m_choice < 0.95:
                m_choice = 4
            else:
                m_choice = 5
        elif enemy.Stamina > 0.25*enemy.Stamina_Max:
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
    return str(m_choice)
