# ask user if they want a top or a bottom color selection
# input what color they watn from our given list
# return color combos for that chosen color



top_or_bottom = input("would you like a top or a bottom: ")

if top_or_bottom == "top":
	color_top = input("Choose a color: red, green, white, black, blue, purple, orange: ")
	if color_top == "red":
		weather = input("is it cold or hot: ")
		if weather == "cold":
			print("use black pants: ")
		elif weather == "hot":
			print("use red shorts")
		else:
			print("please choose the weather situation")



""""
elif top_or_bottom == "bottom":
	color_top = input("What color is your bottom: yellow,red,orange,blue,purple,green,white,black: ")
else:
		print("what nonsense is this")
"""
