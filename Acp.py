g = int(input("Enter the Given amount: "))
b = int(input("Enter the Bill amount: "))

def calculateBill(g,b):
    return (g-b)

change = calculateBill(g,b)

print("Here is your Change:",change)