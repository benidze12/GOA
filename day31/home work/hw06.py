#BOSS LEVEL
#Input() ის საშუალებით რამდენიმე მომხმარებელს შემოატანინეთ სახელი. ცვლადებში შეინახეთ მათ მიერ შემოტანილი სახელების Capitalized ვერსია.
#  შექმენით names სია, რომელიც თავდაპირველად იქნება ცარიელი და თქვენი დავალება იქნება თითოეული სახელის შემოტანაზე დაამატოთ ეს სახელები სიაში, სიის თითოეულ განახლებაზე დაბეჭდეთ სია.

names = [] 
number_of_users = int(input("How many users will enter their name? "))
for i in range(number_of_users):
    name = input(f"Enter name #{i+1}: ")
    capitalized_name = name.capitalize() 
    names.append(capitalized_name)  
    print("Updated list:", names)  