from tkinter import *
from tkinter import ttk  # css for tkinter
from tkinter import messagebox as tm
from datetime import datetime
import dqsClass
import shelve
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

LARGE_FONT = ("Verdana", 16, "bold")
BACKGROUND_COLOUR_DARK = "#283F44"
BACKGROUND_COLOUR_DARKER = "#393B3F"
BACKGROUND_RED = "#AD423E"

class dqsLearn(Frame): # include inheritance as parameters
    def __init__(self, *args, **kwargs): # args(arguments) = any number of variables kwargs(kewyword arguments) = passing dictionaries/data structures
        # tk.Tk.__init__(self, *args, **kwargs)
        Frame.__init__(self, *args, **kwargs) # Initialise the frame

        ttk.Style().configure("TButton", background=BACKGROUND_COLOUR_DARKER)

        container = Frame() # Assign container as a frame which we can alter
        # allow the container to expand into the entire window
        container.pack(side="top", fill="both", expand=True)
        # set up the containing window
        container.grid_rowconfigure(0, weight=2)
        container.grid_columnconfigure(0, weight=2)

        # collection of frames i.e. login, menu, lesson, test
        self.frames = {}

        for page in (login, studentMenu, lesson_1, lesson_2, test_1, test_2, lecturerMenu, view_results1, view_results2, view_average, view_average_sets, view_average_logic):
            # set the current frame
            frame = page(container, self) # Assign the login screen to the first frame to be passed

            # Set initial frame to the login screen
            self.frames[page] = frame

            frame.grid(row=0, column=0, sticky="nsew") # nsew stretches everything to all edges, fits to size of window

        self.show_frame(login)

    def show_frame(self, cont): # cont = controller (unused)
        frame = self.frames[cont] # retrieves the frame with key "cont" from frames dictionary
        frame.tkraise() # Moves called frame to top



# **** COMMON REUSABLE CODE ****

# Classes for each page in the software

class login(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)
        self.controller = controller
        label = Label(self, text="Login Page", font=LARGE_FONT, bg=BACKGROUND_COLOUR_DARKER, fg="white")
        label.place(rely = .425, relx = .5, anchor = CENTER)

        self.label_1 = Label(self, text="Username", fg="white", bg=BACKGROUND_COLOUR_DARKER)
        self.entry_1 = Entry(self)
        self.label_1.place(rely = .47, relx = .45, anchor = CENTER)
        self.entry_1.place(rely = .47, relx = .55, anchor = CENTER)

        self.label_2 = Label(self, text="Password", fg="white", bg=BACKGROUND_COLOUR_DARKER)
        self.entry_2 = Entry(self, show="*")
        self.label_2.place(rely = .5, relx = .45, anchor = CENTER)
        self.entry_2.place(rely = .5, relx = .55, anchor = CENTER)

        self.logbtn = ttk.Button(self, text="Login", command=self._login_btn_clicked)
        self.logbtn.place(rely = .555, relx = .5, anchor = CENTER)

        button1 = ttk.Button(self, text="Student Login", command=lambda: controller.show_frame(studentMenu)) # only calls the function when the button is pressed
        button1.pack()
        button2 = ttk.Button(self, text="Lecturer Login", command=lambda: controller.show_frame(lecturerMenu))  # only calls the function when the button is pressed
        button2.pack()

        self.pack()

    def _login_btn_clicked(self):
        # print("Clicked")
        username = self.entry_1.get()
        password = self.entry_2.get()

        # print(username, password)

        student_usernames = ("C100", "C200", "C300")
        student_passwords = ("PASS", "PASS1", "PASS2")

        teacher_usernames = ("T100", "T200", "T300")
        teacher_passwords = ("TPASS", "TPASS1", "TPASS3")

        if username in student_usernames and password in student_passwords:
            if (student_usernames.index(username) == student_passwords.index(password)):
                tm.showinfo("Login info", "Welcome Student")
                self.controller.show_frame(studentMenu)
                self.line1.destroy()
                self.line2.destroy()
            else:
                tm.showerror("Login error", "Incorrect information")
        elif username in teacher_usernames and password in teacher_passwords:
            if (teacher_usernames.index(username) == teacher_passwords.index(password)):
                tm.showinfo("Login info", "Welcome Teacher")
                self.controller.show_frame(lecturerMenu)
                self.line1.destroy()
                self.line2.destroy()
            else:
                tm.showerror("Login error", "Incorrect information")
        else:
            tm.showerror("Login error", "Incorrect information")


        # button1 = Button(self, text="Student Login", command=studentMenu) # calls the function immediately

class studentMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Student Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to login", command=lambda: controller.show_frame(login))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="Begin logic lesson", command=lambda: controller.show_frame(lesson_1))
        button2.pack(padx=10, pady=10)

        # ?? This should be disabled (greyed out) until the lesson has been completed ??
        button3 = ttk.Button(self, text="Begin logic test", command=lambda: controller.show_frame(test_1))
        button3.pack(padx=10, pady=10)

        button4 = ttk.Button(self, text="Begin sets lesson", command=lambda: controller.show_frame(lesson_2))
        button4.pack(padx=10, pady=10)

        button5 = ttk.Button(self, text="Begin sets test", command=lambda: controller.show_frame(test_2))
        button5.pack(padx=10, pady=10)


class lesson_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Logic - Lesson", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement
        #label.grid(row=0, column=0, columnspan=10, sticky=N)

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)
        #button1.grid(row=1, column=0, columnspan=2, sticky=N)

        canvas_width = 750
        canvas_height = 600

        canvas = Canvas(self, width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOUR_DARK)
        canvas.pack(expand=YES, fill=Y, side=LEFT, padx=10, pady=10)
        #canvas.grid(row=2, column=0, rowspan=1)            

        Lb1 = Listbox(self, bg=BACKGROUND_RED, selectmode=SINGLE, selectbackground="#AD423E")#create listbox object,
        Lb1.insert(1, "Propositional Logic")
        Lb1.insert(2, "Combining Propositions")#add the listbox options
        Lb1.insert(3, "Truth Tables")
        Lb1.insert(4, "Implication")
        Lb1.insert(5, "Tautologies")
        Lb1.insert(6, "De Morgan's Laws")
        Lb1.pack(side=RIGHT, anchor=N, padx=10, pady=10) #display listbox to screen, hug left of lesson slide

        self.slides = {
                    1 : "Slide1.png",
                    2 : "Slide2.png",
                    3 : "Slide3.png",
                    4 : "Slide4.png",
                    5 : "Slide5.png",
                    6 : "Slide6.png"}

        self.slide_index = 0

        # set slide
        def set_slide(evt):
            # J : function for listbox onclick
            Lb1.selection_clear(self.slide_index-1) # J: clear highlighted list box item
            temp_tuple = Lb1.curselection() # J: get index of clicked listbox item 
            self.slide_index = temp_tuple[0]+1 #J: set slide index
            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        def previous_slide(self):
            # if on last slide, re-activate "next" button
            button3.config(state="normal")

            # if moving onto the first slide, disable "previous" button
            if self.slide_index == 2:
                button2.config(state=DISABLED) 

            Lb1.selection_clear(self.slide_index-1) #clear highlighted listbox item, -1 for string indexing

            self.slide_index -= 1
            Lb1.selection_set(self.slide_index-1) #highlight current listbox item, -1 for string indexing

            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        def next_slide(self):
            # if on first slide, re-activate "previous" button
            button2.config(state="normal")

            # if moving onto the last slide, disable "next" button
            if self.slide_index == 6:
                button3.config(state=DISABLED)
            
            Lb1.selection_clear(self.slide_index-1)

            self.slide_index += 1
            Lb1.selection_set(self.slide_index-1)

            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        Lb1.bind('<<ListboxSelect>>', set_slide) # J: bind set_slide function to listbox onclick event
        button2 = ttk.Button(self, text="Previous", command=lambda: previous_slide(self))
        button2.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button2.grid(row=4, column=2)

        button3 = ttk.Button(self, text="Next", command=lambda: next_slide(self))
        button3.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button3.grid(row=4, column=4)


        next_slide(self)
        button2.config(state=DISABLED)

