#DOPIS'
filename = "students4.txt"
fd = open (filename , "a")
fd.write("DOPIS'")
fd.close()
#ZAPIS'
filename = "students5.txt"
fd = open (filename , "w")
fd.write("Zapis''")
fd.close()
#poisk v file
a = str(input("Введите имя и фамилию студента: "))
file1 = open("students4.txt","r")
text1 = file1.read()
if a in text1:
    print ("Студент есть в 4 группе.")
else:
    print("Такой студент не найден в 4 группе.")
file2 = open("students5.txt","r")
text2 = file2.read()
if a in text2:
    print ("Студент есть в 5 группе.")
else:
    print("Такой студент не найден в 5 группе.")
file3 = open("students6.txt","r")
text3 = file3.read()
if a in text3:
    print ("Студент есть в 6 группе.")
else:
    print("Такой студент не найден в 6 группе.")
#poiisk v kataloge
import os
import os.path
file_name = "students4.txt" 
cur_dir = os.getcwd() 

while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)
    if file_name in file_list:
        print ("File Exists in: ", cur_dir)
        break
    else:
        if cur_dir == parent_dir: 
            print ("File not found")
            break
        else:
            cur_dir = parent_dir
