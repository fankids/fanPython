favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}
print(favorite_languages)
print("Sarah's favorite language is " + 
    favorite_languages['sarah'].title() + ".")
print()

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")
print()

for name in favorite_languages.keys():
    print(name.title())
print()

for name in favorite_languages:
    print(name.title())
print()

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())
    if name in friends:
        print("  Hi " + name.title() + ", I see your favorite language is " +
            favorite_languages[name].title() + "!")
print()

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
print()
    
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")
print()

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print()

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())
print()


