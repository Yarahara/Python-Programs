__author__ = "Divine Gbagi"
__date__="12/04/2020"
"""This program creates a graphical user
    interface with tkinter
    """
#Ex1 - Basic Window
##from tkinter import *
##mainWin = Tk()
##mainWin.title("Basic Window")
##mainWin.geometry("400x400")
##mainWin.mainloop()

#Ex2 - Labels & Buttons
##from tkinter import Tk, Label, Button
##class Ex2:
##    def __init__(self, master):
##        self.master = master
##        master.title("First GUI")
##        self.label = Label(master,\
##                           text = "Ex2: Labels & Buttons")
##        self.label.pack()
##
##        self.btnGreet = Button(master, text = "Greet", command = self.greet)
##        self.btnGreet.pack()
##
##        self.btnClose = Button(master, text = "Close", command = master.destroy)
##        self.btnClose.pack()
##
##    def greet(self):
##        print("Hello World!")
##
##myWindow = Tk()
##my_gui = Ex2(myWindow)
##myWindow.mainloop()

#Ex3 - More labels & buttons
##from tkinter import Tk, Label, Button
##class Ex3:
##    def __init__(self, master):
##        self.master = master
##        master.title("Ex3: More labels,btns")
##        self.label = Label(
##            text = "Hello World",
##            foreground = "white",
##            background = "red",
##            width = 20,
##            height = 10
##        )
##        self.label.pack()
##        self.btnGreet = Button(
##            text = "Click me!",
##            width = 25,
##            height = 5,
##            bg = "blue",
##            fg = "white",
##            command = self.greet
##            )
##        self.btnGreet.pack()
##
##        self.btnClose = Button(master, text = "Close", command = master.destroy)
##        self.btnClose.pack()
##
##    def greet(self):
##        print("Hello World!")
##
##myWindow = Tk()
##my_gui = Ex3(myWindow)
##myWindow.mainloop()

#Ex4 Button with Image-- NOTE need to go online and find gif!
##from tkinter import *
##def printMsg():
##    print("Hello from Mickey")
##mainWin = Tk(); mainWin.title("Ex Button w/Image"); mainWin.minsize(400,400)
##imgMickey = PhotoImage(file ="MickeyMouse.gif")
##btnOK = Button(mainWin, image = imgMickey, command = printMsg, \
##               height = 400, width = 400)
##btnOK.pack()
##mainWin.mainloop()

#Ex5 User Input
##from tkinter import *
##def printMsg():
##    print("Hello " + firstName.get() + " " + lastName.get())
##
##mainWindow = Tk(); mainWindow.title("Ex5 User Input")
##mainWindow.maxsize(300,300)
##
##lblFirstName = Label(text = "First Name: ");
##lblFirstName.pack()
##firstName = Entry(mainWindow); firstName.pack()
##
##lblLastName = Label(text = "Last Name: ");
##lblLastName.pack()
##lastName = Entry(mainWindow); lastName.pack()
##
##btnOK = Button(mainWindow, text = "Submit")
##command = printMsg(height = 400, width = 400)
##btnOK.pack()
##mainWindow.mainloop()

#Ex6 Grid
##from tkinter import *
##def printMsg():
##    print("Hello from Mickey")
##
##mainWin = Tk(); mainWin.title("Ex Grid")
##Label(mainWin, text = "Student info", relief = RIDGE).grid(row = 0, column = 0)
##Label(mainWin, text = "************").grid(row = 1, column = 0)
##Label(mainWin, text = "Name", relief = RIDGE).grid(row = 2, column = 0)
##Label(mainWin, text = "John Doe", relief = RIDGE).grid(row = 2, column = 1)
##Label(mainWin, text = "Major", relief = RIDGE).grid(row = 3, column = 0)
##Label(mainWin, text = "Chemistry", relief = RIDGE).grid(row = 3, column = 1)
##mainWin.mainloop()

#Ex7 Two Windows
##from tkinter import *
##def showMsgWin():
##    newWin = Toplevel() # create child window
##    newWin.minsize(300, 300); newWin.title("New Window")
##    lblMessage = Label(newWin, text = "New Window"); lblMessage.pack()
##    btnClose = Button(newWin, text = 'Close', command = newWin.destroy)
##    btnClose.pack()
##mainWin = Tk(); mainWin.minsize(500,300); mainWin.title("Main Window")
##btnShow = Button(mainWin, text = "Open New Window", command = showMsgWin)
##btnShow.pack()
##mainWin.mainloop()

#Ex8 ListBox with Scrollbar
##from tkinter import *
##
##mainWin = Tk(); mainWin.geometry("300x130")
##Label(mainWin, text = "Languages").pack()
##frame = Frame(mainWin); frame.pack()
##listBxLang = Listbox(frame)
##listBxLang.insert(1, "Python"); listBxLang.insert(2, "Java")
##listBxLang.insert(3, "C++"); listBxLang.insert(4, "PHP")
##listBxLang.insert(5, "C#"); listBxLang.insert(6, "Swift")
##listBxLang.insert(7, "R"); listBxLang.insert(8, "Ruby")
##listBxLang.pack(side="left", fill="y")
##
##scrollbar = Scrollbar(frame, orient = "vertical")
##scrollbar.config(command = listBxLang.yview)
##scrollbar.pack(side = "right", fill = "y")
##
###listBxLang.pack()
##mainWin.mainloop()

