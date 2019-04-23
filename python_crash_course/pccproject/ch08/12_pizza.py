def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

    # ~ toppings[0] = 'hhhh'
# ~ Traceback (most recent call last):
  # ~ File "12_pizza.py", line 11, in <module>
    # ~ make_pizza('pepperoni')
  # ~ File "12_pizza.py", line 4, in make_pizza
    # ~ toppings[0] = 'hhhh'
# ~ TypeError: 'tuple' object does not support item assignment

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
