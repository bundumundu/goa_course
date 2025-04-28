#შექმენით ორი სია, ერთი ლუწი რიცხვებისთვის მეორე კენტი რიცხვებისთვის, მომხმარებელს შეეკითხეთ რიცხვი, თუ რიცხვი იქნება ლუწი ეს რიცხვი დაამატეთ ლუწი რიცხვებისთვის განკუთვნილ სიაში, თუ იქნება კენტი დაამატეთ კენტებისთვის განკუთვნილ სიაში, საბოლოოდ კი დაბეჭდეთ ორივე ლუწების და კენტების სია



num_1 = int(input("enter first number -> "))
num_2 = int(input("enter second number -> "))
num_3 = int(input("enter third number -> "))

even_list = ["", "", ""]
odd_list = ["", "", ""]


if num_1 % 2 == 0:
    even_list[0] = num_1
else:
    odd_list[0] = num_1



if num_2 % 2 == 0:
    even_list[1] = num_2
else:
    odd_list[1] = num_2



if num_3 % 2 == 0:
    even_list[2] = num_3
else:
    odd_list[2] = num_3


print(even_list)
print(odd_list)