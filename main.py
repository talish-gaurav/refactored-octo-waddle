
try:
    num = int(input("Enter your age"))
    if num>0:
     print("ERROR! ENTER A POSITIVE NUMBER!")
except ValueError:
    print("ENTER A NUMBER")
except SyntaxError:
    print("ENTER A NUMBER")
else:
    print("Code completed")
