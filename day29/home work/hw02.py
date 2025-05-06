#2) შექმენით ფუნქცია რომელიც მიიღებს სახელებით სავსე სიას შემდეგ კი დააბრუნეთ ყველა ის სახელი რომელიც შედგება მხოლოდ 4 ასოსგან

def four_letter_names(names):
    return [name for name in names if len(name) == 4]

name_list = ["გიორგი", "ანა", "ლაშა", "მარი", "ბექა"]
print(four_letter_names(name_list))  
