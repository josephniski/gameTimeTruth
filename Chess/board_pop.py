# last_board = 
# 	{a1:"R", b1:"N", c1:"B", d1:"Q", e1:"K", f1:"B", g1:"N", h1:"R",
# 	 a}

# curr_board = 
# {}
#columns are letters, rows are numbers
def initialize_base_board():
	letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
	last_board = dict()
	for row in range(1, 9, 1):
		for col in letters:
			spot = col+str(row)
			last_board[spot] = " "
			if (row == 2) or (row == 7):
				last_board[spot] = "p"
			if (row == 1) or (row == 8):
				if (col == "a") or (col == "h"):
					last_board[spot] = "R"
				elif (col == "b")  or (col == "g"):
					last_board[spot] = "N"
				elif (col == "c")  or (col == "f"):
					last_board[spot] = "B"
				elif (col == "d"):
					last_board[spot] = "Q"
				elif (col == "e"):	
					last_board[spot] = "K"

	print(last_board)


initialize_base_board()



#{'a1': 'R', 'b1': 'N', 'c1': 'B', 'd1': 'Q', 'e1': 'K', 'f1': 'B', 'g1': 'N', 'h1': 'R', 
# 'a2': 'p', 'b2': 'p', 'c2': 'p', 'd2': 'p', 'e2': 'p', 'f2': 'p', 'g2': 'p', 'h2': 'p', 
# 'a3': ' ', 'b3': ' ', 'c3': ' ', 'd3': ' ', 'e3': ' ', 'f3': ' ', 'g3': ' ', 'h3': ' ', 
# 'a4': ' ', 'b4': ' ', 'c4': ' ', 'd4': ' ', 'e4': ' ', 'f4': ' ', 'g4': ' ', 'h4': ' ', 
# 'a5': ' ', 'b5': ' ', 'c5': ' ', 'd5': ' ', 'e5': ' ', 'f5': ' ', 'g5': ' ', 'h5': ' ', 
# 'a6': ' ', 'b6': ' ', 'c6': ' ', 'd6': ' ', 'e6': ' ', 'f6': ' ', 'g6': ' ', 'h6': ' ', 
# 'a7': 'p', 'b7': 'p', 'c7': 'p', 'd7': 'p', 'e7': 'p', 'f7': 'p', 'g7': 'p', 'h7': 'p', 
# 'a8': 'R', 'b8': 'N', 'c8': 'B', 'd8': 'Q', 'e8': 'K', 'f8': 'B', 'g8': 'N', 'h8': 'R'}
