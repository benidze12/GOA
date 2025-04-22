#4) შექმენით ფუნქცია რომელიც მიიღებს 2 არგუმენტს შემდეგ კი გამოიტანეთ პირველი არგუმენტი რომელიც იქნება upper_case'ში
#  ხოლო მეორე lower_case'ში და დაამეტეთ ეს არგუმენტები ერთმანეთს
 
def combine(world,hello):
    upper_arg1 = world.upper()
    lower_arg2 = hello.lower()
    result = upper_arg1 + lower_arg2
    return result
print(combine("Hello", "WORLD"))