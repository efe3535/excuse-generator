from random import choice

excuses = [
    [ "I was ", "My neighbor was ", "We were ", "My mom was ", "My sister was ", "My brother was ", "My girlfriend was ", "My boyfriend was ", "My uncle was " ],
    [ "washing my ", "eating a ", "damaging a ", "praying to a ", "riding a ", "making a ", "going through a portal with a ", "invading America for a ", "forgot everything because of a ", "giving birth to " ],
    [ "car.", "cat.", "couch.", "door.", "television.", "computer case.", "carpet", "grenade.", "soldier.", "lettuce.", "my cousin." ]
]

# A funny list, you can create a pull request to add something :]

generated_excuse = []

for choice_first in excuses:
    generated_excuse.append(choice(choice_first))

print("".join(generated_excuse))
