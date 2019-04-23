magicians = ['alice', 'david', 'caroliana']
for magician in magicians:
# ~ print(magician)
  # ~ File "magicians.py", line 3
    # ~ print(magician)
        # ~ ^
# ~ IndentationError: expected an indented block

    # ~ print(magician)
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see you next trick, " + magician.title() + ".\n")
    
print("Thank you, everyone. That was a great magic show!")

# ~ for magician in magicians
    # ~ print(magician)

  # ~ File "magicians.py", line 15
    # ~ for magician in magicians
                            # ~ ^
# ~ SyntaxError: invalid syntax
