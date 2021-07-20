#Excersize implementing both input() and argv
from sys import argv
script, user_name = argv
#script = argv
#user_name = 12
prompt = '> '

print("Hi %r, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" %user_name)
likes = input(prompt)

print("In what type of accomodation do you live?")
accomodation = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Alright, so you said %r about liking me.\nYou live in %r.\nAnd you have a %r computer." %(likes, accomodation, computer))

#Second way of doing a multiline string for the purpose of readability of the code
print(
'''
Alright, so you said %r about liking me.
You live in %r.
And you have a %r computer.
'''
%(likes, accomodation, computer)
)
