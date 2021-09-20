firstNo = int(input("Enter you first operand: "))
operator = input("Enter your operator: ")
secondNo = int(input("Enter your second operand: "))

if operator == "+":
    print(firstNo + secondNo )
elif operator == "-":
    print(firstNo - secondNo)
elif operator == "*":
    print(firstNo * secondNo)
elif operator == "/":
    print(firstNo / secondNo)
else:
    print("Your operator is a wrong one!")



