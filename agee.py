q = input("Do you agree? : ")

if q.lower() in ["y", "yes"]:
    print("Agreed!")
elif q.lower() in ["n", "no"]:
    print("Not Agreed!")
else :
    print("Please write Yes or No!")