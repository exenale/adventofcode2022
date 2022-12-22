f = open("5/example.txt", "r")
end_of_graph = 4


f = open("5/input.txt", "r")
end_of_graph = 9

input_text = f.read()
box_dict = {}

lines = input_text.splitlines()
for idx, columns in enumerate(lines[end_of_graph-1].split()):
    name_of_column = columns
    contents_from_top = []
    for line in lines[0:end_of_graph-1]:
        box = line[(idx)*4:((idx)*4)+4]
        if box.strip():
            contents_from_top.append(box.strip())
    box_dict[name_of_column] = contents_from_top
print(box_dict)


# sol 1
def move_box(from_col, to_col, number_of_times):
    for i in range(0,int(number_of_times)):
        moving_box = from_col[0]
        to_col.insert(0, moving_box)
        from_col.pop(0)

#sol 2
def move_boxes(from_col, to_col, number_of_times):
    number_of_times = int(number_of_times)
    moving_boxes = from_col[0:number_of_times]
    to_col[:0] = moving_boxes
    del from_col[0:number_of_times]

for line in lines[end_of_graph+1:len(lines)]:
    words = line.split()
    num_arr = []
    for word in words:
        if word.isnumeric():
            num_arr.append(word)
    move_boxes(box_dict[num_arr[1]], box_dict[num_arr[2]], num_arr[0])

for key in box_dict.keys():
    print(box_dict[key][0])
