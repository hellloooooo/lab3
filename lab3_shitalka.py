import csv
import sys

print("Группа 4")
filename = "students4.txt"
text_file = open("students4.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()

print("Группа 5")
filename = "students5.txt"
text_file = open("students5.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()


print("Группа 6")
filename = "students6.txt"
text_file = open("students6.txt", "r")
reader = csv.reader(text_file, delimiter = "\t")
for str in reader:
    print(str)
text_file.close()