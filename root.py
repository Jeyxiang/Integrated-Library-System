from mysqlaccessors import connectTo, executeQuery, readQuery
from nosqlaccessors import queryMongo, distinctMongo
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
connection = connectTo("localhost", "root", "passwordHere", "library")
adminCheckerQueue = (420, "1337", "Mr. Admin")

## 1 LOGIN MENU ##
def destroyLoginMenu():
	loginMenu.destroy()

def LoginToMain():
	mainMenuF()
	destroyLoginMenu()
	mainMenu.lift()
	mainMenu.lift()

def navtoReg(): #navigate from login to register
	regMenuF()
	destroyLoginMenu()
	regMenu.lift()
	regMenu.lift()

def loginMenuF():
	global loginMenu
	loginMenu = Toplevel()
	loginMenu.title("Login Page")
	loginMenu.geometry("1280x720")

	def validateLogin():
		global userstatus
		global userName
		global userNameWord
		try:
			userID = username.get()
			passWord = password.get()
			number = v.get()
			if number == 0:
				status = 'Admin'
			else:
				status = 'Member'

			checkerQueue = []
		except:
			return messagebox.showerror(title="Error",message='Invalid Input')
		if status == "Member":
			validate_query = "SELECT * FROM user WHERE ID = '%d' AND password = '%s' "%(userID,passWord)
			results = readQuery(connection,validate_query)
			for result in results:
				checkerQueue.append(result)
			if len(checkerQueue) == 0:
				return messagebox.showerror(title="Error",message="Wrong username/password !")
			else:
				userstatus = status
				userName = str(userID)
				userNameWord = checkerQueue[0][2]
				return LoginToMain()
		else:
			global adminCheckerQueue
			if adminCheckerQueue[0] == userID and adminCheckerQueue[1] == passWord:
				userstatus = status
				userName = str(userID)
				userNameWord = adminCheckerQueue[2]
				return LoginToMain()
			else:
				return messagebox.showerror(title="Error",message="Wrong username/password or you are not an administrator!")

	topleftheader = Label(loginMenu, text = "BT2102", bg = "lightblue", 
		borderwidth = 2, relief = "solid", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	topbar = Label(loginMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	sidebar = Label(loginMenu, text = "Welcome!", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 620)

	usernameLabel = Label(loginMenu,text = "User ID: ", font = ("Mincho", 20))
	usernameLabel.place(x=500,y=200)
	username = IntVar()
	usernameEntry = Entry(loginMenu,textvariable=username, font = ("Mincho", 20))
	usernameEntry.place(x=700,y=200)
	usernameEntry.delete(0, END)

	passwordLabel = Label(loginMenu,text = "Password: ", font = ("Mincho", 20))
	passwordLabel.place(x=500,y=275)
	password = StringVar()
	passwordEntry = Entry(loginMenu,textvariable=password, show="*", font = ("Mincho", 20))
	passwordEntry.place(x=700,y=275)

	loginAsLabel = Label(loginMenu,text = "Signing in As: ", font = ("Mincho", 20))
	loginAsLabel.place(x = 500, y = 350)
	v = IntVar()
	AdminButton = Radiobutton(loginMenu,text = "Admin",padx = 20,variable = v,value = 0, font = ("Mincho", 20))
	AdminButton.place(x = 675, y = 350)
	MemberButton = Radiobutton(loginMenu,text = "Member",padx = 20,variable = v,value = 1, font = ("Mincho", 20))
	MemberButton.place(x = 825, y = 350)

	loginButton = Button(loginMenu,text="Login",command=validateLogin, font = ("Mincho", 16))
	loginButton.place(x=550, y = 450, width=150,height = 50)

	RegButton = Button(loginMenu,text="Register Account",command=navtoReg, font = ("Mincho", 16))
	RegButton.place(x=725, y = 450, width=200,height = 50)

### 2 REGISTRATION MENU ###
def destroyRegMenu():
	regMenu.destroy()

def backtolog():
	loginMenuF()
	destroyRegMenu()
	loginMenu.lift()
	loginMenu.lift()

def regMenuF():
	global regMenu
	regMenu = Toplevel()
	regMenu.title("Registration Menu")
	regMenu.iconbitmap("nlb.ico")
	regMenu.geometry("1280x720")

	def updateUser():
		try:
			userID = userid.get()
			passWord = password.get()
			userName = username.get()
			checkerQueue = []
		except:
			return messagebox.showerror(title="Error",message='Invalid type/Input')

		if passWord == "":
			return messagebox.showerror(title="Error",message='Invalid Password')

		if userID == 420:
			return messagebox.showerror(title="Error",message='User ID cannot be 420')

		test_query = "SELECT * FROM user WHERE ID = '%d' "%(userID)
		results = readQuery(connection,test_query)
		if len(results) == 0:
			sql_query = "INSERT INTO user VALUES ('%d', '%s','%s')"%(userID,passWord,userName)
			executeQuery(connection, sql_query)
			backtolog()
			return messagebox.showinfo(title='success',message="Registration successful!")
			
		else:
			return messagebox.showerror(title="Error",message='userID Already in use!')


	topleftheader = Label(regMenu, text = "BT2102", bg = "lightblue", 
		borderwidth = 2, relief = "solid", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	topbar = Label(regMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	sidebar = Label(regMenu, text = "Registration", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 620)

	userIDRegLabel = Label(regMenu,text = "New User ID: ", font = ("Mincho", 20))
	userIDRegLabel.place(x=500, y=200)
	userid = IntVar()
	userIDEntry = Entry(regMenu,textvariable=userid, font = ("Mincho", 20))
	userIDEntry.place(x=700, y=200)
	userIDEntry.delete(0, END)

	passwordRegLabel = Label(regMenu,text = "New Password: ", font = ("Mincho", 20))
	passwordRegLabel.place(x=500, y=275)
	password = StringVar()
	pwdEntry = Entry(regMenu,textvariable = password, font = ("Mincho", 20))
	pwdEntry.place(x=700, y=275)

	nameRegLabel = Label(regMenu,text = "New User Name: ", font = ("Mincho", 20))
	nameRegLabel.place(x=500, y=350)
	username = StringVar()
	usernameEntry = Entry(regMenu,textvariable = username, font = ("Mincho", 20))
	usernameEntry.place(x=700, y=350)


	RegButton = Button(regMenu,text="Register!",command=updateUser, font = ("Mincho", 16))
	RegButton.place(x=550, y = 450, width=150,height = 50)

	BacktologButton = Button(regMenu,text='Back to Login',command = backtolog, font = ("Mincho", 16))
	BacktologButton.place(x=725, y = 450, width=200, height = 50)

### 3 MAIN MENU ###
def destroyMainMenu():
	mainMenu.destroy()

def nav3to4():
	borrowMenuF()
	destroyMainMenu()
	borrowMenu.lift()
	borrowMenu.lift()

def nav3to5():
	reserveMenuF()
	destroyMainMenu()
	reserveMenu.lift()
	reserveMenu.lift()

def nav3to6():
	FineMenuF()
	destroyMainMenu()
	FineMenu.lift()
	FineMenu.lift()

def nav3to9():
	searchMenuF()
	destroyMainMenu()
	searchMenu.lift()
	searchMenu.lift()

def nav3to8():
	global userstatus
	if userstatus != "Admin":
		return messagebox.showerror("Access Denied!","You are not an administrator!")
	adminMenuF()
	destroyMainMenu()
	adminMenu.lift()
	adminMenu.lift()

def nav3to10a():
	mySQLBookMenuF()
	destroyMainMenu()
	mySQLBookMenu.lift()
	mySQLBookMenu.lift()

def mainMenuF():
	global mainMenu
	mainMenu = Toplevel()
	mainMenu.title("Main Menu")
	mainMenu.iconbitmap("nlb.ico")
	mainMenu.geometry("1280x720")



	topleftheader = Label(mainMenu, text = "Home", bg = "lightblue", 
		borderwidth = 2, relief = "solid", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(mainMenu, text = "Welcome Back \n" + userNameWord[0:10], bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(mainMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(mainMenu, text = "Log Out", command = destroyMainMenu, fg = "lightblue",
			bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	BorrowButton = Button(mainMenu, text = "Borrowed", command = nav3to4, fg = "black",
			bg = "lightgreen", font = ("Mincho", 30))
	BorrowButton.place(x = 280, y = 100, width = 300,height = 450)

	ReserveButton = Button(mainMenu, text = "Reserved", command = nav3to5, fg = "black",
			bg = "palegoldenrod", font = ("Mincho", 30))
	ReserveButton.place(x = 630, y = 100, width = 300,height = 450)

	FineButton = Button(mainMenu, text = "Fines", command = nav3to6, fg = "black",
			bg = "thistle", font = ("Mincho", 30))
	FineButton.place(x = 980, y = 100, width = 300,height = 450)

	SearchButton = Button(mainMenu, text = "MongoDB \nSearch", command = nav3to9, fg = "black",
			bg = "lavender", font = ("Mincho", 30))
	SearchButton.place(x = 280, y = 550, width = 300, height = 170)

	BookSQLButton = Button(mainMenu, text = "MySQL Books", command = nav3to10a, fg = "black",
			bg = "peachpuff", font = ("Mincho", 30))
	BookSQLButton.place(x = 630, y = 550, width = 300, height = 170)

	if userstatus != "Admin":
		AdminButton = Button(mainMenu, text = "Admin", command = nav3to8, fg = "black",
				bg = "lightblue", font = ("Mincho", 30), state = DISABLED)
	else:
		AdminButton = Button(mainMenu, text = "Admin", command = nav3to8, fg = "black",
				bg = "lightblue", font = ("Mincho", 30))
	AdminButton.place(x = 980, y = 550, width = 300, height = 170)

### 4 BORROW MENU ###

def destroyBorrowMenu():
		borrowMenu.destroy()

def nav4to3():
	mainMenuF()
	destroyBorrowMenu()
	mainMenu.lift()
	mainMenu.lift()

def borrowMenuF():
	global borrowMenu
	global userstatus
	global UserName
	borrowMenu = Toplevel()
	borrowMenu.title("Borrowed Page")
	mainMenu.iconbitmap("nlb.ico")
	borrowMenu.geometry("1280x720")

	#initialising the table
	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(borrowMenu,style = "mystyle.Treeview")

	my_tree['columns'] = ("Book ID","Title","End Date")
	my_tree.column("#0",width = 70)
	my_tree.column("Book ID",anchor=CENTER,width=100)
	my_tree.column("Title",anchor=CENTER,width = 350)
	my_tree.column("End Date",anchor=CENTER,width=250)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("Book ID",text="Book ID",anchor=CENTER)
	my_tree.heading("Title",text="Title",anchor=CENTER)
	my_tree.heading("End Date",text="End Date",anchor=CENTER)

	view_query2 = "SELECT bookID,borrowEndDate FROM borrow WHERE borrowerID = %d "%(int(userName))
	results = readQuery(connection, view_query2)
	i = 0
	if len(results) != 0:
		for result in results:
			bookid = result[0]
			title_query = "SELECT title FROM book WHERE ID = %d"%(bookid)
			booktitle = readQuery(connection,title_query)[0][0]
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (result[0],booktitle,result[1]))
			i+=1

	my_tree.place(x=320,y=100,height=300,width = 800)

	def extendDue():
		checkfine_query = "SELECT count(*) FROM fine WHERE userID = %d"%(int(userName)) #check if there are fines unpaid by users
		results = readQuery(connection,checkfine_query)
		outstandingfines = results[0][0]
		y = my_tree.selection()
		x = my_tree.focus()
		if y == ():
			return messagebox.showinfo("Warning", "Please select one book")

		elif outstandingfines != 0:
			return messagebox.showinfo("Unpaid Fines!", "Unpaid Fines: unable to process request")
		else :
			t = my_tree.item(x)
			rowvalues = t['values'] #book id,title,endDate
			book_id = rowvalues[0]
			dueDate = datetime.strptime(rowvalues[2],"%Y-%m-%d")
			daysDue = (date.today() - dueDate.date() ).days
			if daysDue > 0:
				return messagebox.showerror("Error", "Book is overdue and cannot be extended.")
			checkreserved_query = "SELECT * FROM reserve WHERE bookID = %d "%(book_id) #check if people are reserving
			ifReserved = readQuery(connection,checkreserved_query)
			if len(ifReserved) != 0:
				return messagebox.showerror(title="Error",message="Reserved: Book cannot be extended")
			due_date = rowvalues[2]
			converted_date = datetime.strptime(due_date,"%Y-%m-%d")
			extended_date = converted_date.date() + relativedelta(weeks=+4)
			querytoExtend = "UPDATE borrow SET borrowEndDate = CAST('%s' AS DATE) WHERE bookID = '%d' AND borrowerID = %d "%(extended_date.strftime("%Y-%m-%d"),book_id,int(userName))
			executeQuery(connection,querytoExtend)
			popResponse = messagebox.showinfo("Extension Successful!", 
				"Book Extended Successfully \nYou will now be redirected to the main menu.")
			if popResponse:
				return nav4to3()

	def returnBook(): #can take place even if there are outstanding fines
		y = my_tree.selection()
		x = my_tree.focus()
		t = my_tree.item(x)
		if y == ():
			return messagebox.showinfo("Warning","Please select one book")
		else: 
			rowvalues = t['values'] #book id,title,endDate
			bookid = rowvalues[0]
			dueDate = datetime.strptime(rowvalues[2],"%Y-%m-%d")
			daysDue = (date.today() - dueDate.date() ).days
			checkfine_query = "SELECT aggregatedAmount FROM fine WHERE userID = %d"%(int(userName))
			checkfine = readQuery(connection,checkfine_query)
			if daysDue > 0:
				if len(checkfine) != 0: #update existing fine
					updatedAmount = int(checkfine[0][0]) + daysDue
					updatefine_query = "UPDATE fine SET aggregatedAmount = %d WHERE userID = %d"%(int(updatedAmount),int(userName))
				else:
					#create new fines for user
					updatefine_query = "INSERT INTO fine (userID, aggregatedAmount) values (%d, %d)"%(int(userName),int(daysDue))
				#delete reservations if fines exist
				delReserved_query ="DELETE FROM reserve WHERE reserverID = %d" %(int(userName))
				executeQuery(connection,updatefine_query)
				executeQuery(connection,delReserved_query)

			querytoReturn = "DELETE FROM borrow WHERE bookID = %d AND borrowerID = %d" %(int(bookid),int(userName))		
			executeQuery(connection,querytoReturn)
			my_tree.delete(y)
			messagebox.showinfo("Successful Transaction!","Book Returned Successfully")

	toExtendButton = Button(borrowMenu,text="Extend Due Date",command = extendDue, 
		bg = "lightgreen", font = ("Mincho", 20))
	toExtendButton.place(x=420, y=400, width = 300, height = 100)

	returnSelectedButton = Button(borrowMenu,text="Return Book",command = returnBook, 
		bg = "lightgreen", font = ("Mincho", 20))
	returnSelectedButton.place(x=720, y=400, width = 300, height = 100)

	topleftheader = Button(borrowMenu, text = "Home", command = nav4to3,
		bg = "lightgreen", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(borrowMenu, text = "Borrow Menu", bg = "lightgreen", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(borrowMenu, text = "Integrated Library System", bg = "lightgreen", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(borrowMenu, text = "Log Out", command = destroyBorrowMenu, fg = "lightgreen",
			bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

## 5 RESERVE MENU ##

def destroyReserveMenu():
	reserveMenu.destroy()

def nav5to3():
	mainMenuF()
	destroyReserveMenu()
	mainMenu.lift()
	mainMenu.lift()

def reserveMenuF():
	global reserveMenu
	global userstatus
	global userName
	reserveMenu = Toplevel()
	reserveMenu.title("Reservations Page")
	reserveMenu.iconbitmap("nlb.ico")
	reserveMenu.geometry("1280x720")

	#initialising the table

	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(reserveMenu,style = "mystyle.Treeview")

	my_tree['columns'] = ("Book ID","Title","Availability")
	my_tree.column("#0",width = 70)
	my_tree.column("Book ID",anchor=CENTER,width=100)
	my_tree.column("Title",anchor=CENTER,width = 350)
	my_tree.column("Availability",anchor=CENTER,width=250)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("Book ID",text="Book ID",anchor=CENTER)
	my_tree.heading("Title",text="Title",anchor=CENTER)
	my_tree.heading("Availability",text="Availability",anchor=CENTER)

	view_query1 = "SELECT bookID FROM reserve WHERE reserverID = %d "%(int(userName))
	results = readQuery(connection, view_query1)
	i = 0
	if len(results) != 0:
		for result in results:
			bookid = result[0]
			title_query = "SELECT title FROM book WHERE ID = %d"%(int(bookid))
			booktitle = readQuery(connection,title_query)[0][0]
			checkborrowed_query = "SELECT * FROM borrow WHERE bookID = %d"%(int(bookid))
			ifborrowed = readQuery(connection,checkborrowed_query)
			if len(ifborrowed) == 0:
				availability = "Available"
			else:
				availability = "Not Available"
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (bookid,booktitle,availability))
			i+=1

	my_tree.place(x=320,y=100,height=300,width = 800)

	def tryBorrow():
		#not necessary since I will clear reservations when fine exist
		checkfine_query = "SELECT * from fine WHERE userID = '%d'"%(int(userName))
		finescheck = readQuery(connection,checkfine_query)
		if len(finescheck) > 0:
			return messagebox.showerror("Error","Please pay fines before borrowing!")
		#check total books borrowed
		totalborrowed_query = "SELECT count(*) from borrow WHERE borrowerID = %d"%(int(userName)) 
		results = readQuery(connection,totalborrowed_query)
		totalborrowed = results[0][0]
		y = my_tree.selection()
		x = my_tree.focus()
		if y == ():
			return messagebox.showerror("Error","Please select one book")

		elif totalborrowed >= 4:
			return messagebox.showinfo("Book Limit Reached","Each user can only borrow a maximum of 4 books!")
		else:
			t = my_tree.item(x)
			rowvalues = t['values'] #book id,title,availability
			bookid = rowvalues[0]
			check_bookavailability = "SELECT * from borrow WHERE bookID = '%d'"%(int(bookid))
			check_availability = readQuery(connection,check_bookavailability)
			if len(check_availability) != 0:
				return messagebox.showerror(title="Error",message="Book still not available!")
			due_date = datetime.today() + relativedelta(weeks=+4)
			querytodelReserve = "DELETE FROM reserve WHERE reserverID = %d AND bookID = %d" %(int(userName),bookid)
			querytoBorrow = "INSERT INTO borrow (borrowerID, bookID, borrowEndDate) VALUES ('%d', '%d', CAST('%s' AS DATE))"%(int(userName),bookid,due_date.strftime("%Y-%m-%d")) 
			executeQuery(connection,querytoBorrow)
			executeQuery(connection,querytodelReserve)
			my_tree.delete(y)
			return messagebox.showinfo("Booking Successful!", "Book Borrowed Successfully")

	def removeReservation():
		y = my_tree.selection()
		x = my_tree.focus()
		t = my_tree.item(x)
		if y == ():
			return messagebox.showinfo("Error","Please select one book")
		else: 
			rowvalues = t['values'] #book id,title,availability
			bookid = rowvalues[0]
			querytoRemove = "DELETE FROM reserve WHERE reserverID = %d AND bookID = %d" %(int(userName),bookid)
			executeQuery(connection,querytoRemove)
			my_tree.delete(y)
			messagebox.showinfo("Success","Book Reservation Removed Successfully")

	toBorrowButton = Button(reserveMenu,text="Convert to Borrow",command = tryBorrow, 
		bg = "palegoldenrod", font = ("Mincho", 20))
	toBorrowButton.place(x=420,y=400,width = 300,height = 100)

	removeSelectedButton = Button(reserveMenu,text="Remove Selected Book",command = removeReservation, 
		bg = "palegoldenrod", font = ("Mincho", 20))
	removeSelectedButton.place(x=720,y=400,width = 300,height = 100)

	topleftheader = Button(reserveMenu, text = "Home", command = nav5to3,
		bg = "palegoldenrod", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(reserveMenu, text = "Reserve Menu", bg = "palegoldenrod", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(reserveMenu, text = "Integrated Library System", bg = "palegoldenrod", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(reserveMenu, text = "Log Out", command = destroyReserveMenu, fg = "palegoldenrod",
			bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

## 6 FINE MENU ##    
def FineMenuF():
	global FineMenu
	FineMenu = Toplevel()
	FineMenu.title("Fine Menu")
	FineMenu.iconbitmap("nlb.ico")
	FineMenu.geometry("1280x720")

	def destroyFineMenu():
		FineMenu.destroy()

	def nav6to3(): 
		mainMenuF()
		destroyFineMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav6to7():
		paymentMenuF()
		destroyFineMenu()
		paymentMenu.lift()
		paymentMenu.lift()

	def toPay():
		checkForFine = "SELECT * FROM fine WHERE userID = %d "%(int(userName))
		result = readQuery(connection,checkForFine)
		if len(result) == 0:
			return messagebox.showinfo(title="Error",message='Nothing to Pay!')
		else:
			nav6to7()

	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(FineMenu,style = "mystyle.Treeview")

	my_tree['columns'] = ("Fine ID","Fine Paid")
	my_tree.column("#0",width = 70)
	my_tree.column("Fine ID",anchor=CENTER,width = 100)
	my_tree.column("Fine Paid",anchor=CENTER,width=240)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("Fine ID",text="Fine ID",anchor=CENTER)
	my_tree.heading("Fine Paid",text="Fine Paid",anchor=CENTER)

	sum1 = 0
	checkFineAmount_query = "SELECT aggregatedAmount FROM fine WHERE userID = %d"%(int(userName)) 
	Amountcheck = readQuery(connection,checkFineAmount_query)
	if len(Amountcheck) != 0:
		sum1 = Amountcheck[0][0]
	paymentLog_query1 = "SELECT ID,amount FROM payment WHERE userID = %d "%(int(userName))
	results = readQuery(connection, paymentLog_query1) 
	i = 0
	if len(results) != 0:
		for result in results:
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (result[0],result[1]))
			i+=1

	my_tree.place(x=650,y=330,height=300,width = 400)

	PaymentLog = Label(FineMenu, text = "Past Transaction:", bg = "thistle", 
		borderwidth = 0, relief = "solid", font = ("Mincho", 16))
	PaymentLog.place(x = 400, y = 330, width = 200, height = 50)

	AmountDue = Label(FineMenu, text = "Current Amount Due:", bg = "thistle", 
		borderwidth = 0, relief = "solid", font = ("Mincho", 16))
	AmountDue.place(x = 400, y = 230, width = 200, height = 50)

	Amount_label=Label(FineMenu, text = sum1, bg = "thistle", 
		borderwidth = 0, relief = "solid", font = ("Mincho", 16))
	Amount_label.place(x = 600, y = 230,  width = 200, height = 50)

	topleftheader = Button(FineMenu, text = "Home", command = nav6to3,
		bg = "thistle", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(FineMenu, text = "Fine Menu", bg = "thistle", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(FineMenu, text = "Integrated Library System", bg = "thistle", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)
	
	if sum1 == 0:
		paymentButton = Button(FineMenu, text = "Make Payment", command = toPay, fg = "thistle",
			bg = "black", font = ("Mincho", 20), state = DISABLED)
	else:
		paymentButton = Button(FineMenu, text = "Make Payment", command = toPay, fg = "thistle",
			bg = "black", font = ("Mincho", 20))
	paymentButton.place(x = 850, y = 230, width = 280, height = 50)

	logoutButton = Button(FineMenu, text = "Log Out", command = destroyFineMenu, fg = "thistle",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

## 7 PAYMENT MENU ##
def paymentMenuF():
	global paymentMenu
	paymentMenu = Toplevel()
	paymentMenu.title("Payment Menu")
	paymentMenu.iconbitmap("nlb.ico")
	paymentMenu.geometry("1280x720")

	def destroyPaymentMenu():
		paymentMenu.destroy()

	def nav7to3():
		mainMenuF()
		destroyPaymentMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav7to6():
		FineMenuF()
		destroyPaymentMenu()
		FineMenu.lift()
		FineMenu.lift()

	def Paid():
		updatePayment = "SELECT aggregatedAmount FROM fine WHERE userID= %d"%(int(userName))
		countPayment = "SELECT count(*) FROM payment"
		index = 1
		amount = readQuery(connection,updatePayment)[0][0]
		value = readQuery(connection,countPayment)
		if len(value) != 0:
			index = value[0][0] + 1
		querytoPayFine = "DELETE FROM fine WHERE userID =%d"%(int(userName))
		queryPayment = "INSERT INTO payment(ID,userID,amount,fineUserID) values (%d, %d, %d, %d)"%(index,int(userName),int(amount), int(userName))
		executeQuery(connection,queryPayment)
		executeQuery(connection,querytoPayFine)
		response = messagebox.showinfo(title="Paid",message='Payment has been received!')
		if response:
			nav7to3()

	topleftheader = Button(paymentMenu, text = "Home", command = nav7to3,
		bg = "thistle", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	topbar = Label(paymentMenu, text = "Integrated Library System", bg = "thistle", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	sidebar = Label(paymentMenu, text = "Payment Menu", bg = "thistle", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	TypeLabel = Label(paymentMenu,text = "Payment Mode: ",font = ("Mincho", 15))
	TypeLabel.place(x=550,y=130)

	v = IntVar()
	CreditButton = Radiobutton(paymentMenu,text = "Credit",variable = v,value = 0, font = ("None",12)).place(x = 700,y = 130)
	DebitButton = Radiobutton(paymentMenu,text = "Debit",variable = v,value = 1, font = ("None",12)).place(x = 800,y = 130)

	CardNumLabel = Label(paymentMenu,text = "Card Number", font = ("Mincho", 15))
	CardNumLabel.place(x=550,y=200)
	CardNumber = IntVar()
	numberEntry = Entry(paymentMenu,textvariable=CardNumber)
	numberEntry.place(x=700,y=200,width = 300,height=25)
	numberEntry.delete(0, END)

	PinLabel = Label(paymentMenu,text = "Cardholder Name",font = ("Mincho", 15))
	PinLabel.place(x=550,y=260)
	PinNumber = IntVar()
	PinEntry = Entry(paymentMenu,textvariable = PinNumber)
	PinEntry.place(x=700,y=260,width = 300,height=25)
	PinEntry.delete(0, END)

	IDlabel = Label(paymentMenu,text = "Issuing Bank",font = ("Mincho", 15))
	IDlabel.place(x=550,y=320)
	IDNumber = IntVar()
	IDEntry = Entry(paymentMenu,textvariable=IDNumber)
	IDEntry.place(x=700,y=320,width = 300, height = 25)
	IDEntry.delete(0, END)

	passwordLabel = Label(paymentMenu,text = "CVC ",font = ("Mincho", 15))
	passwordLabel.place(x=550,y=380)
	password = StringVar()
	passwordEntry = Entry(paymentMenu,textvariable=password)
	passwordEntry.place(x=700,y=380,width = 300,height = 25)

	logoutButton = Button(paymentMenu, text = "Log Out", command = destroyPaymentMenu, fg = "thistle",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	paymentButton = Button(paymentMenu, text = "Pay Fines", command = Paid, fg = "thistle",
		bg = "black", font = ("Mincho", 20))
	paymentButton.place(x = 600, y = 500, width = 280, height = 50)

	BackButton = Button(paymentMenu, text = "Back to Fines", command = nav7to6, fg = "thistle",
		bg = "black", font = ("Mincho", 20))
	BackButton.place(x = 300, y = 670, width = 280, height = 50)

## 8 ADMIN MENU ##
def adminMenuF():
	global adminMenu
	adminMenu = Toplevel()
	adminMenu.title("Admin Menu")
	adminMenu.iconbitmap("nlb.ico")
	adminMenu.geometry("1280x720")

	def destroyAdminMenu():
		adminMenu.destroy()

	def nav8to3():
		mainMenuF()
		destroyAdminMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav8to4a():
		adminBorrowMenuF()
		destroyAdminMenu()
		adminBorrowMenu.lift()
		adminBorrowMenu.lift()

	def nav8to5a():
		adminReserveMenuF()
		destroyAdminMenu()
		adminReserveMenu.lift()
		adminReserveMenu.lift()

	def nav8to6a():
		adminFineMenuF()
		destroyAdminMenu()
		adminFineMenu.lift()
		adminFineMenu.lift()

	def nav8to9():
		searchMenuF()
		destroyAdminMenu()
		searchMenu.lift()
		searchMenu.lift()

	def nav8to10a():
		mySQLBookMenuF()
		destroyAdminMenu()
		mySQLBookMenu.lift()
		mySQLBookMenu.lift()

	topleftheader = Button(adminMenu, text = "Home", command = nav8to3,
		bg = "lightblue", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(adminMenu, text = "Admin Menu", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(adminMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	BorrowButton = Button(adminMenu, text = "Borrowed", command = nav8to4a, fg = "black",
			bg = "lightgreen", font = ("Mincho", 30))
	BorrowButton.place(x = 280, y = 100, width = 300,height = 450)

	ReserveButton = Button(adminMenu, text = "Reserved", command = nav8to5a, fg = "black",
			bg = "palegoldenrod", font = ("Mincho", 30))
	ReserveButton.place(x = 630, y = 100, width = 300,height = 450)

	FineButton = Button(adminMenu, text = "Fines", command = nav8to6a, fg = "black",
			bg = "thistle", font = ("Mincho", 30))
	FineButton.place(x = 980, y = 100, width = 300,height = 450)

	SearchButton = Button(adminMenu, text = "MongoDB Search", command = nav8to9, fg = "black",
			bg = "lavender", font = ("Mincho", 30))
	SearchButton.place(x = 280, y = 550, width = 500, height = 170)

	BookSQLButton = Button(adminMenu, text = "MySQL Books", command = nav8to10a, fg = "black",
			bg = "peachpuff", font = ("Mincho", 30))
	BookSQLButton.place(x = 780, y = 550, width = 500, height = 170)

	logoutButton = Button(adminMenu, text = "Log Out", command = destroyAdminMenu, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

## ADMIN BORROW MENU ##
def adminBorrowMenuF():
	global adminBorrowMenu
	adminBorrowMenu = Toplevel()
	adminBorrowMenu.title("Borrow Menu")
	adminBorrowMenu.iconbitmap("nlb.ico")
	adminBorrowMenu.geometry("1280x720")

	def destroyAdminBorrowMenu():
		adminBorrowMenu.destroy()

	def nav4ato3():
		mainMenuF()
		destroyAdminBorrowMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav4ato8():
		adminMenuF()
		destroyAdminBorrowMenu()
		adminMenu.lift()
		adminMenu.lift()

	topleftheader = Button(adminBorrowMenu, text = "Home", command = nav4ato3,
		bg = "lightblue", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(adminBorrowMenu, text = "Admin \nBorrow Menu", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(adminBorrowMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(adminBorrowMenu,style = "mystyle.Treeview")

	my_tree['columns'] = ("Borrower ID","Book ID","Title","End Date")
	my_tree.column("#0",width = 50)
	my_tree.column("Borrower ID",anchor=CENTER,width=125)
	my_tree.column("Book ID",anchor=CENTER,width=100)
	my_tree.column("Title",anchor=CENTER,width = 300)
	my_tree.column("End Date",anchor=CENTER,width=150)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("Borrower ID",text="Borrower ID",anchor=CENTER)
	my_tree.heading("Book ID",text="Book ID",anchor=CENTER)
	my_tree.heading("Title",text="Title",anchor=CENTER)
	my_tree.heading("End Date",text="End Date",anchor=CENTER)

	view_query2 = "SELECT borrowerID,bookID,borrowEndDate FROM borrow"
	results = readQuery(connection, view_query2)
	i = 0
	if len(results) != 0:
		for result in results:
			bookid = result[1]
			title_query = "SELECT title FROM book WHERE ID = %d"%(bookid)
			booktitle = readQuery(connection,title_query)[0][0]
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (result[0],result[1],booktitle,result[2]))
			i+=1

	my_tree.place(x=320,y=100,height=300,width = 800)

	logoutButton = Button(adminBorrowMenu, text = "Log Out", command = destroyAdminBorrowMenu, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	BacktoAdminButton = Button(adminBorrowMenu, text = "Back to Admin Menu", command = nav4ato8, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	BacktoAdminButton.place(x = 600, y = 600, width = 300, height = 50)

## ADMIN RESERVE MENU ##   
def adminReserveMenuF():
	global adminReserveMenu
	adminReserveMenu = Toplevel()
	adminReserveMenu.title("Reserve Menu")
	adminReserveMenu.iconbitmap("nlb.ico")
	adminReserveMenu.geometry("1280x720")

	def destroyAdminReserveMenu():
		adminReserveMenu.destroy()

	def nav5ato3():
		mainMenuF()
		destroyAdminReserveMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav5ato8():
		adminMenuF()
		destroyAdminReserveMenu()
		adminMenu.lift()
		adminMenu.lift()

	topleftheader = Button(adminReserveMenu, text = "Home", command = nav5ato3,
		bg = "lightblue", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(adminReserveMenu, text = "Admin \nReserve Menu", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(adminReserveMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(adminReserveMenu, style = "mystyle.Treeview")

	my_tree['columns'] = ("Reserver ID","Book ID","Title")
	my_tree.column("#0", width = 50)
	my_tree.column("Reserver ID", anchor=CENTER, width = 100)
	my_tree.column("Book ID", anchor=CENTER, width = 100)
	my_tree.column("Title", anchor=CENTER, width = 400)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("Reserver ID",text="Reserver ID",anchor=CENTER)
	my_tree.heading("Book ID",text="Book ID",anchor=CENTER)
	my_tree.heading("Title",text="Title",anchor=CENTER)

	view_query1 = "SELECT reserverID, bookID FROM reserve"
	results = readQuery(connection, view_query1)
	i = 0
	if len(results) != 0:
		for result in results:
			bookid = result[1]
			title_query = "SELECT title FROM book WHERE ID = %d"%(bookid)
			booktitle = readQuery(connection,title_query)[0][0]
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (result[0],result[1],booktitle))
			i+=1

	my_tree.place(x=320,y=100,height=300,width = 800)


	logoutButton = Button(adminReserveMenu, text = "Log Out", command = destroyAdminReserveMenu, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	BacktoAdminButton = Button(adminReserveMenu, text = "Back to Admin Menu", command = nav5ato8, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	BacktoAdminButton.place(x = 600, y = 600, width = 300, height = 50)

## ADMIN FINE MENU ##    
def adminFineMenuF():
	global adminFineMenu
	adminFineMenu = Toplevel()
	adminFineMenu.title("Fine Menu")
	adminFineMenu.iconbitmap("nlb.ico")
	adminFineMenu.geometry("1280x720")
	
	def destroyAdminFineMenu():
		adminFineMenu.destroy()

	def nav6ato3():
		mainMenuF()
		destroyAdminFineMenu()
		mainMenu.lift()
		mainMenu.lift()

	def nav6ato8():
		adminMenuF()
		destroyAdminFineMenu()
		adminMenu.lift()
		adminMenu.lift()

	topleftheader = Button(adminFineMenu, text = "Home", command = nav6ato3,
		bg = "lightblue", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(adminFineMenu, text = "Admin \nFine Menu", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(adminFineMenu, text = "Integrated Library System", bg = "lightblue", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)
	
	style = ttk.Style()
	style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Mincho', 15))
	style.configure("mystyle.Treeview.Heading", font=("Mincho", 18))
	my_tree = ttk.Treeview(adminFineMenu,style = "mystyle.Treeview")

	my_tree['columns'] = ("User ID","Fine Amount")
	my_tree.column("#0",width = 20)
	my_tree.column("User ID",anchor=CENTER,width=240)
	my_tree.column("Fine Amount",anchor=CENTER,width=240)
	
	my_tree.heading("#0",text='Index',anchor=CENTER)
	my_tree.heading("User ID",text="User ID",anchor=CENTER)
	my_tree.heading("Fine Amount",text="Fine Amount",anchor=CENTER)

	view_query1 = "SELECT userID,aggregatedAmount FROM fine "
	results = readQuery(connection, view_query1)
	i = 0
	if len(results) != 0:
		for result in results:
			my_tree.insert(parent = '',index='end',iid=i,text=i+1,values = (result[0],result[1]))
			i+=1

	my_tree.place(x=320,y=100,height=300,width = 800)

	logoutButton = Button(adminFineMenu, text = "Log Out", command = destroyAdminFineMenu, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	BacktoAdminButton = Button(adminFineMenu, text = "Back to Admin Menu", command = nav6ato8, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
	BacktoAdminButton.place(x = 600, y = 600, width = 300, height = 50)
	
### SEARCH WINDOW ###
def destroySearchMenu():
	searchMenu.destroy()

def nav9to3():
	mainMenuF()
	destroySearchMenu()
	mainMenu.lift()
	mainMenu.lift()

def nav9to10():
	resultMenuF()
	destroySearchMenu()
	resultMenu.lift()
	resultMenu.lift()

def simpleSearch():
	global searchEntry
	global searchResult
	querycode = {}
	queryproject = {"_id": 1, "title": 1, "isbn": 1, "pageCount": 1, "authors": 1, "categories": 1}
	if searchEntry.get() != "":
		value = {}
		value["$regex"] = searchEntry.get()
		querycode["title"] = value
	searchResult = queryMongo(querycode, queryproject)
	nav9to10()

def advancedSearch():
	global searchID
	global searchTitle
	global searchResult
	global searchISBN
	global searchAuthor
	global searchAuthor2
	global searchAuthor3
	global searchCategoryStore
	global searchCategoryStore2
	global searchCategoryStore3

	querycode = []
	queryproject = {"_id": 1, "title": 1, "isbn": 1, "pageCount": 1, "authors": 1, "categories": 1}

	if checkIDVar.get() == 1 and searchID.get() != "":
		temp = {}
		temp["_id"] = int(searchID.get())
		querycode.append(temp)

	if checkTitleVar.get() == 1 and searchTitle.get() != "":
		value = {}
		temp = {}
		value["$regex"] = searchTitle.get()
		temp["title"] = value
		querycode.append(temp)

	if checkISBNVar.get() == 1 and searchISBN.get() != "":
		value = {}
		temp = {}
		value["$regex"] = searchISBN.get()
		temp["isbn"] = value
		querycode.append(temp)

	if checkYearVar.get() == 1 and searchYear.get() != "":
		year = int(searchYear.get())
		from_year = datetime(year, 1, 1)
		to_year = datetime(year + 1, 1, 1)

		value = {}
		temp = {}
		value["$gte"] = from_year
		value["$lt"] = to_year
		temp["publishedDate"] = value
		querycode.append(temp)

	if checkAuthorVar.get() == 1:
		authorList = []
		if searchAuthor.get() != "":
			authorList.append(searchAuthor.get())
		if searchAuthor2.get() != "":
			authorList.append(searchAuthor2.get())
		if searchAuthor3.get() != "":
			authorList.append(searchAuthor3.get())
		if searchAuthor4.get() != "":
			authorList.append(searchAuthor4.get())

		if authorList != []:
			for authorName in authorList:
				first = {}
				second = {}
				third = {}
				first["$regex"] = authorName
				second["$elemMatch"] = first
				third["authors"] = second
				querycode.append(third)

	if checkCategoryVar.get() == 1:
		categoryList = []
		if searchCategoryStore.get() != "-----":
			categoryList.append(searchCategoryStore.get())
		if searchCategoryStore2.get() != "-----":
			categoryList.append(searchCategoryStore2.get())
		if searchCategoryStore3.get() != "-----":
			categoryList.append(searchCategoryStore3.get())

		if categoryList != []:
			for categoryName in categoryList:
				first = {}
				second = {}
				first["$eq"] = categoryName
				second["categories"] = first
				querycode.append(second)

	finalquerycode = {}
	if querycode != []:
		finalquerycode["$and"] = querycode
	searchResult = queryMongo(finalquerycode, queryproject)
	nav9to10()

def searchMenuF():
	global searchMenu
	searchMenu = Toplevel()
	searchMenu.title("Search Menu")
	searchMenu.iconbitmap("nlb.ico")
	searchMenu.geometry("1280x720")

	topleftheader = Button(searchMenu, text = "Home", command = nav9to3,
		bg = "lavender", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(searchMenu, text = "MongoDB \nSearch Menu", bg = "lavender", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(searchMenu, text = "Integrated Library System", bg = "lavender", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(searchMenu, text = "Log Out", command = destroySearchMenu, fg = "lavender",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)
#SIMPLESEARCH
	searchBtn = Button(searchMenu, text = "Simple Search", command = simpleSearch, fg = "lavender",
		bg = "black", font = ("Mincho", 20))
	searchBtn.place(x = 975, y = 110, width = 280, height = 50)
	
	global searchEntry
	searchEntry = Entry(searchMenu, width = 45, borderwidth = 5, font = ("Mincho", 20))
	searchEntry.place(x = 300, y = 115)
#ribbonSeperator
	orRibbon = Label(searchMenu, text = "OR \n use advanced search below", bg = "lavender", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	orRibbon.place(x = 280, y = 175, width = 1000, height = 100)
#ADVANCEDSEARCH
	advsearchBtn = Button(searchMenu, text = "Advanced Search", command = advancedSearch, fg = "lavender",
		bg = "black", font = ("Mincho", 20))
	advsearchBtn.place(x = 950, y = 670, width = 280, height = 50)
#searchforID
	global checkIDVar
	checkIDVar = IntVar()
	checkID = Checkbutton(searchMenu, text = "Book ID", variable = checkIDVar, font = ("Mincho", 16))
	checkID.place(x = 300, y = 300)

	global searchID
	searchID = Entry(searchMenu, width = 60, borderwidth = 5, font = ("Mincho", 16))
	searchID.place(x = 475, y = 300)
#searchforTitle
	global checkTitleVar
	checkTitleVar = IntVar()
	checkTitle = Checkbutton(searchMenu, text = "Title", variable = checkTitleVar, font = ("Mincho", 16))
	checkTitle.place(x = 300, y = 350)

	global searchTitle
	searchTitle = Entry(searchMenu, width = 60, borderwidth = 5, font = ("Mincho", 16))
	searchTitle.place(x = 475, y = 350)
#searchforISBN
	global checkISBNVar
	checkISBNVar = IntVar()
	checkISBN = Checkbutton(searchMenu, text = "ISBN", variable = checkISBNVar, font = ("Mincho", 16))
	checkISBN.place(x = 300, y = 400)

	global searchISBN
	searchISBN = Entry(searchMenu, width = 60, borderwidth = 5, font = ("Mincho", 16))
	searchISBN.place(x = 475, y = 400)
#searchforAuthor
	global checkAuthorVar
	checkAuthorVar = IntVar()
	checkAuthor = Checkbutton(searchMenu, text = "Author(s)", variable = checkAuthorVar, font = ("Mincho", 16))
	checkAuthor.place(x = 300, y = 450)

	global searchAuthor
	searchAuthor = Entry(searchMenu, width = 13, borderwidth = 5, font = ("Mincho", 16))
	searchAuthor.place(x = 475, y = 450)

	global searchAuthor2
	searchAuthor2 = Entry(searchMenu, width = 13, borderwidth = 5, font = ("Mincho", 16))
	searchAuthor2.place(x = 650, y = 450)

	global searchAuthor3
	searchAuthor3 = Entry(searchMenu, width = 13, borderwidth = 5, font = ("Mincho", 16))
	searchAuthor3.place(x = 825, y = 450)

	global searchAuthor4
	searchAuthor4 = Entry(searchMenu, width = 13, borderwidth = 5, font = ("Mincho", 16))
	searchAuthor4.place(x = 1000, y = 450)
#searchforCategory
	global checkCategoryVar
	checkCategoryVar = IntVar()
	checkCategory = Checkbutton(searchMenu, text = "Category", variable = checkCategoryVar, font = ("Mincho", 16))
	checkCategory.place(x = 300, y = 500)

	global allCategories
	allCategories = ["-----"]
	allcats = distinctMongo("categories")
	allCategories += allcats

	global searchCategoryStore
	searchCategoryStore = StringVar()
	searchCategoryStore.set("-----")
	searchCategory = OptionMenu(searchMenu, searchCategoryStore, *allCategories)
	searchCategory.place(x = 475, y = 500, width = 225, height = 40)

	global searchCategoryStore2
	searchCategoryStore2 = StringVar()
	searchCategoryStore2.set("-----")
	searchCategory2 = OptionMenu(searchMenu, searchCategoryStore2, *allCategories)
	searchCategory2.place(x = 725, y = 500, width = 225, height = 40)
	
	global searchCategoryStore3
	searchCategoryStore3 = StringVar()
	searchCategoryStore3.set("-----")
	searchCategory3 = OptionMenu(searchMenu, searchCategoryStore3, *allCategories)
	searchCategory3.place(x = 975, y = 500, width = 225, height = 40)

#searchforPubYear
	global checkYearVar
	checkYearVar = IntVar()
	checkYear = Checkbutton(searchMenu, text = "Published Year", variable = checkYearVar, font = ("Mincho", 16))
	checkYear.place(x = 300, y = 550)

	global searchYear
	searchYear = Entry(searchMenu, width = 60, borderwidth = 5, font = ("Mincho", 16))
	searchYear.place(x = 475, y = 550)

### RESULT WINDOW ###
def destroyResultMenu():
	resultMenu.destroy()

def nav10to3():
	mainMenuF()
	destroyResultMenu()
	mainMenu.lift()
	mainMenu.lift()

def nav10to11():
	bookMenuF()
	destroyResultMenu()
	bookMenu.lift()
	bookMenu.lift()

def nav10to10a():
	mySQLBookMenuF()
	destroyResultMenu()
	mySQLBookMenu.lift()
	mySQLBookMenu.lift()

def resultMenuF():
	global resultMenu
	global resultTree
	resultMenu = Toplevel()
	resultMenu.title("Result Menu")
	resultMenu.iconbitmap("nlb.ico")
	resultMenu.geometry("1280x720")

	topleftheader = Button(resultMenu, text = "Home", command = nav10to3,
		bg = "lavender", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(resultMenu, text = "MongoDB \nResult Menu", bg = "lavender", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(resultMenu, text = "Integrated Library System", bg = "lavender", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(resultMenu, text = "Log Out", command = destroyResultMenu, fg = "lavender",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	resultTree = ttk.Treeview(resultMenu)
	resultTree['columns'] = ("Book ID", "Title", "ISBN", "Page Count", "Author", "Category")
	resultTree.column("#0", anchor = CENTER, width = 60, minwidth=25)
	resultTree.column("Book ID", anchor = CENTER, width = 60, minwidth = 25)
	resultTree.column("Title", anchor = CENTER, width = 200, minwidth = 25)
	resultTree.column("ISBN", anchor = CENTER, width = 80, minwidth = 25)
	resultTree.column("Page Count", anchor = CENTER, width = 60, minwidth = 25)
	resultTree.column("Author", anchor = CENTER, width = 120, minwidth = 25)
	resultTree.column("Category", anchor = CENTER, width = 120, minwidth = 25)

	resultTree.heading("#0", text = 'Index', anchor = CENTER)
	resultTree.heading("Book ID", text = "Book ID", anchor = CENTER)
	resultTree.heading("Title", text = "Title", anchor = CENTER)
	resultTree.heading("ISBN", text = "ISBN", anchor = CENTER)
	resultTree.heading("Page Count", text = "Page Count", anchor = CENTER)
	resultTree.heading("Author", text = "Author(s)", anchor = CENTER)
	resultTree.heading("Category", text = "Category", anchor = CENTER)

	global searchMongoBookCount
	global searchResult
	searchMongoBookCount = 0

	for result in searchResult:
		authorResult = result.get("authors", "None")
		cateResult = result.get("categories", "None")
		authorString = ""
		cateString = ""
		if isinstance(authorResult, list):
			for name in authorResult:
				authorString += name + ", "
		else:
			authorString = authorResult

		if isinstance(cateResult, list):
			for cate in cateResult:
				cateString += cate + ", "
		else:
			cateString = cateResult

		resultTree.insert(parent = '', index = 'end', iid = searchMongoBookCount, 
			text = searchMongoBookCount + 1, 
			values = (result.get("_id", "None"), result.get("title", "None"), 
				result.get("isbn", "None"), result.get("pageCount", "None"), 
				authorString, cateString))
		searchMongoBookCount += 1

	resultTree.place(x = 420, y = 100, height = 500, width = 700)

	bookViewBtn = Button(resultMenu, text = "Go to MySQL Books", command = nav10to10a, fg = "lavender",
		bg = "black", font = ("Mincho", 24))
	bookViewBtn.place(x = 420, y = 600, width = 700, height = 100)

### MYSQL BOOK MENU ###
def destroyMySQLBookMenu():
	mySQLBookMenu.destroy()

def nav10ato3():
	mainMenuF()
	destroyMySQLBookMenu()
	mainMenu.lift()
	mainMenu.lift()

def nav10ato11():
	bookMenuF()
	destroyMySQLBookMenu()
	bookMenu.lift()
	bookMenu.lift()

def openBook():
	global bookWindowDetail
	y = mySQLTree.selection()
	x = mySQLTree.focus()
	if y == ():
		return messagebox.showinfo("Popup", "Please select one book before continuing")
	else:
		t = mySQLTree.item(x)
		bookWindowDetail = t["values"]
		nav10ato11()

def mySQLBookMenuF():
	global mySQLBookMenu
	global mySQLTree
	mySQLBookMenu = Toplevel()
	mySQLBookMenu.title("MySQL Books Menu")
	mySQLBookMenu.iconbitmap("nlb.ico")
	mySQLBookMenu.geometry("1280x720")

	topleftheader = Button(mySQLBookMenu, text = "Home", command = nav10ato3,
		bg = "peachpuff", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(mySQLBookMenu, text = "MySQL \nBooks Menu", bg = "peachpuff", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(mySQLBookMenu, text = "Integrated Library System", bg = "peachpuff", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	logoutButton = Button(mySQLBookMenu, text = "Log Out", command = destroyMySQLBookMenu, fg = "peachpuff",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	mySQLTree = ttk.Treeview(mySQLBookMenu)
	mySQLTree['columns'] = ("Book ID", "Title", "Borrow Status", "Reserve Status", "Availability")
	mySQLTree.column("#0", anchor = CENTER, width = 60, minwidth=25)
	mySQLTree.column("Book ID", anchor = CENTER, width = 60, minwidth = 25)
	mySQLTree.column("Title", anchor = CENTER, width = 300, minwidth = 25)
	mySQLTree.column("Borrow Status", anchor = CENTER, width = 90, minwidth = 25)
	mySQLTree.column("Reserve Status", anchor = CENTER, width = 90, minwidth = 25)
	mySQLTree.column("Availability", anchor = CENTER, width = 100, minwidth = 25)

	mySQLTree.heading("#0", text = 'Index', anchor = CENTER)
	mySQLTree.heading("Book ID", text = "Book ID", anchor = CENTER)
	mySQLTree.heading("Title", text = "Title", anchor = CENTER)
	mySQLTree.heading("Borrow Status", text = "Borrow Status", anchor = CENTER)
	mySQLTree.heading("Reserve Status", text = "Reserve Status", anchor = CENTER)
	mySQLTree.heading("Availability", text = "Availability", anchor = CENTER)

	global searchBookCount
	searchBookCount = 0
	allBorrowedAndReservedQuery = """SELECT ID, title, b.borrowerID, r.reserverID 
		FROM book LEFT JOIN borrow b ON ID = b.bookID LEFT JOIN reserve r ON ID = r.bookID;"""
	searchResult = readQuery(connection, allBorrowedAndReservedQuery)
	#0=ID,1=Title,2=borrowerID,3=reserverID
	for bookTuple in searchResult:
		if bookTuple[2] == None:
			borrowStatus = "Not Borrowed"
		else:
			borrowStatus = "Borrowed"
		if bookTuple[3] == None:
			reserveStatus = "Not Reserved"
		else:
			reserveStatus = "Reserved"
		if bookTuple[2] == None and bookTuple[3] == None:
			availStat = "Available"
		elif bookTuple[2] != None and bookTuple[3] == None:
			availStat = "Reservation Only"
		else:
			availStat = "Not Available"

		mySQLTree.insert(parent = '', index = 'end', iid = searchBookCount, 
			text = searchBookCount + 1, values = (bookTuple[0], bookTuple[1], borrowStatus, reserveStatus, availStat))
		searchBookCount += 1

	mySQLTree.place(x = 420, y = 100, height = 500, width = 700)

	bookViewBtn = Button(mySQLBookMenu, text = "See Book Details", command = openBook, fg = "peachpuff",
		bg = "black", font = ("Mincho", 24))
	bookViewBtn.place(x = 420, y = 600, width = 700, height = 100)

### BOOK WINDOW ###
def destroyBookMenu():
	bookMenu.destroy()

def nav11to3():
	mainMenuF()
	destroyBookMenu()
	mainMenu.lift()
	mainMenu.lift()

def bookBook():
	global userName
	#check for unpaid fines
	unpaidFineQuery = "SELECT count(*) FROM fine WHERE userID = " + str(userName)
	numUnpaidFine = readQuery(connection, unpaidFineQuery)
	numUnpaidFine = numUnpaidFine[0][0]
	if numUnpaidFine != 0: 
		popResponse = messagebox.showerror("Outstanding Fines", 
			"You are not allowed to borrow until your fines are paid!\n You will now be redirected to the main menu.")
		if popResponse:
			return nav11to3()

	#check for bookloan limit of 4
	bookCountQuery = "SELECT count(*) FROM borrow WHERE borrowerID = " + str(userName)
	numBookLoaned = readQuery(connection, bookCountQuery)
	numBookLoaned = numBookLoaned[0][0]
	if numBookLoaned >= 4:
		popResponse = messagebox.showerror("Book Limit Reached", 
			"Each user can only borrow a maximum of 4 books!\n You will now be redirected to the main menu.")
		if popResponse:
			return nav11to3()

	#check if bookstatus still holds
	bookQuery = "SELECT count(*) FROM borrow WHERE bookID = " + str(bookWindowDetail[0])
	result = readQuery(connection, bookQuery)
	result = result[0]
	if result[0] == 0:
		#execute booking query
		due_date = datetime.today() + relativedelta(weeks=+4)
		bookingQuery = "INSERT INTO borrow (borrowerID, bookID, borrowEndDate) VALUES ('%d', '%d', CAST('%s' AS DATE))"%(int(userName),  bookWindowDetail[0], due_date.strftime("%Y-%m-%d"))
		executeQuery(connection, bookingQuery)
		#query executed, giving confirmation
		popResponse = messagebox.showinfo("Booking Confirmation", 
			"Your booking has been confirmed!\n You will now be redirected to the main menu.")
		if popResponse:
			return nav11to3()
	else: 
		popResponse2 = messagebox.showerror("Booking Error", 
			"There has been an error when processing your booking.\n You will now be redirected to the main menu.")
		if popResponse2:
			return nav11to3()

def reserveBook():
	#check for unpaid fines
	unpaidFineQuery = "SELECT count(*) FROM fine WHERE userID = " + str(userName)
	numUnpaidFine = readQuery(connection, unpaidFineQuery)
	numUnpaidFine = numUnpaidFine[0][0]
	if numUnpaidFine != 0: 
		popResponse = messagebox.showerror("Outstanding Fines", 
			"You are not allowed to reserve until your fines are paid!\n You will now be redirected to the main menu.")
		if popResponse:
			return nav11to3()

	#check if reserver is the borrower
	bookerQuery = "SELECT borrowerID FROM borrow WHERE bookID = " + str(bookWindowDetail[0])
	resultBooker = readQuery(connection, bookerQuery)
	if len(resultBooker) > 0:
		if resultBooker[0][0] == int(userName):
			popResponse = messagebox.showerror("Same User", 
				"You have borrowed this book! \n You will now be redirected to the main menu.")
			if popResponse:
				return nav11to3()


	#check if bookstatus still holds
	bookQuery = "SELECT count(*) FROM reserve WHERE bookID = " + str(bookWindowDetail[0])
	result = readQuery(connection, bookQuery)
	result = result[0]
	if result[0] == 0:
		#execute reservation query
		rsvnQuery = "INSERT INTO reserve (reserverID, bookID) VALUES ('%d', '%d')"%(int(userName),  bookWindowDetail[0])
		executeQuery(connection, rsvnQuery)
		#query executed, giving confirmation 
		popResponse = messagebox.showinfo("Reservation Confirmation", 
			"Your reservation has been confirmed!\n You will now be redirected to the main menu.")
		if popResponse:
			return nav11to3()
	else: 
		popResponse2 = messagebox.showerror("Reservation Error", 
			"There has been an error when processing your reservation.\n You will now be redirected to the main menu.")
		if popResponse2:
			return nav11to3()

def bookMenuF():
	global bookMenu
	bookMenu = Toplevel()
	bookMenu.title("Borrow Menu")
	bookMenu.iconbitmap("nlb.ico")
	bookMenu.geometry("1280x720")

	global bookWindowDetail
	#bookWindowDetail[0] is the bookID

	topleftheader = Button(bookMenu, text = "Home", command = nav11to3,
		bg = "peachpuff", font = ("Mincho", 40))
	topleftheader.place(x = 0, y = 0, width = 280, height = 100)

	sidebar = Label(bookMenu, text = "MySQL Book \nActions Menu", bg = "peachpuff", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 28))
	sidebar.place(x = 0, y = 100, width = 280, height = 570)

	topbar = Label(bookMenu, text = "Integrated Library System", bg = "peachpuff", 
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	topbar.place(x = 280, y = 0, width = 1000, height = 100)

	bookTitle = Label(bookMenu, text = bookWindowDetail[1], fg = "peachpuff", bg = "black",
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	bookTitle.place(x = 280, y = 325, width = 1000, height = 225)

	bookidn = Label(bookMenu, text = "Book ID \n" + str(bookWindowDetail[0]), fg = "peachpuff", bg = "black",
		borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
	bookidn.place(x = 280, y = 100, width = 200, height = 225)

	#book is borrowed and reserved
	if bookWindowDetail[2] == "Borrowed" and bookWindowDetail[3] == "Reserved":
		bookavail = Label(bookMenu, text = "Book has been \n borrowed and reserved", 
			fg = "peachpuff", bg = "black", borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
		bookBtn = Button(bookMenu, text = "Borrowing \n Not Available", command = bookBook, fg = "black",
			bg = "lightgreen", font = ("Mincho", 40), state = DISABLED)
		rsvBtn = Button(bookMenu, text = "Reservation \n Not Available", command = reserveBook, 
			fg = "black", bg = "palegoldenrod", font = ("Mincho", 40), state = DISABLED)
	#book is borrowed but not reserved
	elif bookWindowDetail[2] == "Borrowed" and bookWindowDetail[3] == "Not Reserved":
		bookavail = Label(bookMenu, text = "Book has been borrowed \n but can be Reserved", 
			fg = "peachpuff", bg = "black", borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
		bookBtn = Button(bookMenu, text = "Borrowing \n Not Available", command = bookBook, fg = "black",
			bg = "lightgreen", font = ("Mincho", 40), state = DISABLED)
		rsvBtn = Button(bookMenu, text = "Reserve", command = reserveBook, fg = "black",
			bg = "palegoldenrod", font = ("Mincho", 40))
	#book not borrowed, but reserved
	elif bookWindowDetail[2] == "Not Borrowed" and bookWindowDetail[3] == "Reserved":
		bookavail = Label(bookMenu, text = "A user has \n reserved this book", fg = "peachpuff", 
			bg = "black", borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
		bookBtn = Button(bookMenu, text = "Borrowing \n Not Available", command = bookBook, fg = "black",
			bg = "lightgreen", font = ("Mincho", 40), state = DISABLED)
		rsvBtn = Button(bookMenu, text = "Reservation \n Not Available", command = reserveBook, fg = "black",
			bg = "palegoldenrod", font = ("Mincho", 40), state = DISABLED)
	#book not borrowed and not reserved
	else:
		bookavail = Label(bookMenu, text = "Book Available Now", fg = "peachpuff", 
			bg = "black", borderwidth = 2, relief = "ridge", font = ("Mincho", 40))
		bookBtn = Button(bookMenu, text = "Borrow", command = bookBook, fg = "black",
			bg = "lightgreen", font = ("Mincho", 40))
		rsvBtn = Button(bookMenu, text = "Reserve", command = reserveBook, fg = "black",
			bg = "palegoldenrod", font = ("Mincho", 40))
	bookavail.place(x = 480, y = 100, width = 800, height = 225)


	logoutButton = Button(bookMenu, text = "Log Out", command = destroyBookMenu, fg = "peachpuff",
		bg = "black", font = ("Mincho", 20))
	logoutButton.place(x = 0, y = 670, width = 280, height = 50)

	bookBtn.place(x = 280, y = 550, width = 500, height = 170)
	rsvBtn.place(x = 780, y = 550, width = 500, height = 170)

### DONT TOUCH ###
def openMain():
	loginMenuF()
root = Tk()
startButton = Button(root, text = "Start", command = openMain, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))
startButton.pack()
root.mainloop()
