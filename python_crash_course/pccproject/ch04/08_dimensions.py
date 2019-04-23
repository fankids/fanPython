dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print()

# ~ dimensions[0] = 250
# ~ Traceback (most recent call last):
  # ~ File "dimensions.py", line 5, in <module>
    # ~ dimensions[0] = 250
# ~ TypeError: 'tuple' object does not support item assignment

for dimension in dimensions:
    print(dimension)
print()    

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 60)
print("\nModified dimesions:")
for dimension in dimensions:
    print(dimension)
print()
