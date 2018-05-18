fp = open("D:\PyLadies\pyladies12\zadanie3\members.txt", encoding='UTF-8')
members = {}
for line in fp:
#    print(line)
    name, fathers_name, birth_place, age, share = line.split(',')
    print(name)
#    print(name,fathers_name, birth_place, age, share)
    members[name.replace('\ufeff','')] = {
        'fathers_name': fathers_name if fathers_name != "-" else "",
        'birth_place': birth_place,
        'age': int(age) if age != "-" else 0,
        'share': share
    }
print(members)
fp.close()