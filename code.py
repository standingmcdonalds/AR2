import sys
from colorama import Fore, Style, init
init()
import os

# user guide for making your own
# addon/addon2 will set replacee/replacement to a string. addon can be a list (optional), addon2 cant
# start_key/start_key2 will start the user in a json from a set position (make sure the set position doesnt share a name or ill go to the first one)
# return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names finishes an area and returns all the data back and finishes this codes use
# add a line push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names) for doing multiple changes of seperate things in the same case
# if you want to skip then set skip to True
# leaving empty and only returning will make the user enter 2 from the json starting from the top

def get_valid_input(prompt, valid_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            if valid_values is None or int(user_input) in valid_values:
                return int(user_input)
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose from {valid_values}.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a valid number.\n{Style.RESET_ALL}")


def push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):
    main_module = sys.modules['__main__']
    main_module.backbone(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)


def run(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):

    while True:
        options = get_valid_input(f"Asset replacements:\n"
                        f"0:  {Fore.GREEN}Custom{Style.RESET_ALL}\n"
                        f"1:  {Fore.GREEN}Sights{Style.RESET_ALL}\n"
                        f"2:  {Fore.GREEN}Weapon Sounds{Style.RESET_ALL}\n"
                        f"3:  {Fore.GREEN}Hit sounds{Style.RESET_ALL}\n"
                        f"4:  {Fore.GREEN}Weapon Skins{Style.RESET_ALL}\n"
                        f"5:  {Fore.GREEN}No textures{Style.RESET_ALL}\n"
                        f"Type 'back' to return to the previous menu.\n: ",
                        valid_values=[0, 1, 2, 3, 4, 5]
        )
        if options == 'back':
            print(f"{Fore.CYAN}\nReturning to main menu.{Style.RESET_ALL}")
            skip = True
            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        
        try:
            match options:
                case 0:
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 1:
                    start_key = "AR2 reticles"
                    start_key2 = "reticles"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 2:
                    start_key = "AR2 guns"
                    start_key2 = "gun sounds"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names                    
                case 3:
                    start_key = "AR2 hit sounds"
                    start_key2 = "gun sounds"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 4:
                    start_key = "AR2 skins"
                    start_key2 = "Skin replacements"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names                
                case 5:
                    start_key = "textures"
                    addon2 = "75205be5a167842c7ed931d9d5a904ca"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
