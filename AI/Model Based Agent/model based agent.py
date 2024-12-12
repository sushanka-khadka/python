import random


class Grid:
    def __init__(self,row,col,start_row,start_col,goal_row,goal_col):
        if row >= goal_row and col >= goal_col:
            self.row= row
            self.col=col
            self.goal_row=goal_row
            self.goal_col=goal_col
            self.row_no =start_row
            self.col_no =start_col
            self.grid = [[False for _ in range(col)] for _ in range(row)]

            self.next_row ,self.next_col = 0,0
            # self.grid[0][0] =True
        else:
            print('Object declaration didn\'t go as per plan ')

    def up(self):
        return -1,0
    def down(self):
        return 1,0
    def right(self):
        return 0,1
    def left(self):
        return 0,-1

        #  remarked visited
    def update_model(self):
        # self.row_no ,self.col_no =self.next_row,self.next_col
        self.grid[self.row_no][self.col_no]= True
    def make_goal(self):
        min_distance = self.row + self.col
        next_row,next_col=0,0
        for move in self.down(),self.up(),self.right(),self.left():
            row_no,col_no = self.row_no + move[0], self.col_no + move[1]
            # check for boundary
            if 0<=row_no<self.row and 0<=col_no<self.col:
                distance = abs(row_no - self.goal_row) + abs(col_no - self.goal_col)
            # check for optimum
                if distance < min_distance:
                    next_row, next_col = row_no, col_no
                    min_distance = distance
        self.row_no,self.col_no = next_row, next_col
        self.update_model()


    def way_to_goal(self):
        while self.row_no != self.goal_row or self.col_no != self.goal_col:
            self.make_goal()
            print(f'move to position ({self.row_no},{self.col_no})')
        print("\nReached the goal position!")
        # for _ in self.grid:
        #     print(_)

def main():
    grid_size= 5
    s_row,s_col,g_row,g_col= [random.randint(0,grid_size-1) for i in range(4)]

    # model = Grid(5,5,0,1,4,3)
    # print(model.grid)
    model = Grid(grid_size, grid_size, s_row, s_col, g_row, g_col)
    print('start row:%s start col:%s'%(model.row_no,model.col_no))
    print('goal row:%s goal col:%s\n' % (model.goal_row, model.goal_col))

    model.way_to_goal()
    # print(model.grid)
if __name__ == '__main__':
    main()