#3) ცვლადში შეინახეთ თქვენი გვარი. შემდეგ მომხმარებელს შემოატანინეთ გვარი. შეამოწმეთ თქვენი გვარები ემთხვევა თუ არა ერთმანეთს. თუ ემთხვევა ტერმინალში დაუბეჭდეთ - "Our surnames are similar." სხვა შემთხვევაში - "We have different surnames". ეს პროგრამა აუცილებლად Case Insensitive უნდა იყოს.-->

my_surname = "nadiri" 

user_surname = input("Enter your surname: ")


if my_surname.lower() == user_surname.lower():
    print("Our surnames are similar.")
else:
    print("We have different surnames.")