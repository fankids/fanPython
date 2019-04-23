def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
describe_pet(pet_name='dahuang', animal_type='dog')
describe_pet('dog', pet_name='dahuang')

# ~ describe_pet('dog', animal_type='dog')
# ~ Traceback (most recent call last):
  # ~ File "03_pets.py", line 11, in <module>
    # ~ describe_pet('dog', animal_type='dog')
# ~ TypeError: describe_pet() got multiple values for argument 'animal_type'

# ~ describe_pet(pet_name='dahuang', 'dog')
  # ~ File "03_pets.py", line 17
    # ~ describe_pet(pet_name='dahuang', 'dog')
                                    # ~ ^
# ~ SyntaxError: positional argument follows keyword argument
