#fl = open('D:\PyLadies\pyladies12\zadanie1\message.txt','r')
#end = True

#while end:
#    znaki = fl.read(50)
#    if not znaki:
#        end = False
#    if 'sekret' in znaki:
#    new_word = ''.join([znaki[0], znaki[19, znaki[25], znaki[44], znaki[45], znaki[49]])
#    new_word = new_word.upper()
#    print(new_word)
#fl.close()

fp = open("D:\PyLadies\pyladies12\zadanie2\characters.txt",'r')
characters = fp.readline()
fp.close()
heroes_dictionary = {}
a_list = characters.split(";")
print(a_list)

for item in a_list:
    print(item)
    race, names = item.split(":")
    print(race)
    print(names)
    names_list = names.split("'")
    if race not in heroes_dictionary:
        heroes_dictionary[race] = names_list
    else:
        heroes_dictionary[race].extend()