camel= input("Camelcase:")
snake=""
for character in camel:
    if character.isupper() :
        snake= snake + "_" +character.lower()
    else:
        snake=snake+character
print("snake_case:", snake)
