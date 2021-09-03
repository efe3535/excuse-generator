from random import choice

excuses = [
    [ "I was ", "My neighbor was ", "We were ", "My mom was " ],
    [ "washing my ", "eating a ", "damaging a ", "praying to a " ],
    [ "car.", "cat.", "couch.", "door." ]
]

# A funny list, you can create a pull request to add something :]

generated_excuse = []

for choice_first in excuses:
    generated_excuse.append(choice(choice_first))

print("".join(generated_excuse))