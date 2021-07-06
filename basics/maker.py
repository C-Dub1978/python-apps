def check_sentence(str):
    leadingWords = ("how", "why", "where")
    capitalized = str.capitalize()
    if str.startswith(leadingWords):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []

while True:
    i = input("Enter a phrase, or enter \end to end the program: ")
    if i == "\end":
        break
    else:
        results.append(check_sentence(i))

print(" ".join(results))
