f = open("7/input.txt", "r")
input_text = f.read()

dir_list={}
dir_example = {
    "name": "/",
    "child_dirs": [],
    "files": [
        {"name": "a",
        "size": 12}
    ]

}

def create_dir(command):
    if command == "..":
        pass

def find_parent(current_dir):
    for dirs in dir_list.keys():
        if current_dir in dir_list[dirs]["child_dirs"]:
            return dirs
    return ''

def find_dir(command, dir_path):
    dir_command = command.removeprefix("$ cd").strip()
    if dir_command == "..":
        dir_path = dir_path[0:len(dir_path)-1]
    
        return find_parent(dir_command), dir_path
    else:
        dir_path.append(dir_command)
        dir_path_name = '-'.join(dir_path)
        if dir_path_name not in dir_list.keys():
            dir_list[dir_path_name]={
                "name": dir_command,
                "child_dirs": [],
                "files": [],
                "parent_dir": find_parent(dir_command),
                "dir_path": dir_path.copy(),
            }
        return dir_command, dir_path

def collect_children_dirs(dir_name):
    children_dirs = dir_list[dir_name]["child_dirs"].copy()
    dir_length = len(children_dirs)
    for dir in children_dirs:
        pass


def add_dir_info(current_dir, line):
    split_line = line.split()
    if split_line[0] == "dir":
        dir_list[current_dir]["child_dirs"].append(split_line[1])
    elif split_line[0].isnumeric():
        dir_list[current_dir]["files"].append({
            "name": split_line[1],
            "size": split_line[0],
        })

dir_path = []
for line in input_text.splitlines():
    dir = None
    if "$ cd" in line:
        current_dir, dir_path  = find_dir(line, dir_path)
    
    if "$ ls" in line:
        continue
    else:
        add_dir_info('-'.join(dir_path), line)

def find_total_size(dir_name):
    all_dirs = []
    for check_dir in dir_list.keys():
        if dir_name in dir_list[check_dir]['dir_path']:
            all_dirs.append(check_dir)
    total_size=0
    all_files = []
    for dir in all_dirs:
        all_files.extend(dir_list[dir]["files"])
    for files in all_files:
        total_size += int(files["size"])
    return total_size


def get_files(dir_name):
    all_files = dir_list[dir_name]["files"].copy()
    for child_dir in dir_list[dir_name]["child_dirs"]:
        child_files = get_files(child_dir).copy()
        all_files.extend(child_files)

    return all_files

def get_all_files_dir(dir_name):
    file_list = []
    for dir in dir_list.keys():
        # print(dir[0:len(dir_name)])
        if dir_name in dir[0:len(dir_name)]:
            file_list.extend(dir_list[dir]["files"])
    total_size = 0
    # print(file_list)
    for file in file_list:
        total_size += int(file["size"])
    return total_size


# print(dir_list)
# print(get_all_files_dir("/-a"))
# print(find_total_size("a"))
total_size =0 
for dir_name in dir_list.keys():
    # print(dir_name)
    # print(get_all_files_dir(dir_name))
    if get_all_files_dir(dir_name) <= 100000:
        total_size += get_all_files_dir(dir_name)
print(total_size)

#answer two
amt_free = 70000000 - get_all_files_dir("/")
amt_needed = 30000000 - amt_free
collect_possible_dirs = []
for dir_name in dir_list.keys():
    if get_all_files_dir(dir_name) >= amt_needed:
        collect_possible_dirs.append({"name": dir_name, "total_size": get_all_files_dir(dir_name)})

min=None
min_name = None
for dir in collect_possible_dirs:
    if min==None or dir["total_size"]<= min:
        min = dir["total_size"]
print(min)