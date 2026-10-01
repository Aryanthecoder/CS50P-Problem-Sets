import emoji
code = input("Input: ").strip()
result = emoji.emojize(code, language="alias")
if result == code:
    print("Not found")
else:
    print(result)
