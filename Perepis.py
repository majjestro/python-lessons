surnames = []
count_output = 0
years_range = [int(input("Введите минимальный возраст: ")), int(input("Введите максимальный возраст: "))]
current_year = int(input("Введите текущий год: "))
f = open('Perepis.txt')
try:
    for line in f:
        full_name = line.split("  ", 3)
        birthday = [int(i) for i in full_name.pop(3)[0:-1].split('.')]
        if (birthday[2] < 1978): count_output += 1
        if (years_range[0] < current_year - birthday[2] < years_range[1]): print(line.replace("  ", ' ')[0:-1])
        surnames.append(full_name[0])
    print("\nФамилии людей, родившихся раньше 1978 года:\n", '\n'.join(surnames), sep='')
finally:
   f.close()

input()
