#3) შექმენით ფუნქცია რომელიც მიიღებს რიცხვებით სავსე სიას შემდეგ კი გამოიტანეთ ისეთი რიცხვები რომლებიც იყოფა 3'ზეც და 5'ზეც

def divisible_by_3_and_5(numbers):
    return [num for num in numbers if num % 3 == 0 and num % 5 == 0]

num_list = [3, 5, 10, 15, 20, 30, 45]
print(divisible_by_3_and_5(num_list))  
