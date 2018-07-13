word = "ThiS is String with Upper and lower case Letters"

word_lower = word.lower()

list_alpha = list(word_lower)

dict_alpha = {}

for item in list_alpha:
    if item != " ":
        count_alpha = list_alpha.count(item)
        dict_alpha[item] = count_alpha

for key, value in sorted(dict_alpha.items()):
    print("{0}:  {1}".format(key, value))