from appJar import gui

# initialize variables
total = 0
backup = 0
app = gui("Python Counter", "400x200")

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

def customCount(num):
	global total
	global backup
	global app
	try:
		value = int(app.getEntry("n="))
	except TypeError:
		return
	backup = total
	total += value
	app.setLabel("total", "Total: " + str(total))

# initialize GUI
app.setFont(18)
app.setSticky("news")
app.setExpand("both")
app.addLabel("total", "Total: 0", 0, 0, 4)
app.setLabelBg("total", "black")
app.setLabelFg("total", "orange")


app.addLabelNumericEntry("n=", 1, 0, 4)
app.setEntryDefault("n=", "0")

app.addButton("+1", count, 2, 0)
app.addButton("+2", count, 2, 1)
app.addButton("+5", count, 2, 2)
app.addButton("+n", customCount, 2, 3)

app.addButton("Undo", undo, 3, 0, 4)
app.setLabelFg("total", "red")

# start the GUI
app.go()