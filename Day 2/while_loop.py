# count = 0
# while count < 5:
#     name =input("Enter your name")
#     print(name + "Is awesome")
#     count += 1


word = str(input("Please type a word: "))
vcount = 0
for char in word:
    if char in("a","e","i","o", "u"):
        vcount += 1
print("Number of vowels:", vcount)