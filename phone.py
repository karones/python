#генерация номеров по префиксу. file in - список префиксов, file out - номера
import re
def stringToInt(string):
    length = len(string)
    if (length == 3):
        return [(int(string) +1 )*  1000000000,  int(string) *  1000000000]
    if (length == 4):
        return [(int(string) +1 )*  100000000,  int(string) *  100000000]
    if (length == 5):
        return [(int(string) +1 )*  10000000,  int(string) *  10000000]
    if (length == 6):
        return [(int(string) +1 )*  1000000,  int(string) *  1000000]
    if (length == 7):
        return  [(int(string) +1 )* 100000,  int(string) *  100000]
    if (length == 8):
        return  [(int(string) +1 )*  10000,  int(string) *  10000]
    if (length == 9):
        return  [(int(string) +1 )*  1000,  int(string) *  1000]
    if (length == 10):
        return  [(int(string) +1 )*  100,  int(string) *  100]
    if (length == 11):
        return  [(int(string) +1 )*  10,  int(string) *  10]
try:
    inFile = open('in',  'r')
    outFile = open ('out',  'w')
except IOError:
    print ("Ошибка открытия файла")
   # print (error)
    
prefixList = []     
for line in inFile:
    line.rstrip()
    line =re.sub(r"\+",  "",  line)
    line = re.sub(r"^8",  "7",  line)
    prefixList.append(line)

prefixInt = []
for prefix in prefixList:
    prefixInt.append(stringToInt(prefix))

count = 0    
for massiv in prefixInt:
    while massiv[0] > massiv[1]:
        outFile.write("+" + str(massiv[1]) + "\n")
        massiv[1] +=1
        count += 1
print ("Файл сформирован:" + str(count) + "номеров" )
    
    
