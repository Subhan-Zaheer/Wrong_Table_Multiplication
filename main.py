
import random

def wrongTable_Calculating(num, range1):
    tables = []
    rand = random.randint(1, num)

    for i in range(1, range1 + 1):
        if i == rand:
            tables.append(random.randint((i*num) + 1, (i+1)*num)-1)
            continue

        tables.append(i*num)
    return tables


def correcting_table(correct_table, wrong_table):
    dict1 = dict()
    if correct_table == wrong_table:
        return None
    else:
        for i in range(len(correct_table)):
            if correct_table[i] != wrong_table[i]:
                dict1[i] = wrong_table[i]
                return dict1

if __name__ == '__main__':
    num = int(input("Enter the number of which you want to calculate the table : "))
    range1 = int(input("Enter the range to print the table from 1 to ? : "))
    wrong_table = wrongTable_Calculating(num, range1)
    print(wrong_table)
    correct_table= [x*num for x in range(1, range1 + 1)]
    print(correct_table)
    correction = correcting_table(correct_table, wrong_table)
    for key, val in correction.items():
        print(f"\nhe value in wrong Table is wrong at index \"{key}\" and the value of this index is : \"{val}\"")



