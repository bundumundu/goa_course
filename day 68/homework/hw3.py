#3) შექმენით ფუნქცია რომელსაც გადაეცემა სახელი და შემდეგ დაუბეჭდეთ რამდენი ასოა ამ სახელში

name= input("what is your name?? ")
def name_len(user_name):
    for i in range(len(user_name)):
        return i
    
print(name_len(name))