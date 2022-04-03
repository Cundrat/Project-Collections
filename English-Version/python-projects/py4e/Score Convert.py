score = input("Enter score: ")
fs = float(score)
if fs >= 1.1:
    print("Error")
elif fs >= 0.9:
    print("A")
elif fs >= 0.8:
    print("B")
elif fs >= 0.7:
    print("C")
elif fs >= 0.6:
    print("D")
elif fs < 0.6:
    print("F")
