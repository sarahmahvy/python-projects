full_dot = '●'
empty_dot = '○'

def create_character (character_name, strength, intelligence, charisma):
    if not isinstance (character_name, str):
        return 'The character name should be a string'
    if character_name == '':
        return 'The character should have a name'
    if len(character_name)>10:
        return 'The character name is too long'
    if " " in character_name:
        return 'The character name should not contain spaces'
    
    if not isinstance (strength,int) or not isinstance (intelligence,int) or not isinstance (charisma,int):
        return 'All stats should be integers'
    if (strength < 1) or (intelligence < 1) or (charisma < 1):
        return 'All stats should be no less than 1'
    if (strength + intelligence + charisma) <= 7:
        return 'The character should start with 7 points'
    STR = ''
    INT = ''
    CHA = ''
    for loop in range (10):
        if strength != 0:
            STR = STR + full_dot
            strength = strength - 1
        elif strength == 0:
            STR = STR + empty_dot

        if intelligence != 0:
            INT = INT + full_dot
            intelligence = intelligence - 1
        elif intelligence == 0:
            INT = INT + empty_dot

        if charisma != 0:
            CHA = CHA + full_dot
            charisma = charisma - 1
        elif charisma == 0:
            CHA = CHA + empty_dot

    display_strength = 'STR ' + STR
    display_intelligence = 'INT ' + INT
    display_charisma = 'CHA ' + CHA
    return "\n".join([
        character_name, display_strength, display_intelligence, display_charisma
    ])
name = input("Enter your character's name: ")
strength = int(input("Enter your character's strength: "))
intelligence = int(input("Enter your character's intelligence: "))
charisma = int(input("Enter your character's charisma: "))
print(create_character(name, strength, intelligence, charisma))


