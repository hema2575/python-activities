x = 1
y = 10
if x == 1:
    print(f"{x} is equal to 1")

if y != 1:
    print(f"{y} is not equal to 1")
    
if x < y:
    print(f"{x} is not less than {y}")

if y > x:
    print(f"{y} is greater than {x} ")
    
if x >= 1:
    print(f"{x} is greater than or equal to 1")

if x == 1 and y == 10:
    print(f"{x} is equal to 1 and {y} is equal to 10")
    
if x < 45 or y < 5:
    print(f"One or more statements were true")

if x < 10:
    if y < 5:
        print (f"{x} is less than 10 and {y} is not less than 5")
    elif y == 5:
        print (f"{x} is less than 10 but {y} is equal to 5")
    else:
        print(f"{x} is less than 10 and {y} is greater than 5")