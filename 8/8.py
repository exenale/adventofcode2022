f = open("8/input.txt", "r")
input_text = f.read()

class Tree():
    def __init__(self, position, height):
        self.position = position
        self.height = height
        self.visible = None
    
    def set_visible(self):
        self.visible = True

    def check_height_in_row_1(self, tree_grid):       
        x, y = self.position 
        i = x-1
        while i >= 0:
            # print(i)
            # print(tree_grid[i][y].height, self.height)
            if tree_grid[i][y].height >= self.height:
                return i
            i = i-1
        return i

    def check_height_in_row_2(self, tree_grid):    
        x, y = self.position    
        i = x+1
        column_num = (len(tree_grid))
        while i < column_num:
            if tree_grid[i][y].height >= self.height:
                return i
            i = i+1
        return i

    def check_height_in_col_1(self, tree_grid):       
        x, y = self.position 
        i = y-1
        while i >= 0:
            if tree_grid[x][i].height >= self.height:
                return i
            i = i-1
        return i

    def check_height_in_col_2(self, tree_grid):    
        x, y = self.position    
        i = y+1
        row_num =(len(tree_grid[0]))
        while i < row_num:
            if tree_grid[x][i].height >= self.height:
                return i
            i = i+1
        return i


    def check_trees_in_row(self, tree_grid):
        x, y = self.position
        column_num = (len(tree_grid))
        row_num =(len(tree_grid[0]))
        if x == 0 or x == column_num-1:
            self.visible = True
            return

        if y == 0 or y == row_num-1:
            self.visible = True
            return

        if self.check_height_in_row_1(tree_grid) < 0 or self.check_height_in_row_2(tree_grid) == column_num:
            self.visible = True
            return
        
        if self.check_height_in_col_1(tree_grid) < 0 or self.check_height_in_col_2(tree_grid) == row_num:
            self.visible = True
            return
        

        self.visible = False
        return

    def find_scenic_score(self, tree_grid):
        x, y = self.position
        column_num = (len(tree_grid))
        row_num =(len(tree_grid[0]))
        scene_range = []
        i = x
        self.scenic_score = self.check_vis_in_row_1(tree_grid) * self.check_vis_in_row_2(tree_grid) * self.check_vis_in_col_1(tree_grid) * self.check_vis_in_col_2(tree_grid)


    def check_vis_in_row_1(self, tree_grid):       
        x, y = self.position 
        i = x-1
        count_tree = 0
        while i >= 0:
            if tree_grid[i][y].height >= self.height:
                count_tree += 1
                return count_tree
            i = i-1
            count_tree += 1
        return count_tree

    def check_vis_in_row_2(self, tree_grid):    
        x, y = self.position    
        i = x+1
        column_num = (len(tree_grid))
        count_tree = 0
        while i < column_num:
            if tree_grid[i][y].height >= self.height:
                count_tree += 1
                return count_tree
            i = i+1
            count_tree += 1
        return count_tree

    def check_vis_in_col_1(self, tree_grid):       
        x, y = self.position 
        i = y-1
        count_tree = 0
        while i >= 0:
            if tree_grid[x][i].height >= self.height:
                count_tree += 1
                return count_tree
            i = i-1
            count_tree += 1
        return count_tree

    def check_vis_in_col_2(self, tree_grid):    
        x, y = self.position    
        i = y+1
        row_num =(len(tree_grid[0]))
        count_tree = 0
        while i < row_num:
            if tree_grid[x][i].height >= self.height:
                count_tree += 1
                return count_tree
            i = i+1
            count_tree += 1
        return count_tree


tree_grid = {}
for idx, line in enumerate(input_text.splitlines()):
    tree_grid[idx] = {}
    for idx2, chr in enumerate(line):
        new_tree = Tree([idx, idx2], int(chr))
        tree_grid[idx][idx2] = (new_tree)

column_num = (len(tree_grid))
row_num =(len(tree_grid[0]))





# print(tree_grid[3][2].position, tree_grid[3][2].height)
# tree_grid[3][2].check_trees_in_row(tree_grid)
# print(tree_grid[3][2].visible)

# print(tree_grid[2][3].position, tree_grid[2][3].height)
# tree_grid[2][3].check_trees_in_row(tree_grid)
# print(tree_grid[2][3].visible)

# print(tree_grid[2][1].position, tree_grid[2][1].height)
# tree_grid[2][1].check_trees_in_row(tree_grid)
# print(tree_grid[2][1].visible)


# print(tree_grid[3][2].position, tree_grid[3][2].height)
# tree_grid[3][2].find_scenic_score(tree_grid)
# print(tree_grid[3][2].scenic_score)

def count_vis_trees(tree_grid):
    for tree_row in tree_grid.keys():
        for tree_col in tree_grid[tree_row]:
            tree_grid[tree_row][tree_col].check_trees_in_row(tree_grid)
            tree_grid[tree_row][tree_col].find_scenic_score(tree_grid)
    count_visible_trees=0
    top_scenic_score = 0
    for tree_row in tree_grid.keys():
        for tree_col in tree_grid[tree_row]:
            # print(tree_grid[tree_row][tree_col].position, tree_grid[tree_row][tree_col].visible)
            if tree_grid[tree_row][tree_col].visible:
                count_visible_trees +=1
            if tree_grid[tree_row][tree_col].scenic_score > top_scenic_score:
                top_scenic_score = tree_grid[tree_row][tree_col].scenic_score

    print("Visible trees: ", count_visible_trees)
    print("Top scenic score: ", top_scenic_score)

def print_vis_graph(tree_grid):
    for tree_row in tree_grid.keys():
        line = ''
        for tree_col in tree_grid[tree_row]:
            
            if tree_grid[tree_row][tree_col].visible:
                line +='v'
            else:
                line +='x'
        print(line)

def print_scenic_score_graph(tree_grid):
    for tree_row in tree_grid.keys():
        line = ''
        for tree_col in tree_grid[tree_row]:
            
            line +=str(tree_grid[tree_row][tree_col].scenic_score)+" "

        print(line)


def print_tree_grid(tree_grid):
    for tree_row in tree_grid.keys():
        line = ''
        for tree_col in tree_grid[tree_row]:
            

            line +=str(tree_grid[tree_row][tree_col].height)

        print(line)

count_vis_trees(tree_grid)
# print_scenic_score_graph(tree_grid)

