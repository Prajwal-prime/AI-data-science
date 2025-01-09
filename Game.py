def start_game():
    print("Welcome to the Avengers Adventure Game!")
    print("You are recruited as a new Avenger. Do you accept the challenge?")
    choice = input("Type 'yes' to accept or 'no' to decline: ").lower()

    if choice == 'yes':
        avengers_base()
    else:
        print("You declined the offer. The world needed you, but you chose otherwise. Game Over.")

def avengers_base():
    print("You arrive at the Avengers base. Iron Man gives you a mission to save the world.")
    print("Do you accept his mission or request training first?")
    choice = input("Type 'mission' to accept or 'training' to train: ").lower()

    if choice == 'mission':
        first_mission()
    else:
        training_session()

def training_session():
    print("You decide to train with Black Widow and Captain America.")
    print("They teach you combat skills and teamwork strategies.")
    print("After training, you are ready for the mission. Do you want to proceed?")
    choice = input("Type 'yes' to proceed or 'no' to stay back: ").lower()

    if choice == 'yes':
        first_mission()
    else:
        print("You stayed back and missed the chance to prove yourself. Game Over.")

def first_mission():
    print("Your first mission is to retrieve the Tesseract from Loki.")
    print("Do you confront Loki directly or sneak into his lair?")
    choice = input("Type 'confront' or 'sneak': ").lower()

    if choice == 'confront':
        confront_loki()
    else:
        sneak_into_lair()

def confront_loki():
    print("You confront Loki. He uses his illusions to trick you.")
    print("Do you attack or wait for backup?")
    choice = input("Type 'attack' or 'wait': ").lower()

    if choice == 'attack':
        print("Loki defeats you with his scepter. You failed the mission. Game Over.")
    else:
        print("Thor arrives just in time and defeats Loki. The Tesseract is secured. Mission Complete!")
        alien_invasion()

def sneak_into_lair():
    print("You sneak into Loki's lair and find the Tesseract guarded by Chitauri soldiers.")
    print("Do you fight the guards or call for reinforcements?")
    choice = input("Type 'fight' or 'call': ").lower()

    if choice == 'fight':
        print("You bravely fight the guards and secure the Tesseract. Mission Complete!")
        alien_invasion()
    else:
        print("Reinforcements arrive, and together you defeat the guards. Mission Complete!")
        alien_invasion()

def alien_invasion():
    print("Loki's defeat enrages Thanos, who sends an army to Earth.")
    print("Do you defend New York or evacuate civilians?")
    choice = input("Type 'defend' or 'evacuate': ").lower()

    if choice == 'defend':
        print("You join the Avengers in an epic battle and save New York. You are a true hero!")
        print("Congratulations, you saved the world. Game Over.")
    else:
        print("You prioritize saving lives and successfully evacuate thousands. Your bravery is celebrated.")
        print("Congratulations, you saved the world. Game Over.")

if __name__ == "__main__"
    start_game()
