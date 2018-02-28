from appJar import gui

# initialize variables
total = 0
backup = 0
app = gui("Python Counter", "300x100")

# define functions
def count(num):
	global total
	global backup
	global app
	backup = total
	if num == "+1":
		total += 1
	elif num == "+2":
		total += 2
	elif num == "+5":
		total += 5
	app.setLabel("total", "Total: " + str(total))

def undo(btn):
	global total
	global backup
	global app
	total = backup
	app.setLabel("total", "Total: " + str(total))


# initialize GUI
app.setFont(18)
app.setSticky("news")
app.setExpand("both")
app.addLabel("total", "Total: 0", 0, 0, 3)
app.setLabelBg("total", "black")
app.setLabelFg("total", "orange")
app.addButton("+1", count, 1, 0)
app.addButton("+2", count, 1, 1)
app.addButton("+5", count, 1, 2)
app.addButton("Undo", undo, 2, 0, 3)
app.setLabelFg("total", "red")

# start the GUI
app.go()