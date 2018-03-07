window_width = 500
window_height = 500

border_width = 20
border_height = 20

number_of_squares = (50, 50)
all_squares = number_of_squares[0]*number_of_squares[1]
square_width = int((window_width-2*border_width)/number_of_squares[0])
square_height = int((window_height-2*border_height)/number_of_squares[1])
square_field_width = number_of_squares[0]*square_width
square_field_height = number_of_squares[1]*square_height

sleep_delay = 0
