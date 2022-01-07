count_output = 0
years_range = [int(input("Введите минимальный возраст: ")), int(input("Введите максимальный возраст: "))]
current_year = int(input("Введите текущий год: "))
f = open('Perepis.txt')
try:
    for line in f:
        name = line.split("  ", 3)
        birthday = [int(i) for i in name.pop(3)[0:-1].split('.')]
        if (years_range[0] < current_year - birthday[2] < years_range[1]):
            count_output += 1
            print(line.replace("  ", ' ')[0:-1]) 
finally:
   f.close()

input()
