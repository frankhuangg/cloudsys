import sys
client = sys.argv[1]
dict = {'angel':0, 'A':0, 'B':0, 'C':0}
if client not in dict.keys():
    print('Not User')
    sys.exit()
f = open("1.txt", "r", encoding = "utf-8")
temp = f.readlines()
for line in temp[2:]:
    line=line.replace(" ","").strip("\n").split(",")
    if client in line:
        print(line)
next = temp[1].split(':')[1].strip("\n")
f.close()
while(len(temp) == 7):
    f = open( next, "r", encoding = "utf-8")
    temp = f.readlines()
    for line in temp[2:]:
        line = line.replace(" ","").strip("\n").split(",")
        if client in line:
            print(line)
    next = (temp[1].split(':')[1].strip("\n"))
    f.close()
