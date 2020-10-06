# Spencer Nettles  
# Farkle Game
import random

def printTable(d):
    print("DIE  | ROLL")
    print("D1   | ", "     | "*d[0][1], d[0][0])
    print("D2   | ", "     | "*d[1][1], d[1][0])
    print("D3   | ", "     | "*d[2][1], d[2][0])
    print("D4   | ", "     | "*d[3][1], d[3][0])
    print("D5   | ", "     | "*d[4][1], d[4][0])
    print("D6   | ", "     | "*d[5][1], d[5][0])

def farkle(d, roll):
    counter = list()
    x = 0
    index = 0
    while x < len(d):
        if d[x][1] == roll:
            counter.append(d[x][0])
            index += 1
        x += 1

    farkle = True
    if counter.count(1) > 0 or counter.count(5) > 0:
        farkle = False
    elif counter.count(2) >= 3 or counter.count(3) >= 3 or counter.count(4) >= 3 or counter.count(6) >= 3:
        farkle = False
    
    if farkle:
        print("FARKLE LOSER!!!")

    return farkle


def roll(d, roll, keep):
    if roll == 0:
        d[0][0] = random.randint(1,6)
        d[1][0] = random.randint(1,6)
        d[2][0] = random.randint(1,6)
        d[3][0] = random.randint(1,6)
        d[4][0] = random.randint(1,6)
        d[5][0] = random.randint(1,6)
    else:
        index = 1
        while index <= 6:
            if index not in keep and d[index-1][1] == (roll - 1):
                d[index-1][0] = random.randint(1,6)
                d[index-1][1] = roll
            index += 1
    return d

def keepDie(roll):
    keep = list()
    if roll >= 10000:
        keep.append(int(roll / 10000))
        roll -= (keep[0] * 10000)
        keep.append(int(roll / 1000))
        roll -= (keep[1] * 1000)
        keep.append(int(roll / 100))
        roll -= (keep[2] * 100)
        keep.append(int(roll / 10))
        roll -= (keep[3] * 10)
        keep.append(roll)
    elif roll >= 1000:
        keep.append(int(roll / 1000))
        roll -= (keep[0] * 1000)
        keep.append(int(roll / 100))
        roll -= (keep[1] * 100)
        keep.append(int(roll / 10))
        roll -= (keep[2] * 10)
        keep.append(roll)
    elif roll >= 100:
        keep.append(int(roll / 100))
        roll -= (keep[0] * 100)
        keep.append(int(roll / 10))
        roll -= (keep[1] * 10)
        keep.append(roll)
    elif roll >= 10:
        keep.append(int(roll / 10))
        roll -= (keep[0] * 10)
        keep.append(roll)
    elif roll >= 1:
        keep.append(roll)
    return keep


   

def main():
    numRoll = 0
    keep = list()
    d = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]   
    d = roll(d, numRoll, keep)
    printTable(d)
    if farkle(d, numRoll):
        return

    total = int(input("Which die do you want to keep (press 7 to reroll, 0 to quit): "))
    if  total > 0:
        keep = keepDie(total)

    while total is not 0 and not farkle(d, numRoll):   
        if len(keep) > 0:
            numRoll += 1
            roll(d, numRoll, keep)
            printTable(d)

        total = int(input("Which die do you want to keep (press 7 to reroll, 0 to quit): "))
        if  total > 0 and total is not 7:
            keep = keepDie(total)
        elif total == 7:
            d = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            numRoll = 0
            keep.clear()
            d = roll(d, numRoll, keep)
            printTable(d)



if __name__ == "__main__":
    main()