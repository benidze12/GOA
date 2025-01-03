#4) შექმენი ცვლადი birthyear და მომხმარებელს შემოატანინე დაბადების წელი, შემდეგ შექმენი მეორე ცვლადი date და შემოიტანოს მომხმარებელმა რომელი წელია, შემდეგ date-ს გამოაკელით birthyear, და გაიგებთ მომხმარებლის ასაკს. 
birthyear = int(input("sheiyvanet dabdebis weli: "))
date = int(input("sheiyvanet romeli welia: "))

age = date - birthyear
print("momxmareblis asaki aris: {age} weli")