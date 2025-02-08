# %% [markdown]
# # Lab 2 - Refactoring
# ## Refactoring is:
# 
# Refactoring is the process of restructuring or rewriting code, while not changing its original functionality. The goal of refactoring is to improve internal code by making many small changes without altering the code's external behavior. 
# 
# It is easier said than done. 

# %% [markdown]
# ### Part 1 - Warm-up
# 
# You will refactor the following code:

# %%
#stolen from https://realpython.com/python-refactoring/
#yes you can go there and look at what they did no do it yourself
x = 5
value = input("Enter a number: ")
y = int(value)
if x < y:
    print(f"{x} is less than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{x} is more than {y}")

# %%
# put your refactored code here

sol = 5
guess = int(input("Enter a number: "))
if sol < guess:
    print(f"{sol} is less than {guess}")
elif x == guess:
    print(f"{sol} is equal to {guess}")
else:
    print(f"{sol} is more than {guess}")

# %% [markdown]
# ## Part 2
# Refactor the following

# %%
def a(x, y):
    if x == "wizard":
        if y == "fireball":
            return "casts fireball"
        elif y == "lightning":
            return "casts lightning"
        else:
            return "does nothing"
    elif x == "warrior":
        if y == "slash":
            return "slashes with sword"
        elif y == "bash":
            return "bashes with shield"
        else:
            return "does nothing"
    else:
        return "does nothing"

def b(z):
    for i in range(10):
        if z == "dragon":
            return "fights dragon"
        elif z == "goblin":
            return "fights goblin"
        elif z == "orc":
            return "fights orc"
        else:
            return "does nothing"

def c():
    for i in range(5):
        print("exploring dungeon")
    print("finding treasure")

def main():
    print(a("wizard", "fireball"))
    print(a("warrior", "slash"))
    print(b("dragon"))
    c()
main()


# %%
# put your refactored code here
def character(chartype, move):
    spells = ["fireball", "lightning"]
    attacks = ["slash", "bash"]
    if chartype == "wizard":
        if move in spells:
            return "casts " + move
    elif chartype == "warrior":
        if move in attacks:
            return "uses " + move
    else:
        return "does nothing"

def mobs(monster):
    enemies = ["dragon", "goblin", "orc"]
    if monster in enemies:
        return "fights" + monster
    else:
        return "does nothing"

def c():
    for i in range(5):
        print("exploring dungeon\nfinding treasure")
        #it makes more sense to find treasure after exploring the dungeon and then to continue exploring after that

print(character("wizard", "fireball"))
print(character("warrior", "slash"))
print(mobs("dragon"))
c()

# %% [markdown]
# # Part 3
# Refactor your partners lab 1 code so it is a clean function. Look at part 4 and see how you can adapt the code to fit project one. 

# %%
# put your refactored code here

import random

comp_roll_stats = [0,0,0,0,0,0]
usr_roll_stats = [0,0,0,0,0,0]
win_stats = [0,0]
P_numbers = [random.randint(1,6) for _ in range(5)]
print('You rolled: ', P_numbers)
C_numbers = [random.randint(1,6) for _ in range(5)]
print('Computer rolled: ', C_numbers)

def userplay():
    for x in range(5):
        if 1 == P_numbers[x]:
            usr_roll_stats[0] += 1
        if 2 == P_numbers[x]:
            usr_roll_stats[1] += 1
        if 3 == P_numbers[x]:
            usr_roll_stats[2] += 1
        if 4 == P_numbers[x]:
            usr_roll_stats[3] += 1
        if 5 == P_numbers[x]:
            usr_roll_stats[4] += 1
        if 6 == P_numbers[x]:
            usr_roll_stats[5] += 1

def compplay():
    for x in range(5):
        if 1 == C_numbers[x]:
            comp_roll_stats[0] += 1
        if 2 == C_numbers[x]:
            comp_roll_stats[1] += 1
        if 3 == C_numbers[x]:
            comp_roll_stats[2] += 1
        if 4 == C_numbers[x]:
            comp_roll_stats[3] += 1
        if 5 == C_numbers[x]:
            comp_roll_stats[4] += 1
        if 6 == C_numbers[x]:
            comp_roll_stats[5] += 1

userplay()
compplay()
print('Results:')
for x in range(5):
    if P_numbers[x] > C_numbers[x]:
        print('You win!')
        win_stats[0] += 1
    if P_numbers[x] < C_numbers[x]:
        print('You Lose!')
        win_stats[1] += 1
    if P_numbers[x] == C_numbers[x]:
        print("You Tie!")
print('Stats:')
print(win_stats)
print('Roll History:')
print(usr_roll_stats, comp_roll_stats)

# %% [markdown]
# ## Part 4 - take home but start in class                  
# # Project #1  introduction 
# 
# 
# Your task is to develop a text-based video game focusing on the player profile, inventory system, and combat mechanics. Create a realistic player character with at least 10 inventory items, each with a description and an associated trait. Enjoy the process!
# 
# Incorporate all the concepts we've covered so far, including files (read and write), JSON, operators, lists, optional tuples, functions, modules, and classes.
# 
# ### Requirements:
# - **Player Type Selection**: Allow players to choose their character type. Set attributes based on the choice (e.g., wizard: magic = 10, knight: magic = 0).
# - **Inventory Display**: Implement a function to show the player's inventory.
# - **Item Details**: Write a function to provide detailed information about an inventory item (e.g., Knife: "forged in the depths of Polymar", +5 magic, edged weapon, one-handed).
#   - Bonus: Calculate bonuses when equipping and unequipping items.
# - **Inventory Management**: Create functions to add and remove items from the inventory.
# - **Persistence**: Ensure the game can save and reload the player's character using files.
# 
# Focus on building the player and inventory system for your text-based adventure game (similar to Zork). The map and gameplay can be developed later.
# 
# ### Game Features:
# - **Player Profile**: Include player stats.
# - **Inventory System**: Implement a bag to hold items.
# - **Items**: Include 10 items, each with a description and trait (e.g., +5 magic).
# - **Concepts**: Utilize functions, loops, arrays, classes, and constants. You may also use files and structs if desired.
# - **Player Type Selection**: Allow players to choose their character type and set attributes accordingly (e.g., wizard: magic = 10, knight: magic = 0).
# - **Inventory Display**: Implement a function to show the player's inventory.
# - **Code Quality**: Keep your code clean and consider various player needs, as this project will be handed off to a partner for further development.
# 
# 

# %% [markdown]
# # Project 1 - Part 1
# Spend time planning out your code. You may work with your partner to plan out your code. How would you like your game to play? 
# 
# Use a UML planner like: 
# 
# 
# https://miro.com/
# 

# %%



