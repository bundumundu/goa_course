# მომხმარებელს შემოატანინეთ რიცხვი, შემდეგ კი დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი და მათ გვერდით მიუწერეთ ლუწია თუ კენტი
number = int(input("enter a number: "))
for i in range(number):
    print(i, "is even" if i % 2 == 0 else "is odd")