class lesson_2(Frame):
    # ****EDIT THIS CLASS FOR YOUR LESSON ALEX****


    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Logic - Lesson", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement
        #label.grid(row=0, column=0, columnspan=10, sticky=N)

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)
        #button1.grid(row=1, column=0, columnspan=2, sticky=N)

        canvas_width = 960
        canvas_height = 720

        canvas = Canvas(self, width=canvas_width, height=canvas_height, bg=BACKGROUND_COLOUR_DARK)
        canvas.pack(expand=YES, fill=Y, side=LEFT, padx=10, pady=10)
        #canvas.grid(row=2, column=0, rowspan=1)
        #

        Lb1 = Listbox(self, bg=BACKGROUND_RED, selectmode=SINGLE, selectbackground="#AD423E")#create listbox object,
        Lb1.insert(1, "Sets")
        Lb1.insert(2, "Special sets")#add the listbox options
        Lb1.insert(3, "Notation")
        Lb1.insert(4, "Python and sets")
        Lb1.insert(5, "Types of sets, and venn diagrams")
        Lb1.insert(6, "Types of sets, and venn diagrams")
        Lb1.insert(7, "Inclusion-exclusion principle")
        Lb1.pack(side=RIGHT, anchor=N, padx=10, pady=10) #display listbox to screen, hug left of lesson slide

        self.slides = {
                    1 : "SlideA1.png",
                    2 : "SlideA2.png",
                    3 : "SlideA3.png",
                    4 : "SlideA4.png",
                    5 : "SlideA5.png",
                    6 : "SlideA6.png",
                    7 : "SlideA7.png"}

        self.slide_index = 0

        # set slide
        def set_slide(evt):
            # J : function for listbox onclick
            Lb1.selection_clear(self.slide_index-1) # J: clear highlighted list box item
            temp_tuple = Lb1.curselection() # J: get index of clicked listbox item 
            self.slide_index = temp_tuple[0]+1 #J: set slide index
            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        def previous_slide(self):
            # if on last slide, re-activate "next" button
            button3.config(state="normal")

            # if moving onto the first slide, disable "previous" button
            if self.slide_index == 2:
                button2.config(state=DISABLED)

            Lb1.selection_clear(self.slide_index-1) #clear highlighted listbox item, -1 for string indexing

            self.slide_index -= 1
            Lb1.selection_set(self.slide_index-1) #highlight current listbox item, -1 for string indexing

            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        def next_slide(self):
            # if on first slide, re-activate "previous" button
            button2.config(state="normal")

            # if moving onto the last slide, disable "next" button
            if self.slide_index == 6:
                button3.config(state=DISABLED)

            Lb1.selection_clear(self.slide_index-1)

            self.slide_index += 1
            Lb1.selection_set(self.slide_index-1)

            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)


        Lb1.bind('<<ListboxSelect>>', set_slide) # J: bind set_slide function to listbox onclick event
        button2 = ttk.Button(self, text="Previous", command=lambda: previous_slide(self))
        button2.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button2.grid(row=4, column=2)

        button3 = ttk.Button(self, text="Next", command=lambda: next_slide(self))
        button3.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button3.grid(row=4, column=4)


        next_slide(self)
        button2.config(state=DISABLED)

