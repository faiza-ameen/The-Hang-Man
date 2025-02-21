from colorama import Fore, Style
print()
print("**** WELCOME TO THE HANGMAN GAME ****")
print()
class play():

    def word(self):
        import random
        failed_choice = 1
        in_choice = 5
        self.word_choice = random.choice(self.name)
        self.hwords =  ["_"] * len(self.word_choice)
        print(f"{Fore.RED}You only have 6 incorrect choices.{Style.RESET_ALL}")
        print()
        while True:

            letter = input("Enter your choice: ").lower()
                            
            if letter not in self.word_choice:
                print(f"{Fore.RED}Incorrect choice => {failed_choice}.{Style.RESET_ALL}")
                failed_choice += 1
                print(f"{Fore.RED}You have {in_choice} choices left!{Style.RESET_ALL}")
                in_choice -= 1
            print()

            for index in range(len(self.word_choice)):
                if self.word_choice[index] == letter:
                    self.hwords[index] = letter

            print(" ".join(self.hwords))

            if failed_choice == 6:
                print(f"{Fore.RED}You have reached your attempts."
                        f"\n BETTER LUCK NEXT TIME!{Style.RESET_ALL}")
                print(f"The word was : {Fore.BLUE} {self.word_choice}{Style.RESET_ALL}")
                break

            if "_" not in self.hwords:
                print(f"{Fore.GREEN}CONGRATULATIONS!!\nYOU HAVE GUESSED THE RIGHT WORD!!!{Style.RESET_ALL}")
                break

class hangman:

    name = input("Enter your full name: ").title()
    print(name)

    def categories(self):

        print()
        print("We have four categories in this game:"
        "\n1- Movie names."
        "\n2- Seasons."
        "\n3- Songs."
        "\n4- All."
        f"\n{Fore.RED}Before you select out an option from these categories, we would like to tell you that this game includes only English work.{Style.RESET_ALL}")

        choice = int(input("Enter your category: "))

        if choice == 1:
            import random

            class Movies(play):

                name = ["spiderman", "lift", "anyonebutyou",
                            "theconjuring", "misteramerica","theflash",
                            "jurassicworld", "missionimpossible","interstellar",
                            "thenotebook", "damsel"]
                print()

            m = Movies()
            m.word()

        elif choice == 2:
            import random

            class Seasons(play):
                name = ["howimetyourmother", "friends", "bigbangtheory","you","emilyinparis",
                        "bridgerton", "ginnyandgeorgia", "queencharlotte", "atypical","xokitty"]
                
            s = Seasons()
            s.word()
                
        elif choice == 3:
            import random
            class Songs(play):
                name = ["badblood", "letmedownslowly", "faded", "umbrella", "closer",
                        "lily", "breakmyheart", "dieforyou","findyou", "howlong"]
                
            s1 = Songs()
            s1.word()

        elif choice == 4:
            import random
            class all(play):
                name = ["badblood", "letmedownslowly", "faded", "umbrella", "closer",
                    "lily", "breakmyheart", "dieforyou","findyou", "howlong",
                    "howimetyourmother", "friends", "bigbangtheory","you","emilyinparis",
                    "bridgerton", "ginnyandgeorgia", "queencharlotte", "atypical","xokitty",
                    "spiderman", "lift", "anyonebutyou","theconjuring", "misteramerica","theflash",
                    "jurassicworld", "missionimpossible","interstellar",
                    "thenotebook", "damsel" ]
            a = all()
            a.word()
            

c = hangman()
c.categories()

class loop(hangman):
    while True:
        ask = input("Do you want to play another round?(yes/no): ").lower()
        if ask == "yes":
            c = hangman()
            c.categories()
        else:
            break