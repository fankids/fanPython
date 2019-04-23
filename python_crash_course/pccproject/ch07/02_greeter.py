name = input("Please enter your name: ")
print("Hello, " + name + "!")
print()

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print("\nHello, " + name + "!")
print()

age = input("How old are you? ")
print(age)
print()

# ~ age >= 18
# ~ Traceback (most recent call last):
  # ~ File "02_greeter.py", line 16, in <module>
    # ~ age >= 18
# ~ TypeError: '>=' not supported between instances of 'str' and 'int

age = int(age)
print(age >= 18)
print()
