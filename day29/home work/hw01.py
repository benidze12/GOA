#1) შექმენით ფუნქცია რომელიც არგუმენტად მიიღებს სიას შემდეგ კი ამ სიიდან დააბრუნედ მხოლოდ კენტი რიცხვების ჯამი

def sum_odd_numbers(numbers):
    return sum(num for num in numbers if num % 2 != 0) 

my_list = [1, 2, 3, 4, 5, 6, 7]
print(sum_odd_numbers(my_list))  

