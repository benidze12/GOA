#5) ცვლადში შეინახეთ სახელი. შემდეგ მომხმარებელსაც შემოატანინეთ თავისი სახელი. თუ თქვენი სახელების პირველი და ბოლო ასო ერთმანეთს დაემთხვევა გამოიტანეთ 2.
#თუ სახელის ან პირველი ან ბოლო ასო დაემთხვევა გამოიტანეთ 1. ყველა სხვა შემთხვევაში: 0.-->
my_name = "Luka"  
user_name = input("Enter your name: ")


first = my_name[0].lower() == user_name[0].lower()
last = my_name[-1].lower() == user_name[-1].lower()

if first and last:
    print(2)
elif first or last:
    print(1)
else:
    print(0)