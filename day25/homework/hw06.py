#BOSS Level: 
#🔥 დაწერე ფუნქცია, რომელიც მიიღებს ტექსტს, დააბრუნებს ყველა სიტყვის სიგრძეს და დაამატებს მას "სიგრძე" თითოეულ სიტყვას.
#📌 მაგ: word_lengths("hello world python") → ['hello 5', 'world 5', 'python 6']
#📝 დეტალები:
#ტექსტი უნდა გაიყოს სიტყვებად.
#თითოეულ სიტყვას უნდა დაემატოს მისი სიგრძე.
#(არ არის აუცილებელი ამ დავალების შესრულება თუ შეძლებთ გააკეთეთ)

def word_lengths(text):
    words = text.split()
    return [f"{word} {len(word)}" for word in words]
print(word_lengths("hello world python"))
