# sudoku problem
from random import randint as rand
board = [[["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]],
         [["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]],
         [["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]],
          [["","",""],["","",""],["","",""]]]
#error count

#functions
def check_row(row,cseg,cplace,number):
    row_found = False
    for i in range(9):
        if row != i:
            #print board[i][cseg][cplace], number , board[i][cseg][cplace] == number
            if board[i][cseg][cplace] == number:
                row_found = True
                #row_error += 1
    return not row_found
def check_column(row,cseg,cplace,number):
    column_found = False
    for i in range(9):
        if (cseg+1)*3+(cplace+1) != i+1:
            #print board[row][i/3][i%3] , number
            if board[row][i/3][i%3] == number:
                column_found = True
    return not column_found

def check_box(row,cseg,cplace,number,debug = False):
    #need to be programmed
    box_found = False
    if row < 3 and cseg == 0:
        #check box 1
        for crow in range(0,3):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][0][ccplace] == number:
                        box_found = True
    elif row < 3 and cseg == 0:
        #check box 2
        for crow in range(0,3):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][1][ccplace] == number:
                        box_found = True
    elif row < 3:
        #check box 3
        for crow in range(0,3):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][2][ccplace] == number:
                        box_found = True
    elif row < 6 and cseg == 1:
        #check box 4
        for crow in range(3,6):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][0][ccplace] == number:
                        box_found = True
    elif row < 6 and cseg == 1:
        #check box 5
        for crow in range(3,6):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][1][ccplace] == number:
                        box_found = True
    elif row < 6:
        #check box 6
        for crow in range(3,6):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][2][ccplace] == number:
                        box_found = True
    elif cseg == 2:
        #check box 7
        for crow in range(6,9):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][0][ccplace] == number:
                        box_found = True
    elif cseg == 2:
        #check box 8
        for crow in range(6,9):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][1][ccplace] == number:
                        box_found = True
    else:
        #check box 9
        for crow in range(6,9):
            for ccplace in range(0,3):
                if (crow,ccplace) != (row,cplace):
                    if debug:
                        print board[crow][0][ccplace],number
                    if board[crow][2][ccplace] == number:
                        box_found = True
    return not box_found
assign = 0
row_error = 0
box_error = 0
column_error = 0
complete_first_stage = False
global numbers_add
numbers_add = 0
def insert(row,cseg,cplace,number,numbers_add,row_error,assign,box_error,column_error):
    if board[row][cseg][cplace] == "":
        if check_row(row,cseg,cplace,number):
            if check_column(row,cseg,cplace,number):
                if check_box(row,cseg,cplace,number):
                    board[row][cseg][cplace] = number
                    numbers_add += 1
                    print "numbers added ",numbers_add
                    return True,numbers_add,row_error,assign,box_error,column_error
                else:
                    box_error += 1
                    return False,numbers_add,row_error,assign,box_error,column_error
            else:
                column_error += 1
                return False,numbers_add,row_error,assign,box_error,column_error
        else:
            row_error += 1
            return False,numbers_add,row_error,assign,box_error,column_error
    else:
        assign += 1
        return False,numbers_add,row_error,assign,box_error,column_error
# first stage add some random number into the sudoku
while complete_first_stage == False:
    complete_first_stage = True
    for line in board:
        for segment in line:
            for value in segment:
                if value == "":
                    complete_first_stage = False
    if numbers_add > 60:
        complete_first_stage = True
    row = rand(0,8)
    column = rand(0,8)
    rseg = row / 3
    rplace = row % 3
    cseg = column / 3
    cplace = column % 3
    #print board[row][cseg][cplace]
    number = rand(0,8)
    val,numbers_add,row_error,assign,box_error,column_error = insert(row,cseg,
                                                                     cplace,number,
                                                                     numbers_add,
                                                                     row_error,
                                                                     assign,
                                                                     box_error,
                                                                     column_error)
    #print row_error

NSE = False
for row in range(9):
    for cseg in range(3):
        for cplace in range(3):
            inserted = False
            for i in range(9):
                if not inserted:
                    inserted,numbers_add,row_error,assign,box_error,column_error = insert(row,cseg,
                                                                     cplace,number,
                                                                     numbers_add,
                                                                     row_error,
                                                                     assign,
                                                                     box_error,
                                                                     column_error)
            if not inserted:
                 NSE = True
        if NSE:
            break
    if NSE:
        break
    
        


for item in board:
    print item
print assign , "assignment errors"
print row_error , "row errors"
print column_error, "column errors"
print box_error, "box errors"