class test_1(Frame):    #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        self.tstart = datetime.now()  # get current time

        label = Label(self, text="Logic - Test", font=LARGE_FONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        #button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        #button1.grid(padx=10, pady=10)

        self.varQ1A = StringVar()
        self.varQ2A = StringVar()
        self.varQ3A = StringVar()
        self.varQ4T1 = IntVar()
        self.varQ4T2 = IntVar()
        self.varQ4F1 = IntVar()
        self.varQ4F2 = IntVar()
        self.varQ5T = StringVar()
        self.varQ5F1 = StringVar()
        self.varQ5F2 = StringVar()
        self.varQ5F3 = StringVar()

        # test questions===============================================================
        label = Label(self, text="What is a tautology?", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=1, column=0)

        Q1R = Radiobutton(self, text="A correct proposition.", variable=self.varQ1A, value="x1")
        Q1R.grid(row=1, column=1, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="A incorrect proposition.", variable=self.varQ1A, value="y1")
        Q1R.grid(row=1, column=2, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="A always correct proposition.", variable=self.varQ1A, value="t1")
        Q1R.grid(row=2, column=1, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="A always incorrect proposition.", variable=self.varQ1A, value="z1")
        Q1R.grid(row=2, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=3, columnspan=4, sticky=EW)

        label = Label(self, text="De Morgans Law states that...", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=4, column=0)

        Q2R = Radiobutton(self, text="¬qV¬p => ¬(p^q)", variable=self.varQ2A, value="t2")
        Q2R.grid(row=4, column=1, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="p => ¬q", variable=self.varQ2A, value="y2")
        Q2R.grid(row=4, column=2, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="p^q = qVp", variable=self.varQ2A, value="x2")
        Q2R.grid(row=5, column=1, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="q = ¬(¬q)", variable=self.varQ2A, value="z2")
        Q2R.grid(row=5, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=6, columnspan=4, sticky=EW)

        label = Label(self, text="Select the logical equivalent.", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=7, column=0)

        Q3R = Radiobutton(self, text="q^¬p => ¬(q^p)", variable=self.varQ3A, value="x3")
        Q3R.grid(row=7, column=1, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="q => ¬q^¬q", variable=self.varQ3A, value="y3")
        Q3R.grid(row=7, column=2, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="q => p", variable=self.varQ3A, value="z3")
        Q3R.grid(row=8, column=1, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="¬pV¬q => ¬(p^q)", variable=self.varQ3A, value="t3")
        Q3R.grid(row=8, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=9, columnspan=4, sticky=EW)

        label = Label(self, text="Select ALL propositions.", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=10, column=0)

        Q4C = Checkbutton(self, text="x+y-(f(j/k*67.462)) > 1067", variable=self.varQ4T1)
        Q4C.grid(row=10, column=1, sticky=N+E+S+W)
        Q4C = Checkbutton(self, text="The sky is blue", variable=self.varQ4T2)
        Q4C.grid(row=10, column=2, sticky=N+E+S+W)
        Q4C = Checkbutton(self, text="Star Wars or Star Trek", variable=self.varQ4F1)
        Q4C.grid(row=11, column=1, sticky=N+E+S+W)
        Q4C = Checkbutton(self, text="Can I have a drink", variable=self.varQ4F2)
        Q4C.grid(row=11, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=12, columnspan=4, sticky=EW)

        label = Label(self, text="Finish this truth table.", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=13, column=0)

        # truth table, header
        Q5L = Label(self, text="P")
        Q5L.grid(row=13, column=1, sticky=N+E+S+W)
        Q5L = Label(self, text="Q")
        Q5L.grid(row=13, column=2, sticky=N+E+S+W)
        Q5L = Label(self, text="AND")
        Q5L.grid(row=13, column=3, sticky=N+E+S+W)

        # truth table, data
        Q5Tr1 = Label(self, text="T")
        Q5Tr1.grid(row=14, column=1, sticky=N+E+S+W)
        Q5Tr2 = Label(self, text="T")
        Q5Tr2.grid(row=15, column=1, sticky=N+E+S+W)
        Q5Tr3 = Label(self, text="T")
        Q5Tr3.grid(row=14, column=2, sticky=N+E+S+W)
        Q5Tr4 = Label(self, text="T")
        Q5Tr4.grid(row=16, column=2, sticky=N+E+S+W)

        Q5F1 = Label(self, text="F")
        Q5F1.grid(row=15, column=2, sticky=N+E+S+W)
        Q5F2 = Label(self, text="F")
        Q5F2.grid(row=16, column=1, sticky=N+E+S+W)
        Q5F3 = Label(self, text="F")
        Q5F3.grid(row=17, column=1, sticky=N+E+S+W)
        Q5F4 = Label(self, text="F")
        Q5F4.grid(row=17, column=2, sticky=N+E+S+W)

        # truth table input
        Q5I = Entry(self, width=5, textvariable=self.varQ5T)
        Q5I.grid(row=14, column=3, sticky=E)
        Q5I = Entry(self, width=5, textvariable=self.varQ5F1)
        Q5I.grid(row=15, column=3, sticky=E)
        Q5I = Entry(self, width=5, textvariable=self.varQ5F2)
        Q5I.grid(row=16, column=3, sticky=E)
        Q5I = Entry(self, width=5, textvariable=self.varQ5F3)
        Q5I.grid(row=17, column=3, sticky=E)


        button = ttk.Button(self, text="Finish", command=lambda: self.submitTest(controller))
        button.grid(padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))
        button1.grid(padx=10, pady=10)

    def submitTest(self, controller):
        # adding each response to a dictionary
        questions = {
               'Q1': ('t1', self.varQ1A.get()),
               'Q2': ('t2', self.varQ2A.get()),
               'Q3': ('t3', self.varQ3A.get()),
               'Q4': ('1:1:0:0', str(self.varQ4T1.get()) + ':' + str(self.varQ4T2.get()) + ':' + str(self.varQ4F1.get()) + ':' + str(self.varQ4F2.get())),
               'Q5': ('T:F:F:F', str(self.varQ5T.get()) + ':' + str(self.varQ5F1.get()) + ':' + str(self.varQ5F2.get()) + ':' + str(self.varQ5F3.get()))
            }

        # variable to possible error message
        alertMsg = ""

        # check if each individual question has been answered
        if questions['Q1'][1] == "":
            alertMsg = "You must answer the first question"
        if questions['Q2'][1] == "":
            alertMsg = "You must answer the second question"
        if questions['Q3'][1] == "":
            alertMsg = "You must answer the third question"
        if questions['Q4'][1] == "0:0:0:0":
            alertMsg = "You must answer the fourth question"
        if questions['Q5'][1] == ":::":
            alertMsg = "You must answer the fifth question"

        # if alertMsg is blank, all questions been completed
        if alertMsg == "":
            q1 = ""
            q2 = ""
            q3 = ""
            q4 = ""
            q5 = ""

            if questions['Q1'][0] == questions['Q1'][1]:
                q1 = "correct"
            else:
                q1 = "incorrect"

            if questions['Q2'][0] == questions['Q2'][1]:
                q2 = "correct"
            else:
                q2 = "incorrect"

            if questions['Q3'][0] == questions['Q3'][1]:
                q3 = "correct"
            else:
                q3 = "incorrect"

            if questions['Q4'][0] == questions['Q4'][1]:
                q4 = "correct"
            else:
                q4 = "incorrect"

            if questions['Q5'][0] == questions['Q5'][1]:
                q5 = "correct"
            else:
                q5 = "incorrect"

            tm.showinfo("Results", "Your results are\n" + q1 + "\n" + q2 + "\n" + q3 + "\n" + q4 + "\n" + q5)

            #print(questions['Q1'], questions['Q2'], questions['Q3'], questions['Q4'], questions['Q5'])

            tfinish = datetime.now()
            timeElapsed = tfinish - self.tstart
            # timeElapsed = "00:00:00"

            newResult = dqsClass.UserResult("0001", "0001", timeElapsed, questions)

            print(newResult.lessonID)
            print(newResult.userID)
            print(newResult.timeElapsed)
            print(newResult.questions)

            #creating object
            db = shelve.open("responses1.dat", 'n')
            # storing object in Pickle db
            db[newResult.lessonID] = newResult
            db.close()
            #newResult = dqsClass.UserResult("0001", '0001', timeElapsed, questions)
            #db = shelve.open("shelved.dat", 'r')
            #db['0001'] = newResult
            #d.close()

            controller.show_frame(studentMenu)
        else:
            tm.showwarning("Entry Error", alertMsg)


