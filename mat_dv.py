math = dict()
algebra = dict()
geometry = dict()
variants_win = [algebra, geometry, math]
f = open('mat_dv.txt')
try:
    for line in f:
        info = line.split(' ')
        for i in range(len(variants_win)):
            balls = int(info[3]) + int(info[4]) if (i == 2) else int(info[i+3])
            if (int(info[2]) not in variants_win[i]): variants_win[i] |= {int(info[2]): [balls,' '.join(info[0:1])]}
            else:
                max_ball = variants_win[i].get(int(info[2]))[0]
                if (max_ball < balls): variants_win[i][int(info[2])] = [balls, ' '.join(info[0:1])]
                elif (max_ball == balls): variants_win[i][int(info[2])] = [balls, ' '.join(info[0:1]), variants_win[i][int(info[2])][1]]
finally:
   f.close()

for i in range(len(variants_win)):
    print(i,':',variants_win[i])
input()
