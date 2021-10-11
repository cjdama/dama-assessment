sum= 0

try:
    e_input = int(input('Enter integer: '))
    if e_input > 5:
        for i in range(1,e_input):
            if not i % 3 or not i % 5:
                sum += i
                print(i, end= ' ')
        print("Total:",sum)
    else:
        print("Invalid")

except ValueError:
     print("No valid integer! Please try again ...")
