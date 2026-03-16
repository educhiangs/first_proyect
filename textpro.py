def text_maker(phrase):
    question = ("how", "what", "why")
    capitalized_phrase = phrase.capitalize()
    if phrase.startswith(question):
        return "{}?.".format(capitalized_phrase)
    else:
        return "{}.".format(capitalized_phrase)

# print(text_maker("how are you"))
results = []
while True:
    user_input = input("Say something: ")
    if user_input == "\\end":
        break
    else:
        results.append(text_maker(user_input))
print(" ".join(results))