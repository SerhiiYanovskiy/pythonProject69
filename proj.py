elems = "Shakespeares profitable fashionable crediability"
vowels = ["a", "e", "i", "o", "u"]
vowel = [x for x in elems.split(" ")]
print([x[0] for x in [[bukva for x in vowel if bukva in x] for bukva in vowels] if len(x) == len(vowel)])
a = [x for x in [[bukva in x for x in vowel] for bukva in vowels]]
a = [vowels[a.index(x)] for x in a if False in x]
count = [x for x in vowels if elems.count(x) > 2]
count2 = [x for x in vowels if elems.count(x) == 1]
print(count2)

