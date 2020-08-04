import time

AVERAGE_LETTERS_IN_WORDS = 5
with open("text.txt") as f:
    target_text = f.read()

target_pars = target_text.split("\n")
correct_letters = 0
wrong_letters = 0
elapsed_time = 0
print("hi welcome are you ready to take test")
_ = input("then press enter")

for target_para in target_pars:
    splited_target = target_para.split(" ")
    print(target_para)
    start_time = time.time()
    typed_text = input()
    stop_time = time.time()
    count = 0
    for word in typed_text.split(" "):
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
