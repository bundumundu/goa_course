# 1) Count() ფუნქცია გამოიყენება ელემენტის რაოდენობის დასათვლელად სიაში ან ტექსტში.
# მაგალითად: list.count(x) ითვლის, რამდენჯერ გვხვდება x სიაში.

example_list = ['a', 'b', 'a', 'c']
count_a = example_list.count('a')  # აბრუნებს 2-ს, რადგან 'a' ორჯერ არის სიაში
print("Count of 'a':", count_a)


# 2) sorted() ფუნქცია აბრუნებს დალაგებულ სიას (ახალ ობიექტს), ორიგინალის შეცვლის გარეშე.
# ძირითადად ვიყენებთ list, tuple, set ან string ტიპებზე.

unsorted_list = [3, 1, 4, 2]
sorted_list = sorted(unsorted_list)  # დაალაგებს [1, 2, 3, 4]
print("Sorted list:", sorted_list)


# 3) შეინახეთ ინგლისური ანბანის ასოები არეულად, დაალაგეთ sorted() ფუნქციით

import random
import string

letters = list(string.ascii_lowercase)  # ყველა ასო
random.shuffle(letters)  # არევა
print("Unsorted letters:", letters)

sorted_letters = sorted(letters)
print("Sorted letters:", sorted_letters)


# 4) 15 რიცხვი სიაში არეულად, sorted() ფუნქციით ზრდადობით დალაგება

numbers = [12, 3, 45, 6, 18, 29, 1, 8, 34, 23, 5, 17, 27, 9, 14]
sorted_numbers = sorted(numbers)
print("Sorted numbers (ascending):", sorted_numbers)


# 5) 10 რიცხვი არეულად, sorted() + ინდექსინგი კლებადობით

random_numbers = [7, 2, 9, 4, 1, 8, 3, 6, 5, 10]
descending_sorted = sorted(random_numbers)[::-1]  # ინდექსინგით გადაბრუნება
print("Sorted numbers (descending):", descending_sorted)
