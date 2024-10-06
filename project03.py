"""
Author: Kouame Alexandre Paul
Last updated: 09:13 PM UTC

Program: Adventure Game

For creativity I prefered to ask user at prompt to choose cpital letter like A or B, ... instead typed every string to easy choice
"""
print('\nThe game puts you in the shoes of a warrior, ready to protect your village from a fearsome monster. Your mission is to choose an enemy to face and make the right decisions to defeat the creature and save your community.')

#Scenario level 1
monster = input('\nWhich monster do you want to face ( DRAGON or ANACONDA )? ')
if monster.lower() == 'dragon' :
    print(f'\nYou pick up a {monster.upper()}, a winged creature that spits fire and flies over your village.')
    print("So, you'll have to take to the air by piloting a plane to attack the beast from the sky.")
    
    #Scenario level 2
    plane = input('\nWhich type of plane will you fly. Choose: A(FAST FIGHTER JET) or B (HEAVY BOMBER)? ')
    if plane.upper() == "A":
        print('You pick up a FAST FIGHTER JET, capable of agile maneuvers to dodge the dragon’s flames')
        print('You have the advantage of speed, but you’ll need to be precise in your attacks.')
        print('The dragon is swooping down, breathing fire. Your opponent is attacking!')
       
        #Scenario level 3
        attack = input('\nHow do you react. Choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(FLY HIGHER TO GAIN ALTITUDE) or D(CALL FOR REINFORCEMENTS)? ')
        if attack.upper() == "A":
            print()
            print('DODGE the flames: You attempt to outmaneuver the dragon by flying around it, using your plane’s agility to avoid the fire')
            print('You successfully avoid the flames, but you miss a chance to strike back. The battle continues')
        elif attack.upper() == "B":
            print()
            print("COUNTER-ATTACK immediately: You fly straight towards the dragon and unleash your weapons, even though you risk getting burned in the process")
            print("You hit the dragon hard, but the flames scorch your plane. You’ll need to finish the fight before your plane takes too much damage.")
        elif attack.upper() == "C":
            print()
            print("FLY HIGHER to gain altitude: You climb higher into the sky to get a better angle on the dragon and plan a more strategic strike, but this leaves you vulnerable for a moment.")
            print("You gain a better position, but the dragon gains ground. You’ll need to act fast before it’s too late.")
        elif attack.upper() == "D":
            print()
            print("CALL FOR REINFORCEMENTS: You radio in for backup from other pilots, hoping to overwhelm the dragon with multiple attackers. This takes time, but the extra help could be vital.")
            print("Your allies arrive, and together, you have a stronger chance to defeat the dragon, but you’ve lost precious time in the process.")
        else:
            print()
            print('You need to choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(FLY HIGHER TO GAIN ALTITUDE) or D(CALL FOR REINFORCEMENTS)')
            print('NO REACT GAME OVER')

    elif plane.upper() == "B":
        print('You pick up a HEAVY BOMBER, capable of dropping powerful bombs on the dragon, but slower and less maneuverable')
        print('You have great firepower, but the monster could catch up to you before you can strike.')
        print('Your opponent is attacking!')

        #Scenario level 3
        attack = input('\nHow do you react. Choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(FLY HIGHER TO GAIN ALTITUDE) or D(CALL FOR REINFORCEMENTS)? ')
        if attack.upper() == "A":
            print('\nDODGE the flames: You attempt to outmaneuver the dragon by flying around it, using your plane’s agility to avoid the fire')
            print('You successfully avoid the flames, but you miss a chance to strike back. The battle continues')
        elif attack.upper() == "B":
            print("\nCOUNTER-ATTACK immediately: You fly straight towards the dragon and unleash your weapons, even though you risk getting burned in the process")
            print("You hit the dragon hard, but the flames scorch your plane. You’ll need to finish the fight before your plane takes too much damage.")
        elif attack.upper() == "C":
            print("\nFLY HIGHER to gain altitude: You climb higher into the sky to get a better angle on the dragon and plan a more strategic strike, but this leaves you vulnerable for a moment.")
            print("You gain a better position, but the dragon gains ground. You’ll need to act fast before it’s too late.")
        elif attack.upper() == "D":
            print("\nCALL FOR REINFORCEMENTS: You radio in for backup from other pilots, hoping to overwhelm the dragon with multiple attackers. This takes time, but the extra help could be vital.")
            print("Your allies arrive, and together, you have a stronger chance to defeat the dragon, but you’ve lost precious time in the process.")
        else:
            print('\nYou need to choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(FLY HIGHER TO GAIN ALTITUDE) or D(CALL FOR REINFORCEMENTS)')
            print('NO REACT GAME OVER')
    
    else:
        print('You need to choose the plane you will fly. The plane should be a fast fighter jet or a heavy bomber')
        print('GAME OVER')

