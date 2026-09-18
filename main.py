full_dot = '●'
empty_dot = '○'
def create_character(character_name,strength,intelligence,charisma):
    the_list = [strength,intelligence,charisma]
    checking_stats_equal_int = True
    

    strength_full_dot = strength * full_dot
    intelligence_full_dot = intelligence * full_dot
    charm_full_dot = charisma * full_dot
    strength_empty_dot = strength * full_dot
    intelligence_empty_dot = intelligence * full_dot
    charm_empty_dot = charisma * full_dot

    if type(character_name) != str:
        return "The character name should be a string"
    elif character_name == "":
        return "The character should have a name"
    elif len(character_name) > 10:
        return "The character name is too long"
    elif character_name == " ":
        return "The character name should not contain spaces"
    
    elif any(the_list <1):
        return "All stats should be no less than 1"
    elif any(the_list > 4):
        return"All stats should be no more than 4"
    elif strength + intelligence + charisma !=7:
        return "The character should start with 7 points"
    else:
        return f"{character_name}\n STR {strength_full_dot}{strength_empty_dot}\n INT {intelligence_full_dot}{intelligence_empty_dot}\n CHA {charm_full_dot}{charm_empty_dot}"

    
    
    
    
    
printing_variable = create_character("e" ,3,5,4 )
print(printing_variable)
