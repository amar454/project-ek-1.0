try: 
    # Imports
    import webbrowser
    import pyautogui
    from tkinter import Tk  
    import time 
    import pyperclip
    # I might need these libraries later.
    # import keyboard 
    # import msvcrt
    # import argparse
    import string
    import random
    import json
except ImportError as f: # Catches if some libraries aren't isntalled. Might not be neccisarry, but whatever.
    print("Some dependencies aren't installed.")
def save_alt(username: str, password: str):
    json.load(open("alt_data.json", 'r'))
    
def make_alt(name: str, amount: int, group_name: str): # function unfortunately doesn't work, Roblox Captcha :|
    """
    Routine creates alt accounts using pyautogui, and will make a name and increment from 001-999. 
    I don't really recommend putting more then like 20 because it is pretty slow.
    """
    alt_data = json.load(open(r'alt_data.json'))
    if group_name in alt_data:
        return "Group name already taken."
    # This for loop basically checks if any of the names within the amount given alts in the automated alt naming process are taken.
    for f in range(amount):
        # continue
        pyperclip.copy('')
        webbrowser.open("https://www.roblox.com/")
        time.sleep(2)
        pyautogui.moveTo(x=822, y=384)
        pyautogui.leftClick()
        pyautogui.moveTo(x=801, y=454)
        pyautogui.leftClick()
        pyautogui.moveTo(x=977, y=389)
        pyautogui.leftClick()
        pyautogui.moveTo(x=971, y=449)
        pyautogui.leftClick()
        pyautogui.moveTo(x=1093, y=389)
        pyautogui.leftClick()
        pyautogui.moveTo(x=1055, y=933)
        pyautogui.leftClick()
        pyautogui.moveTo(x=927, y=478)
        pyautogui.leftClick()
        pyautogui.write(name + "_" + str((range(amount).index(f))+1).zfill(3))
        pyautogui.leftClick()
        pyautogui.moveTo(x=746, y=497)
        pyautogui.dragTo(960, 498, 0.5, button='left')
        pyautogui.hotkey('ctrl', 'c')
        if pyperclip.paste() == 'This username is already in use':
            return print("\nError. One or more of the usernames auto generated were unfortunately already taken. Try a different name.")
        elif pyperclip.paste() == 'Username not appropriate for ':
            return print("\nError. The username isn't appropriate for Roblox. Try a different name.")
        elif pyperclip.paste() == '':
            pass
        else:
            return "\nAnother error was encountered, most likely the name is too long. "
        print(f'Checked name {f+1}, not taken.')
    
    group_alt_names = []
    # appends nicknames for json storage later.
    for f in range(amount): 
        group_alt_names.append(name + "_" + str((range(amount).index(f))+1).zfill(3))
    
    
    
    # This loop basically is a macro that performs a full alt creation after checks are completed.
    group_alt_dict = {} 
    for f in range(amount):
        # continue
        webbrowser.open("https://www.roblox.com/")
        if f == 0: time.sleep(6)
        if f != 0: time.sleep(2)
        pyautogui.moveTo(x=822, y=384)
        pyautogui.leftClick()
        pyautogui.moveTo(x=801, y=454)
        pyautogui.leftClick()
        pyautogui.moveTo(x=977, y=389)
        pyautogui.leftClick()
        pyautogui.moveTo(x=971, y=449)
        pyautogui.leftClick()
        pyautogui.moveTo(x=1093, y=389)
        pyautogui.leftClick()
        pyautogui.moveTo(x=1055, y=933)
        pyautogui.leftClick()
        pyautogui.moveTo(x=927, y=478)
        pyautogui.leftClick()
        pyautogui.write(name + "_" + str((range(amount).index(f))+1).zfill(3))
        pyautogui.moveTo(x=906, y=568)
        character_list = list(string.ascii_letters + string.digits + "!@#$%^&*()")
        random.shuffle(character_list)
        password = []
        for i in range(16):
            password.append(random.choice(character_list))
        random.shuffle(password)
        password = "".join(password)
        group_alt_dict[name + "_" + str((range(amount).index(f))+1).zfill(3)] = (password)
        pyautogui.leftClick()
        pyautogui.write(password)
        pyautogui.moveTo(x=952, y=805)
        pyautogui.leftClick()
        time.sleep(.5)
        pyautogui.leftClick()
        time.sleep(6)
        pyautogui.moveTo(x=1867, y=120)
        pyautogui.leftClick()
        pyautogui.moveTo(x=1816, y=311)
        pyautogui.leftClick()
        pyautogui.moveTo(x=946, y=771)
        pyautogui.leftClick()
    alt_data[group_name] = group_alt_dict
    
    
    print(alt_data)
    
    json.dump(obj=alt_data, fp=open(r'alt_data.json', 'r+')) # unnote this line when you want alt account data to be saved and stored.
if __name__ == "__main__":
    pass