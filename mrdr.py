import turtle
t = turtle.Turtle 

clues = []

suspects = ["murderous miles", "nyphol nico", "antiblood atticus", "Reniffer the radiant revenant", "big burger"]
suspect = ["big burger"]
print(suspects)
murder = input("you go to sleep but you hear a dead guy walking around! oof..... Do you want to investigate (A), or get a piece of cake from the fridge (B)?")
print(murder)
while True:
    if murder == "A":
        die = input("Do you want to respawn? (Y or N):")
        if die == "Y":
            print(murder)
    elif murder == "B":
        print("You found a piece of red velvet cake!")
        eat = input("do you want to eat the cake? (Y)")
        if eat == "Y":
            print("You gained superpowers.")
        clues = print("the killer loves food...")
        clues = input("do you think the killer is murderous miles (A), nyphol nico (B), antiblood atticus (C), Reniffer the radiant revenant(D)or big burger (E)? ")
        if clues == "E":
            print("you won the burger games!!!")
            break
    murder2 = input("You run up the stairs and trip but start flying. Do you want to grab a knife (A), or grab an axe(B)?")
    print(murder2)
    while True:
            if murder2 == "B":
                axe = input("do you want to grab an axe(Y)")
                if axe == "Y":
                    print("You ripped your legs off and died")
            elif murder2 == "A":
                knife = input("Do you want to grab a knife? (Y or N):")
                if knife == "Y":
                    print("You grab the knife but stab yourself, but you end up making the knife poisonous.")
            clues = print("the killer uses weapons...")
            clues = input("do you think the killer is murderous miles (A), nyphol nico (B), antiblood atticus (C), Reniffer the radiant revenant(D)or big burger (E)? ")
            if clues == "E":
                print("you won the burger games!!!")
                break
            Murder3 = input("you see something with an axe run away in tall grass over in yonderville. Do you want to chase it (A) or 360 noscope it off the roof of your house (B)?")
            print(Murder3)
            while True:
                if Murder3 == "A":
                    Chase = input("Do you want to charge it? (Y):")
                    if Chase == "Y":
                        print("You charge it and eat grass, but you end up tripping and your brain falls out.")
                elif Murder3 == "B":
                    water = input("do you want to use your watergun?(Y)")
                if water == "Y":
                    print("You jump off the roof and hit the hamburger from 20 feet away!")
                break
            clues = print("the killer is a burger...")
            clues = input("do you think the killer is murderous miles (A), nyphol nico (B), antiblood atticus (C), Reniffer the radiant revenant(D)or big burger (E)? ")
            if clues == "E":
                print("you won the burger games!!!")
                break
    break


