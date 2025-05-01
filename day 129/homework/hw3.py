def clean_and_uppercase(word):
    clean_word = word.replace("%", "")  # ვშლით %
    return clean_word.upper()           # ვაბრუნებთ დიდი ასოებით

# გამოყენება:
input_word = "C%o%d%i%n%g"
result = clean_and_uppercase(input_word)
print(result)  # შედეგი: CODING