class test_2(Frame):    #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        self.tstart2 = datetime.now()  # get current time

        label = Label(self, text="Sets - Test", font=LARGE_FONT)
        label.grid(row=0, column=1, padx=10, pady=10)

        #button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        #button1.grid(padx=10, pady=10)

        self.SvarQ1A = StringVar()
        self.SvarQ2A = StringVar()
        self.SvarQ3A = StringVar()

        # test questions===============================================================
        label = Label(self, text="What is cardinality?", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=1, column=0)

        Q1R = Radiobutton(self, text="A large set.", variable=self.SvarQ1A, value="x1")
        Q1R.grid(row=1, column=1, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="The length of a set.", variable=self.SvarQ1A, value="t1")
        Q1R.grid(row=1, column=2, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="A mini Pope.", variable=self.SvarQ1A, value="y1")
        Q1R.grid(row=2, column=1, sticky=N+E+S+W)
        Q1R = Radiobutton(self, text="A method of intersection.", variable=self.SvarQ1A, value="z1")
        Q1R.grid(row=2, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=3, columnspan=4, sticky=EW)

        label = Label(self, text="What is a subset?", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=4, column=0)

        Q2R = Radiobutton(self, text="A set containing items that are ALL in another set.", variable=self.SvarQ2A, value="t2")
        Q2R.grid(row=4, column=1, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="A underwater set.", variable=self.SvarQ2A, value="y2")
        Q2R.grid(row=4, column=2, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="U+VC", variable=self.SvarQ2A, value="x2")
        Q2R.grid(row=5, column=1, sticky=N+E+S+W)
        Q2R = Radiobutton(self, text="Z or {0,1,2,3}", variable=self.SvarQ2A, value="z2")
        Q2R.grid(row=5, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=6, columnspan=4, sticky=EW)

        label = Label(self, text="In python, a = set([1,2,3]),", font=LARGE_FONT, relief=RIDGE, width=30)
        label.grid(row=7, column=0)
        label2 = Label(self, text="what is the result of a.add(3)", font=LARGE_FONT, relief=RIDGE, width=30)
        label2.grid(row=8, column=0)

        Q3R = Radiobutton(self, text="[1,2,3,3]", variable=self.SvarQ3A, value="x3")
        Q3R.grid(row=7, column=1, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="[NaN]", variable=self.SvarQ3A, value="y3")
        Q3R.grid(row=7, column=2, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="[1,2,3] + 3", variable=self.SvarQ3A, value="z3")
        Q3R.grid(row=8, column=1, sticky=N+E+S+W)
        Q3R = Radiobutton(self, text="[1,2,3]", variable=self.SvarQ3A, value="t3")
        Q3R.grid(row=8, column=2, sticky=N+E+S+W)

        sep = ttk.Separator(self, orient=HORIZONTAL)
        sep.grid(row=9, columnspan=4, sticky=EW)


        button = ttk.Button(self, text="Finish", command=lambda: self.submitTest2(controller))
        button.grid(padx=10, pady=10)

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))
        button1.grid(padx=10, pady=10)


    def submitTest2(self, controller):
        questions = {
                'Q1': ['t1', self.SvarQ1A.get()],
                'Q2': ['t2', self.SvarQ2A.get()],
                'Q3': ['t3', self.SvarQ3A.get()]
            }

        alertMsg = ""

        if questions['Q1'][1] == "":
            alertMsg = "You must answer the first question"
        if questions['Q2'][1] == "":
            alertMsg = "You must answer the second question"
        if questions['Q3'][1] == "":
            alertMsg = "You must answer the third question"

        # if alertMsg is blank, all questions been completed
        if alertMsg == "":
            q1 = ""
            q2 = ""
            q3 = ""

            if questions['Q1'][0] == questions['Q1'][1]:
                q1 = "correct"
            else:
                q1 = "incorrect"

            if questions['Q2'][0] == questions['Q2'][1]:
                q2 = "correct"
            else:
                q2 = "incorrect"

            if questions['Q3'][0] == questions['Q3'][1]:
                q3 = "correct"
            else:
                q3 = "incorrect"

            tm.showinfo("Results", "Your results are\n" + q1 + "\n" + q2 + "\n" + q3)

            #print(questions['Q1'], questions['Q2'], questions['Q3'])

            # get tiem teken on test
            tfinish = datetime.now()
            timeElapsed = tfinish - self.tstart2

            newResult = dqsClass.UserResult("0001", "0001", timeElapsed, questions)

            print(newResult.lessonID)
            print(newResult.userID)
            print(newResult.timeElapsed)
            print(newResult.questions)

            db = shelve.open("responses2.dat", "n")
            db[newResult.lessonID] = newResult
            db.close()

            controller.show_frame(studentMenu)
        else:
            tm.showwarning("Entry Error", alertMsg)




class lecturerMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Lecturer Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to login", command=lambda: controller.show_frame(login))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="View Results for test 1", command=lambda: controller.show_frame(view_results1))
        button2.pack(padx=10, pady=10)

        button3 = ttk.Button(self, text="View Results for test 2", command=lambda: controller.show_frame(view_results2))
        button3.pack(padx=10, pady=10)
        
        button4 = ttk.Button(self, text="View Average Mark ", command=lambda: controller.show_frame(view_average))
        button4.pack(padx=10, pady=10)
        
class view_average(Frame):  # Alex Mumford
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Average Mark Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) 

        button1 = ttk.Button(self, text="Back to Lecturer Menu", command=lambda: controller.show_frame(lecturerMenu))  
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="View Sets Average", command=lambda: controller.show_frame(view_average_sets))
        button2.pack(padx=10, pady=10)

        button3 = ttk.Button(self, text="View Logic Average", command=lambda: controller.show_frame(view_average_logic)) 
        button3.pack(padx=10, pady=10)

class view_average_sets(Frame):  # Alex Mumford
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Average Sets Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) 
        button1 = ttk.Button(self, text="Back to Average Menu", command=lambda: controller.show_frame(view_average))  
        button1.pack(padx=10, pady=10)



class view_average_logic(Frame):  # Alex Mumford
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Average Logic Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) 
        button1 = ttk.Button(self, text="Back to Average Menu", command=lambda: controller.show_frame(view_average))  
        button1.pack(padx=10, pady=10)


