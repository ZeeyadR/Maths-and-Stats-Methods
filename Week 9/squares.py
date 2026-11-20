while True:
    try:
        n = int(input("Please enter a positive number"))
        if n > 0:
            break
        else:
            print("A positive number wasn't entered.")
    except ValueError:
        print("No number was entered")

i = 0
while i**2<=n:
    if i % 2 == 0:
        print(i**2)
    i = i + 1
