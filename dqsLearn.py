from tkinter import *
from tkinter import ttk  # css for tkinter
from tkinter import messagebox
from datetime import datetime
#from dqsClass import *

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

        for page in (login, studentMenu, lesson_1, test_1, lecturerMenu, view_results):
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
        label = Label(self, text="Login Page", font=LARGE_FONT, bg=BACKGROUND_COLOUR_DARKER, fg="white")
        label.pack(padx=10, pady=10)

        # button1 = Button(self, text="Student Login", command=studentMenu) # calls the function immediately
        button1 = ttk.Button(self, text="Student Login", command=lambda: controller.show_frame(studentMenu)) # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)
        button2 = ttk.Button(self, text="Lecturer Login", command=lambda: controller.show_frame(lecturerMenu))  # only calls the function when the button is pressed
        button2.pack(padx=10, pady=10)

class studentMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Student Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to login", command=lambda: controller.show_frame(login))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="Begin lesson", command=lambda: controller.show_frame(lesson_1))
        button2.pack(padx=10, pady=10)

        # ?? This should be disabled (greyed out) until the lesson has been completed ??
        button3 = ttk.Button(self, text="Begin test", command=lambda: controller.show_frame(test_1))
        button3.pack(padx=10, pady=10)


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
        def set_slide(self):
            pass

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
            if self.slide_index == 5:
                button3.config(state=DISABLED)
            
            Lb1.selection_clear(self.slide_index-1)

            self.slide_index += 1
            Lb1.selection_set(self.slide_index-1)

            self.img = PhotoImage(file=self.slides.get(self.slide_index))
            canvas.create_image(0, 0, anchor=NW, image=self.img)
            print(self.slide_index)

        button2 = ttk.Button(self, text="Previous", command=lambda: previous_slide(self))
        button2.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button2.grid(row=4, column=2)

        button3 = ttk.Button(self, text="Next", command=lambda: next_slide(self))
        button3.pack(side=TOP, padx=10, pady=10, anchor=NE)
        #button3.grid(row=4, column=4)


        next_slide(self)
        button2.config(state=DISABLED)


