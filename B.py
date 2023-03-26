def generate(token, form):
    # TODO Write here your code
    print(token, form)

def parse(word):
    #TODO Write your code
    return ("word<noun>")

print(generate("ұлар","<plural>")) # ұларлар
print(generate("ұлар","<dative>")) # ұларға
print(parse("ұлар")) # ("ұлар<noun>")
print(parse("қарға")) # ("қар<noun><dative>","қарға<noun>")
print(parse("кемелер")) # ("кеме<noun><plural>")