class view_results1(Frame):  #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        #PLACEHOLDER DATA
        userIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score = [4, 6, 2, 8, 9, 0, 5, 6, 5, 6]
        testId = "1"
        #PLACEHOLDER DATA

        maxGrade = 9
        userIdLength = len(userIds)
        plt.bar(userIds, score, align="center")

        plt.xlabel("Students")
        plt.ylabel("Score in test")
        #plt.xticks(userIds)
        plt.title("Results from test " + str(testId))
        plt.axis([1, userIdLength, 0, maxGrade])
        plt.grid(True)
        plt.savefig("plots/plotsaveTest_" + str(testId))


        canvas_width = 750
        canvas_height = 600

        canvas = Canvas(self, width=canvas_width, height=canvas_height)
        canvas.pack(expand=YES, fill=Y, side=LEFT, padx=10, pady=10)

        self.img = PhotoImage(file="plots/plotsaveTest_" + testId + ".png")
        canvas.create_image(0, 0, anchor=NW, image=self.img)



        label = Label(self, text="View Results", font=LARGE_FONT)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(lecturerMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        buttonL2 = ttk.Button(self, text="Sets test results", command=lambda: controller.show_frame(view_results2))
        buttonL2.pack(padx=10, pady=6)

class view_results2(Frame):  #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        #PLACEHOLDER DATA
        userIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        score = [4, 6, 2, 8, 9, 0, 5, 6, 5, 6]
        testId = "2"
        #PLACEHOLDER DATA

        maxGrade = 3
        userIdLength = len(userIds)
        plt.bar(userIds, score, align="center")

        plt.xlabel("Students")
        plt.ylabel("Score in test")
        #plt.xticks(userIds)
        plt.title("Results from test " + str(testId))
        plt.axis([1, userIdLength, 0, maxGrade])
        plt.grid(True)
        plt.savefig("plots/plotsaveTest_" + str(testId))


        canvas_width = 750
        canvas_height = 600

        canvas = Canvas(self, width=canvas_width, height=canvas_height)
        canvas.pack(expand=YES, fill=Y, side=LEFT, padx=10, pady=10)

        self.img = PhotoImage(file="plots/plotsaveTest_" + testId + ".png")
        canvas.create_image(0, 0, anchor=NW, image=self.img)



        label = Label(self, text="View Results", font=LARGE_FONT)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(lecturerMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        buttonL1 = ttk.Button(self, text="Logic test results", command=lambda: controller.show_frame(view_results1))
        buttonL1.pack(padx=10, pady=6)



widthpixels = "1280"
heightpixels = "800"

root = Tk()
root.iconbitmap(default="favicon.ico") # Team 12 Yeahhhh Boiiiii
root.title("DQS - Learn")
root.geometry(widthpixels + "x" + heightpixels)
app = dqsLearn(root)
root.mainloop()
