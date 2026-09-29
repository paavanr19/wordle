import random
from colorama import Fore, Style


def validate_word(word):
    if len(word)!=5:
        return False
    for letter in word:
        if not (letter.isalpha()):
            return False
    return True

def parse_word(word, target_word):
    return_word=""
    index=0;
    for letter in word:
        if letter in target_word:
            if letter in target_word and target_word[index]==letter:
                #make letter green
                letter = Fore.GREEN + letter + Style.RESET_ALL
            else:
                #make letter yellow
                letter = Fore.YELLOW + letter + Style.RESET_ALL
        return_word+=letter
        index+=1
    return return_word

def check_win(word, target_word):
    return word is target_word 



        
file = open("words.txt","r") #open a file in read mode
target_word = random.choice(list(file))



win_condition = False
counter = 0

while counter < 5 and win_condition is False:
    entered_word = input("Enter a five letter word: ")
    entered_word=entered_word.strip().replace(" ","")
    print("You entered: " + entered_word)
    if validate_word(entered_word) is True:
        counter+=1
        print("valid word")
        checked_word=parse_word(entered_word,target_word)
        print("checked word: " + checked_word)
        if (check_win(checked_word,target_word)):
            print("You won!")
            win_condition=True
        else:
            continue;
    else:
        print("Invalid word. Try again")
        continue


if (win_condition):
    print("You won!. It took you "+counter+" tries")
else:
    print("You lost. The word was ", target_word)
    


