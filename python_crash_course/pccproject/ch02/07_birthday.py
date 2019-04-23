age = 23

# ~ message = "Happy " + age + "rd Birthday!"
# ~ Traceback (most recent call last):
  # ~ File "birthday.py", line 2, in <module>
    # ~ message = "Happy " + age + "rd Birthday!"
# ~ TypeError: must be str, not int

message = "Happy " + str(age) + "rd Birthday!"

print(message)
