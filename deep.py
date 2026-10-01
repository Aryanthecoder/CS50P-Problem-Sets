answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

answer = answer.strip().lower().replace("-","")

valid_answers = ["42", "fortytwo", "forty two"]

if answer in valid_answers:
    print("Yes")
else:
    print("No")