class test_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        tstart = datetime.now()  # get current time

        label = Label(self, text="Logic - Test", font=LARGE_FONT)
        label.grid(row=1, column=1, columnspan=3)

        #button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        #button1.pack(padx=10, pady=10)

        # test questions===============================================================
        label = Label(self, text="What is a tautology?", font=LARGE_FONT)
        label.grid(row=2, column=3)

        label = Label(self, text="De Morgans Law states that...", font=LARGE_FONT)
        label.grid(row=7, column=3)

        label = Label(self, text="Select the logical equivalent.", font=LARGE_FONT)
        label.grid(row=12, column=3)

        label = Label(self, text="Select ALL propositions.", font=LARGE_FONT)
        label.grid(row=17, column=3)

        label = Label(self, text="Finish this truth table.", font=LARGE_FONT)
        label.grid(row=22, column=3)
        # ============================================================================

        # variable initilisation
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

        # test answer area============================================================
        Q1R = Radiobutton(self, text="A correct proposition.", variable=self.varQ1A, value="x1")
        Q1R.grid(row=3, column=3, sticky=W)
        Q1R = Radiobutton(self, text="A incorrect proposition.", variable=self.varQ1A, value="y1")
        Q1R.grid(row=4, column=3, sticky=W)
        Q1R = Radiobutton(self, text="A always correct proposition.", variable=self.varQ1A, value="t1")
        Q1R.grid(row=5, column=3, sticky=W)
        Q1R = Radiobutton(self, text="A always incorrect proposition.", variable=self.varQ1A, value="z1")
        Q1R.grid(row=6, column=3, sticky=W)

        Q2R = Radiobutton(self, text="¬qV¬p => ¬(p^q)", variable=self.varQ2A, value="t2")
        Q2R.grid(row=8, column=3, sticky=W)
        Q2R = Radiobutton(self, text="p => ¬q", variable=self.varQ2A, value="y2")
        Q2R.grid(row=9, column=3, sticky=W)
        Q2R = Radiobutton(self, text="p^q = qVp", variable=self.varQ2A, value="x2")
        Q2R.grid(row=10, column=3, sticky=W)
        Q2R = Radiobutton(self, text="q = ¬(¬q)", variable=self.varQ2A, value="z2")
        Q2R.grid(row=11, column=3, sticky=W)

        Q3R = Radiobutton(self, text="q^¬p => ¬(q^p)", variable=self.varQ3A, value="x3")
        Q3R.grid(row=13, column=3, sticky=W)
        Q3R = Radiobutton(self, text="q => ¬q^¬q", variable=self.varQ3A, value="y3")
        Q3R.grid(row=14, column=3, sticky=W)
        Q3R = Radiobutton(self, text="q => p", variable=self.varQ3A, value="z3")
        Q3R.grid(row=15, column=3, sticky=W)
        Q3R = Radiobutton(self, text="¬pV¬q => ¬(p^q)", variable=self.varQ3A, value="t3")
        Q3R.grid(row=16, column=3, sticky=W)

        Q4C = Checkbutton(self, text="x+y-(f(j/k*67.462)) > 1067", variable=self.varQ4T1)
        Q4C.grid(row=18, column=3, sticky=W)
        Q4C = Checkbutton(self, text="The sky is blue", variable=self.varQ4T2)
        Q4C.grid(row=19, column=3, sticky=W)
        Q4C = Checkbutton(self, text="Star Wars or Star Trek", variable=self.varQ4F1)
        Q4C.grid(row=20, column=3, sticky=W)
        Q4C = Checkbutton(self, text="Can I have a drink", variable=self.varQ4F2)
        Q4C.grid(row=21, column=3, sticky=W)

        # truth table, header
        Q5L = Label(self, text="P")
        Q5L.grid(row=23, column=1, sticky=W)
        Q5L = Label(self, text="Q")
        Q5L.grid(row=23, column=2, sticky=W)
        Q5L = Label(self, text="AND")
        Q5L.grid(row=23, column=3, sticky=W)

        # truth table, data
        Q5Tr1 = Label(self, text="T")
        Q5Tr1.grid(row=24, column=1, sticky=W)
        Q5Tr2 = Label(self, text="T")
        Q5Tr2.grid(row=25, column=1, sticky=W)
        Q5Tr3 = Label(self, text="T")
        Q5Tr3.grid(row=24, column=2, sticky=W)
        Q5Tr4 = Label(self, text="T")
        Q5Tr4.grid(row=26, column=2, sticky=W)

        Q5F1 = Label(self, text="F")
        Q5F1.grid(row=26, column=1, sticky=W)
        Q5F2 = Label(self, text="F")
        Q5F2.grid(row=27, column=1, sticky=W)
        Q5F3 = Label(self, text="F")
        Q5F3.grid(row=25, column=2, sticky=W)
        Q5F4 = Label(self, text="F")
        Q5F4.grid(row=27, column=2, sticky=W)

        # truth table input
        Q5I = Entry(self, width=1, textvariable=self.varQ5T)
        Q5I.grid(row=24, column=3)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F1)
        Q5I.grid(row=25, column=3)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F2)
        Q5I.grid(row=26, column=3)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F3)
        Q5I.grid(row=27, column=3)
        # ====================================================================================================


        # sort variables
        # LIAM LIAM LIAM==============================================================================================================================================
        # THIS THIS THIS==============================================================================================================================================
        # BIT BIT BIT=================================================================================================================================================
        # the variables are saved as question numbers, they contain a number that pertains to the number of points that the user has scored from that question.
        # variables you want are question1, question2, question3, question4, question5, time

        if self.varQ1A == "t1":
            self.question1 = 1
        else:
            self.question1 = 0

        if self.varQ2A == "t2":
            self.question2 = 1
        else:
            self.question2 = 0

        if self.varQ3A == "t3":
            self.question3 = 1
        else:
            self.question3 = 0

        question4 = 0
        if self.varQ4T1.get() == 1:
            self.question4 = 1
        if self.varQ4T2.get() == 1:
            self.question4 = question4 + 1
        if self.varQ4F1.get() == 1:
            self.question4 = question4 - 1
        if self.varQ4F2.get() == 1:
            self.question4 = question4 - 1
        if question4 < 0:
            self.question4 = 0

        if self.varQ5T == "T" and self.varQ5F1 == "F" and self.varQ5F2 == "F" and self.varQ5F3 == "F":
            self.question5 = 4
        else:
            self.question5 = 0

        button = ttk.Button(self, text="Finish", command=lambda: controller.show_frame(studentMenu))
        button.grid(row=28, column=2, padx=10, pady=10)

        def submitTest(self):
            questions = {
                'Q1': ('t1', self.varQ1A),
                'Q2': ('t2', self.varQ2A),
                'Q3': ('t3', self.varQ3A),
                'Q4': ('1:1:1:1',
                       str(self.varQ4T1) + ':' + str(self.varQ4T2) + ':' + str(self.varQ4F1) + ':' + str(self.varQ4F2))
            }

            tfinish = datetime.now()
            timeElapsed = tfinish - self.tstart

            newResult = dqsClass.UserResult("0001", userID, timeElapsed, questions)

            db = shelve.open("shelved.dat")

            db[userID] = newResult

            d.close()

            controller.show_frame(studentMenu)

class lecturerMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Lecturer Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to login", command=lambda: controller.show_frame(login))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="View Results", command=lambda: controller.show_frame(view_results))
        button2.pack(padx=10, pady=10)


class view_results(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="View Results", font=LARGE_FONT)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(lecturerMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)


widthpixels = "1000"
heightpixels = "800"

root = Tk()
root.iconbitmap(default="favicon.ico") # Team 12 Yeahhhh Boiiiii
root.title("DQS - Learn")
root.geometry(widthpixels + "x" + heightpixels)
app = dqsLearn(root)
root.mainloop()