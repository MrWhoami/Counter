from appJar import gui

# initialize variables
total = 0
backup = 0
app = gui("Python Counter", "400x200")

# define functions
def count(num):
	"""Basic count function +1, +2, +5"""
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
	"""Undo the last count"""
	global total
	global backup
	global app
	total = backup
	app.setLabel("total", "Total: " + str(total))

def customCount(num):
	"""Count with customized value"""
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

def keyPress(key):
	"""Key binding"""
	global total
	global backup
	global app
	
	if key == "<z>":
		backup = total
		total += 1
	elif key == "<x>":
		backup = total
		total += 2
	elif key == "<c>":
		backup = total
		total += 5
	elif key == "<space>":
		try:
			value = int(app.getEntry("n="))
		except TypeError:
			return
		backup = total
		total += value
	app.setLabel("total", "Total: " + str(total))

def showHelp(name):
	"""Show a pop-up help window"""
	global app
	app.infoBox("Help and About", """Counter
A counter you can define your step. Developed by Jiyuan Liu.

Shortcuts:
    z: +1
    x: +2
    c: +3
space: +n""")

def waitDev(name):
	global app
	app.infoBox("Oops", name + " is still under construction")


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

# bind keys
app.bindKey("<space>", keyPress)
app.bindKey("<z>", keyPress)
app.bindKey("<x>", keyPress)
app.bindKey("<c>", keyPress)

# add tool bar
tools = ["REFRESH", "OPEN", "SAVE", "HELP"]
tbFunc = [waitDev, waitDev, waitDev, showHelp]
app.addToolbar(tools, tbFunc, findIcon=True)

# start the GUI
app.go()