#5)შექმენით ფუნქცია, რომელსაც გადაეცემა წინადადება (მაგ: "hello how are you") და შედეგად აბრუნებს სიას,
#სადაც იქნება მოცემული თითოეული სიტყვა და გვერძე ეწერება მისი სიგრძე (["hello 5", "how 3", "are 3", "you 3"]

def word_lengths(sentence):
    words = sentence.split()  
    result = []  
    for word in words:
        result.append(f"{word} {len(word)}")  
    return result
print(word_lengths("hello how are you"))
