

# will come back to implement my final return with f strings ----------------------------

full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    if not isinstance(character_name, str):
        return 'The character name should be a string'
    elif not character_name:
        return 'The character should have a name'
    elif len(character_name) > 10:
        return 'The character name is too long'
    elif ' ' in character_name:
        return 'The character name should not contain spaces'
    elif any(not isinstance(s, int) for s in [strength, intelligence, charisma]):
        return 'All stats should be integers'
    elif any(s < 1 for s in [strength, intelligence, charisma]):
        return 'All stats should be no less than 1'
    elif any(s > 4 for s in [strength, intelligence, charisma]):
        return 'All stats should be no more than 4'
    elif strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'
    else:
        return (
            character_name + '\n' +
            'STR ' + full_dot * strength + empty_dot * (10 - strength) + '\n' +
            'INT ' + full_dot * intelligence + empty_dot * (10 - intelligence) + '\n' +
            'CHA ' + full_dot * charisma + empty_dot * (10 - charisma)
        )
