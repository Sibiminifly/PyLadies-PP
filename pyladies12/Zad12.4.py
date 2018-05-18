#fl = open('cat.txt', 'a+', encoding='UTF-8')
#fp.readlines()
#for line in fl()
#    print(line)

#fl.write('Ala ma kota')
#fl.close('cat.txt','fixed.txt')

file_in = open('D:\PyLadies\pyladies12\zadanie4\cat.txt')
file_out = open ('D:\PyLadies\pyladies12\zadanie4\ fixed.txt', 'a+')

for line in file_in:
    fixed_line = line.replace('\\','')
    file_out .write(fixed_line)
file_in.close()
file_out.close()