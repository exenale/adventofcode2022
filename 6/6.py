f = open("6/input.txt", "r")
input_text = f.read()

def find_start_code_pos(input_text, marker_length):
    for i in range(len(input_text)-marker_length):
        check_slice = input_text[i:i+marker_length]
        if len(set(check_slice)) == marker_length:
            return i+marker_length
    return -1

#sol 1
print(find_start_code_pos(input_text,4))

#sol 2
print(find_start_code_pos(input_text, 14))