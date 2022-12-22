f = open("12/example.txt", "r")
input_text = f.read()

lines = input_text.splitlines()

length = len(lines[0])
height = len(lines)

print(length, height)