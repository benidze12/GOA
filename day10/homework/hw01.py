#მომხმარებელს უნდა შეყვანოს თავისი სახელი და ასაკი, შემდეგ კი გამოსახოს შეტყობინება ფორმატით: გამარჯობა, [სახელი]! შენ ხარ [ასაკი] წლის.

name = input("enter your name: ")
print(name)
age = int(input("enter your age: "))
print(age)
print("გამარჯობა, " + name + "! "+ "შენ ხარ " + str(age) + " წლის")