#Ex9 ListBox Show Selected Item
##from tkinter import *
##def get_list(event):
##    index = listbxLang.curselection()[0] #get selected line index
##    selText = listbxLang.get(index) # get the line's text
##    txtSelection.delete(0, 50) #delete previous text
##    txtSelection.insert(0, selText)
##
##mainWin = Tk()
##mainWin.title("Listboc Operations")
### create the listboc (size is in characters)
##listbxLang = Listbox( mainWin, width = 50, height = 6)
##listbxLang.grid(row = 0, column = 0)
##
### Display selected item
##txtSelection = Entry(mainWin, width = 50, bg = 'yellow')
##txtSelection.insert(0, 'Select a language')
##txtSelection.grid(row = 1, column = 0)
##
### populate the listbox
##langList = ["Python", "Java", "C++", "Swift", "C#", "Perl", "Ruby", "R", "SQL"]
##for item in langList:
##    listbxLang.insert(END, item)
##
###click on a list item to display selection
##listbxLang.bind('<ButtonRelease-1>', get_list)
##
##mainWin.mainloop()

#Ex10 Menus
##from tkinter import *
##from tkinter.filedialog import askopenfilename
##def showDialog():
##    infileName = askopenfilename()
##    print("You chose this file: " + infileName)
##
##def showMsgWin():
##    newWin = Toplevel()
##    newWin.minsize(300, 300);
##    message = "This is the new window"
##    lblMsg = Label(newWin, text = message)
##    lblMsg.pack()
##    btnClose = Button(newWin, text = "Close", command = newWin.destroy)
##    btnClose.pack()
##
##def showAbout():
##    aboutWin = Toplevel()
##    aboutWin.title("About the ABC Company")
##    aboutWin.minsize(200,200)
##    tmp = "Mr.Brown\nABC Company\nMoorhead, MN"
##    lblMsg = Label(aboutWin, text = tmp)
##    lblMsg.pack()
##
##def closeApplication():
##    mainWin.destroy()
##    mainWin.quit()

#Ex11 -Form
from tkinter import *
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid(); self._skillList = []
        self.name(); self.major(); self.yrsAttend();
        self.skills(); self.text(); self.submit()

    def name(self):
        self._lblName = Label(self, text = 'Name:');
        self._lblName.grid(row = 0, column = 0, sticky = W)
        self._txtName = Entry(self);
        self._txtName.grid(row = 0, column = 1, sticky = W)

    def major(self):
        self._lblMajor = Label(self, text = 'Major:');
        self._lblMajor.grid(row = 1, column = 0, sticky = W)
        self._txtMajor = Entry(self);
        self._txtMajor.grid(row = 1, column =1, sticky = W)

    def yrsAttend(self):
        self._lblYrs = Label(self, text = 'Yrs attended: ');
        self._lblYrs.grid(row = 2, column = 0, sticky = W)
        self.spinYrs = Spinbox(self, form = 0, to = 10, state = NORMAL);
        self.spinYrs.grid(row = 2, column = 1, sticky = W)

    def skills(self):
        self._powerpoint = BooleanVar();
        self._excel = BooleanVar();
        self._word = BooleanVar()
        self._lblSkills = Label(self, text = 'Check all skills:');
        self._ckbkWord = Checkbutton(self, text = 'Word',\
                                     variable = self._word, onvalue = True, offvalue = False)
        self._ckbxWord.grid(row=4, column=1, sticky = W)

        self._ckbxPwrPt = Checkbutton(self, text = 'Powerpoint', variable = self._powerpint,\
                                      onvalue = True, offvalue = False)
        self._ckbxPwrPt.grid(row =5, column = 1, sticky = W)
        self._ckbxExcel = Checkbutton(self, text = 'Excel', variable = self._excel, onvalue =True,\
                                      offvalue = False)
        self._ckbxExcel.grid(row = 6,column = 1, sticky = W)

    def submit(self):
        self._text = Text(self, width = 40, height = 5);
        self._text.grid(row = 8, column = 0, sticky = W)

    def updateSkillList(self):
        if self._word.get(): self._skillList.append('Word');
        if self._excel.get(): self._skillList.append('Excel')
        if self._powerpoint.get(): self._skillList.append('Powerpoint')

    def showInfo(self):
        formattedString = ''; self._skillList = []
        nameString = self._txtName.get();
        strMajor = 'Major: '+self._txtMajor.get();
        strYrs = 'Years attended:' + str(self.spinYrs.get())
        strSkill=''; self.updateSkillList();
        for skil in self._skillList:
            strSkill += skill+','
        strSkill = strSkill[0:len(strSkill)-2]
        tmp = nameString + '\n' + strMajor +'\n' +strYrs + '\n' + strSkill + '\n'
        self._text.delete(0.0,END);
        self._text.insert(0.0,tmp)

root = Tk(); root.title('Student Information');
app = Application(root);
root.mainloop()
                                      
            

mainWin = Tk()
menuBar = Menu(mainWin)
menuFile = Menu(menuBar, tearoff = 0)
menuFile.add_command(label = "New", command = showMsgWin)
menuFile.add_command(label = "Open", command = showDialog)
menuFile.add_command(label = "Exit", command = closeApplication)

menuBar.add_cascade(label = "File", menu = menuFile)
menuHelp = Menu(menuBar, tearoff = 1)
menuHelp.add_command(label = "About", command = showAbout)
menuBar.add_cascade(label = "Help", menu = menuHelp)

mainWin.config(menu = menuBar)
mainWin.mainloop()



    






































