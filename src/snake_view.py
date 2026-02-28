def draw_board(canvas, x1, y1, x2, y2, board, info_mode):

    rows = len(board)
    cols = len(board[0])

    cell_width = (x2 - x1) / cols
    cell_height = (y2 - y1) / rows

    for row in range(rows):
        for col in range(cols):
            value = board[row][col]
            color = get_color(value)

            cell_xstart = x1 + col * cell_width
            cell_ystart = y1 + row * cell_height
            cell_xend = cell_xstart + cell_width
            cell_yend = cell_ystart + cell_height

            canvas.create_rectangle(cell_xstart, cell_ystart, 
            cell_xend, cell_yend, 
            fill=color, outline="gray")
    
            cell_xcoordinate = cell_xstart + (cell_xend - cell_xstart) / 2
            cell_ycoordinate = cell_ystart + (cell_yend - cell_ystart) / 2

            if info_mode == True:
                canvas.create_text(cell_xcoordinate, cell_ycoordinate,
                text = f"{row}, {col} \n{board[row][col]}",
                font='Arial 10')



def get_color(value):
    if value == 0:
        return "white"
    elif value > 0: 
        return "green"
    elif value < 0: 
        return "red"
       

if __name__ == '__main__':
    from uib_inf100_graphics.simple import canvas, display

    test_board = [
        [1, 2, 3, 0, 5, 4,-1,-1, 1, 2, 3],
        [0, 4, 0, 7, 0, 3,-1, 0, 0, 4, 0],
        [0, 5, 0, 8, 1, 2,-1,-1, 0, 5, 0],
        [0, 6, 0, 9, 0, 0, 0,-1, 0, 6, 0],
        [0, 7, 0,10,11,12,-1,-1, 0, 7, 0],
    ]

    draw_board(canvas, 25, 80, 375, 320, test_board, True)
    display(canvas)