text = "ეს არის ტექსტი"
result = text.split()
print(result)  


text = "ვაშლი,მსხალი,ბანანი"
result = text.split(",")
print(result)  # ['ვაშლი', 'მსხალი', 'ბანანი']

text = "ხაზი1\nხაზი2\nხაზი3"
result = text.split("\n")
print(result)  # ['ხაზი1', 'ხაზი2', 'ხაზი3']


text = "ერთი ორი სამი ოთხი"
result = text.split(" ", 2)
print(result)  # ['ერთი', 'ორი', 'სამი ოთხი']

text = "www.example.com"
result = text.split(".")
print(result)  # ['www', 'example', 'com']
