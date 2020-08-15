import time
from os import system,name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


AVERAGE_LETTERS_IN_WORDS = 5
with open("text.txt",'r') as f:
    target_text = f.read()
clear()
target_pars = target_text.split("\n")
correct_letters = 0
wrong_letters = 0
elapsed_time = 0
lines=[]
for para in target_pars:
    lines.extend(para.split(". "))
print("hi welcome are you ready to take test")
_ = input("then press enter")
for line in lines:
    clear()
    splited_target = line.split(" ")
    print(line)
    start_time = time.time()
    typed_text = input()
    stop_time = time.time()
    count = 0
    typed_text_split=typed_text.split(" ")
    for word in typed_text_split:
        try:
            if word == splited_target[count]:
                correct_letters += len(word)
            else:
                wrong_letters += len(word)
        except IndexError:
            break
        count += 1
    elapsed_time += stop_time - start_time
total_letters = correct_letters + wrong_letters
wrong_words = wrong_letters / AVERAGE_LETTERS_IN_WORDS
correct_words = correct_letters / AVERAGE_LETTERS_IN_WORDS
total_words = wrong_words + correct_words
time_in_min = elapsed_time / 60
net_speed = int(total_words / time_in_min)
gross_speed = int(correct_words / time_in_min)
print(f"net speed is {net_speed},gross speed is {gross_speed}")
