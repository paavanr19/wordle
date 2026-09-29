import requests
from colorama import Fore, Style

response = requests.get(
    "https://random-word-api.herokuapp.com/word",
    params={"length": 5})

target_word=response.json()[0]
print(target_word)


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
    return word == target_word 



guesses_dict={}
win_condition = False
counter = 0

while counter < 5 and not win_condition:
    entered_word = input("Enter a five letter word: ")
    entered_word=entered_word.strip().replace(" ","")
    if validate_word(entered_word) is True:
        if entered_word not in guesses_dict:
            guesses_dict[entered_word]=counter+1
        else:
            print("You already guessed that word")
            continue
        counter+=1
        checked_word=parse_word(entered_word,target_word)
        print("checked word: " + checked_word)
        if (check_win(entered_word,target_word)):
            win_condition=True
            break;
        else:
            continue;
    else:
        print("Invalid word. Try again")
        continue


if (win_condition):
    print("You won! It took you",counter,"tries")
else:
    print(Fore.RED + "You lost. The word was ", target_word , Style.RESET_ALL)
    