elif monster.lower() == 'anaconda' :
    print(f'\nYou pick up an {monster.upper()}, terrorizing fishermen in the murky waters.')
    print("So, you'll have to sail a boat to confront the giant snake in the ocean.")

    #Scenario level 2
    boat = input('\nWhich type of boat will you choose A(FAST AND LIGHT BOAT) or B(HEAVY WARSHIP)? ')
    
    if boat.upper() == "A":
        print('\nYou pick up FAST AND LIGHT BOAT, to sail around the anaconda and attack it from a distance.')
        print('You have the advantage of speed, but you’ll need to be precise in your attacks.')
        print('The anaconda is rising from the water, ready to strike. Your opponent is attacking!')

        #Scenario level 3
        attack = input('\nHow do you react. Choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(RETREAT TO DEEPER WATER) or D(SET A TRAP)? ')
        if attack.upper() == "A":
            print("\nDODGE its attack: You steer your boat sharply to the side, trying to avoid the serpent's powerful strike")
            print("You narrowly escape the anaconda’s grasp, but the monster is still in the water, ready to strike again.")
        elif attack.upper() == "B":
            print("\nCOUNTER-ATTACK immediately: You fire your weapons at the anaconda as it prepares to strike, even if it means exposing your boat to the serpent’s grasp.")
            print("You land a powerful hit, but the anaconda coils around your boat. You’ll need to break free quickly before it crushes your vessel.")
        elif attack.upper() == "C":
            print("\nRETREAT TO DEEPER WATERS: You steer your boat farther out into the ocean, hoping the deeper waters will slow down the anaconda’s movements, giving you more time to react.")
            print("You successfully move to deeper waters, slowing the anaconda, but you risk losing sight of the serpent.")
        elif attack.upper() == "D":
            print("\nSET A TRAP: You drop bait or explosives in the water to lure the anaconda into a vulnerable position, but this will require patience and careful timing.")
            print("The trap is set, and if the timing is right, you can deliver a critical blow, but the plan requires patience and precision.")
        else:
            print('\nYou need to choose : A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(RETREAT TO DEEPER WATER) or D(SET A TRAP)? ')
            print('NO REACT. GAME OVER')

    elif boat.upper() == "B":
        print('\nYou pick up a HEAVY WARSHIP, armed with cannons to strike hard, but harder to maneuver.')
        print('HEAVY WARSHIP, armed with cannons to strike hard, but harder to maneuver')
        print('The anaconda is rising from the water, ready to strike. Your opponent is attacking!')

        #Scenario level 3
        attack = input('\nHow do you react. Choose: A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(RETREAT TO DEEPER WATER) or D(SET A TRAP)? ')
        if attack.upper() == "A":
            print("\nDODGE its attack: You steer your boat sharply to the side, trying to avoid the serpent's powerful strike")
            print("You narrowly escape the anaconda’s grasp, but the monster is still in the water, ready to strike again.")
        elif attack.upper() == "B":
            print("\nCOUNTER-ATTACK immediately: You fire your weapons at the anaconda as it prepares to strike, even if it means exposing your boat to the serpent’s grasp.")
            print("You land a powerful hit, but the anaconda coils around your boat. You’ll need to break free quickly before it crushes your vessel.")
        elif attack.upper() == "C":
            print("\nRETREAT TO DEEPER WATERS: You steer your boat farther out into the ocean, hoping the deeper waters will slow down the anaconda’s movements, giving you more time to react.")
            print("You successfully move to deeper waters, slowing the anaconda, but you risk losing sight of the serpent.")
        elif attack.upper() == "D":
            print("\nSET A TRAP: You drop bait or explosives in the water to lure the anaconda into a vulnerable position, but this will require patience and careful timing.")
            print("The trap is set, and if the timing is right, you can deliver a critical blow, but the plan requires patience and precision.")
        else:
            print('You need to choose : A(DODGE THE ATTACK) or B(STRIKE BACK IMMEDIATELY) or C(RETREAT TO DEEPER WATER) or D(SET A TRAP)? ')
            print('NO REACT. GAME OVER')

    else:
        print('You need to choose the boat for fight. Choose: A(FAST AND LIGHT BOAT) or B(HEAVY WARSHIP)? ')
        print('GAME OVER')

else :
    print('You need to choose the monster you want to face. The monster should be dragon or anaconda.')
    print('GAME OVER')