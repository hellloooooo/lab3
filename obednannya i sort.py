#obednannya
filenames = ['students4.txt', 'students5.txt', 'students6.txt']

with open('students456.txt', 'w') as outfile:

    for names in filenames:
        with open(names) as infile:

            outfile.write(infile.read())
#slovAR i sort po serednyomy
a_dictionary = {}
a_file = open("students4.txt")
for line in a_file:
    key, value = line.split(",")
    a_dictionary[key] = value
for i in sorted(a_dictionary.items(),key = lambda para: para[1]):
    print(i) 


