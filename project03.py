"""
Author: Kouame Alexandre Paul
Last updated: 09:13 PM UTC

Program: Adventure Game
"""
print('\nThe game puts you in the shoes of a warrior, ready to protect your village from a fearsome monster. Your mission is to choose an enemy to face and make the right decisions to defeat the creature and save your community.')

#Scenario level 1
monster = input('\nWhich monster do you want to face ( dragon or anaconda )? ')
if monster.lower() == 'dragon' :
    print(f'\nYou pick up a {monster.upper()}, a winged creature that spits fire and flies over your village.')
    print("So, you'll have to take to the air by piloting a plane to attack the beast from the sky.")
    
    #Scenario level 2
    plane = input('\nWhich type of plane will you fly. Choose(A or B) (A - fast fighter jet or B - heavy bomber)? ')
    if plane.upper() == "A":
        print('You pick up a Fast Fighter Jet, capable of agile maneuvers to dodge the dragon’s flames')
        print('(Jet or fast boat): You have the advantage of speed, but you’ll need to be precise in your attacks.')
        print('The dragon is swooping down, breathing fire. Your opponent is attacking!')
       
        #Scenario level 3
        attack = input('\nHow do you react. Choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
        if attack.upper() == "A":
            print('Dodge the flames: You attempt to outmaneuver the dragon by flying around it, using your plane’s agility to avoid the fire')
            print('(Dodge): You successfully avoid the flames, but you miss a chance to strike back. The battle continues')
        elif attack.upper() == "B":
            print("Counter-attack immediately: You fly straight towards the dragon and unleash your weapons, even though you risk getting burned in the process")
            print("(Counter-attack): You hit the dragon hard, but the flames scorch your plane. You’ll need to finish the fight before your plane takes too much damage.")
        else:
            print('You need to choose (A or B) (A - Dodge the attack or B - Strike back immediately)')
            print('GAME OVER')

    elif plane.upper() == "B":
        print('You pick up a heavy bomber, capable of dropping powerful bombs on the dragon, but slower and less maneuverable')
        print('(Bomber or warship): You have great firepower, but the monster could catch up to you before you can strike.')
        print('Your opponent is attacking!')

        #Scenario level 3
        attack = input('\nHow do you react. Choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
        if attack.upper() == "A":
            print('You pick up a Strike back immediately: You counter-attack with all the strength of your weapons, even if it exposes you to risks')
            print('(Counter-attack): You hit hard, but the monster retaliates. You will succeed if your chosen vehicle provides enough protection or agility')
        else:
            print('You need to choose (A or B) (A - Dodge the attack or B - Strike back immediately)')
            print('GAME OVER')
    
    else:
        print('You need to choose the plane you will fly. The plane should be a fast fighter jet or a heavy bomber')
        print('GAME OVER')

elif monster.lower() == 'anaconda' :
    print(f'\nYou pick up an {monster.upper()}, terrorizing fishermen in the murky waters.')
    print("So, you'll have to sail a boat to confront the giant snake in the ocean.")

    #Scenario level 2
    boat = input('\nWhich type of boat will you choose (A or B) (A - Fast and Light Boat or B - Heavy Warship)? ')
    
    if boat.upper() == "A":
        print('You pick up fast and light boat, to sail around the anaconda and attack it from a distance.')
        print('(Jet or fast boat): You have the advantage of speed, but you’ll need to be precise in your attacks.')
        print('The anaconda is rising from the water, ready to strike. Your opponent is attacking!')

        #Scenario level 3
        attack = input('\nHow do you react. Choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
        if attack.upper() == "A":
            print("Dodge its attack: You steer your boat sharply to the side, trying to avoid the serpent's powerful strike")
            print("(Dodge): You narrowly escape the anaconda’s grasp, but the monster is still in the water, ready to strike again.")
        elif attack.upper() == "B":
            print("Counter-attack immediately: You fire your weapons at the anaconda as it prepares to strike, even if it means exposing your boat to the serpent’s grasp.")
            print("(Counter-attack): You land a powerful hit, but the anaconda coils around your boat. You’ll need to break free quickly before it crushes your vessel.")
        else:
            print('Reaction not found.You had been choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
            print('YOU FAIL IN YOUR MISSION')

    elif boat.upper() == "B":
        print('You pick up a heavy warship, armed with cannons to strike hard, but harder to maneuver.')
        print('Heavy warship, armed with cannons to strike hard, but harder to maneuver')
        print('The anaconda is rising from the water, ready to strike. Your opponent is attacking!')

        #Scenario level 3
        print('')
        attack = input('\nHow do you react. Choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
        if attack.upper() == "A":
            print("Dodge its attack: You steer your boat sharply to the side, trying to avoid the serpent's powerful strike")
            print("(Dodge): You narrowly escape the anaconda’s grasp, but the monster is still in the water, ready to strike again.")
        elif attack.upper() == "B":
            print("Counter-attack immediately: You fire your weapons at the anaconda as it prepares to strike, even if it means exposing your boat to the serpent’s grasp.")
            print("(Counter-attack): You land a powerful hit, but the anaconda coils around your boat. You’ll need to break free quickly before it crushes your vessel.")
        else:
            print('Reaction not found.You had been choose(A or B) (A - Dodge the attack or B - Strike back immediately)? ')
            print('YOU FAIL IN YOUR MISSION')

    else:
        print('You need to choose the boat for fight. The boat should be (A or B) (A - Fast and Light Boat or B - Heavy Warship)? ')
        print('GAME OVER')

else :
    print('You need to choose the monster you want to face. The monster should be dragon or anaconda.')
    print('GAME OVER')