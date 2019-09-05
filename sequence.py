n = int(input("Enter the length of the sequence: ")) # Do not change this line

count_num = 3
num1 = 1
num2 = 2
num3 = 3

while count_num < n:
    if count_num == 3:
        print(num1)
        print(num2)
        print(num3)
    summ = num1 + num2 + num3
    print(summ)
    count_num += 1
    
    num1 = num2
    num2 = num3
    num3 = summ