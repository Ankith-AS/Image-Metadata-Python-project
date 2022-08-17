from random import randint
import string
ans_list = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
hap_or_sad_list = ["I sense turbulence.", "Wonder awaits.", "I sense negativity.", "I predict joyousness."]
new_list = ["I sense great results.", "Disaster awaits.", "The possibilities are endless.", "As i see it, good."]

question = [" "]
question_index = 1
while True:
    
    str = question.append(input("Ask for your fortune...    "))
    if question[question_index].find("happy") > -1:
        print(hap_or_sad_list[randint(0, len(hap_or_sad_list) - 1)])
        break
    elif question[question_index].find("sad") > -1:
        print(hap_or_sad_list[randint(0, len(hap_or_sad_list) - 1)])
        break
    elif question[question_index].find("new") > -1:
        print(new_list[randint(0, len(new_list) - 1)])
        break
    else:
        print(ans_list[randint(0, len(ans_list) - 1)])
    question_index += 1
    break