from tkinter import *
from tkinter import ttk  # css for tkinter
from tkinter import messagebox
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

        for page in (login, studentMenu, lesson_1, lesson_2, test_1, lecturerMenu, view_results):
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

        button2 = ttk.Button(self, text="Begin logic lesson", command=lambda: controller.show_frame(lesson_1))
        button2.pack(padx=10, pady=10)

        # ?? This should be disabled (greyed out) until the lesson has been completed ??
        button3 = ttk.Button(self, text="Begin logic test", command=lambda: controller.show_frame(test_1))
        button3.pack(padx=10, pady=10)

        button4 = ttk.Button(self, text="Begin sets lesson", command=lambda: controller.show_frame(lesson_2))
        button4.pack(padx=10, pady=10)


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

class test_1(Frame):    #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.tstart = datetime.now()  # get current time

        label = Label(self, text="Logic - Test", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        #button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        #button1.pack(padx=10, pady=10)

        # test questions===============================================================
        label = Label(self, text="What is a tautology?", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        label = Label(self, text="De Morgans Law states that...", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        label = Label(self, text="Select the logical equivalent.", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        label = Label(self, text="Select ALL propositions.", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        label = Label(self, text="Finish this truth table.", font=LARGE_FONT)
        label.pack(padx=10, pady=10)
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
        Q1R.pack(padx=10, pady=10)
        Q1R = Radiobutton(self, text="A incorrect proposition.", variable=self.varQ1A, value="y1")
        Q1R.pack(padx=10, pady=10)
        Q1R = Radiobutton(self, text="A always correct proposition.", variable=self.varQ1A, value="t1")
        Q1R.pack(padx=10, pady=10)
        Q1R = Radiobutton(self, text="A always incorrect proposition.", variable=self.varQ1A, value="z1")
        Q1R.pack(padx=10, pady=10)

        Q2R = Radiobutton(self, text="¬qV¬p => ¬(p^q)", variable=self.varQ2A, value="t2")
        Q2R.pack(padx=10, pady=10)
        Q2R = Radiobutton(self, text="p => ¬q", variable=self.varQ2A, value="y2")
        Q2R.pack(padx=10, pady=10)
        Q2R = Radiobutton(self, text="p^q = qVp", variable=self.varQ2A, value="x2")
        Q2R.pack(padx=10, pady=10)
        Q2R = Radiobutton(self, text="q = ¬(¬q)", variable=self.varQ2A, value="z2")
        Q2R.pack(padx=10, pady=10)

        Q3R = Radiobutton(self, text="q^¬p => ¬(q^p)", variable=self.varQ3A, value="x3")
        Q3R.pack(padx=10, pady=10)
        Q3R = Radiobutton(self, text="q => ¬q^¬q", variable=self.varQ3A, value="y3")
        Q3R.pack(padx=10, pady=10)
        Q3R = Radiobutton(self, text="q => p", variable=self.varQ3A, value="z3")
        Q3R.pack(padx=10, pady=10)
        Q3R = Radiobutton(self, text="¬pV¬q => ¬(p^q)", variable=self.varQ3A, value="t3")
        Q3R.pack(padx=10, pady=10)

        Q4C = Checkbutton(self, text="x+y-(f(j/k*67.462)) > 1067", variable=self.varQ4T1)
        Q4C.pack(padx=10, pady=10)
        Q4C = Checkbutton(self, text="The sky is blue", variable=self.varQ4T2)
        Q4C.pack(padx=10, pady=10)
        Q4C = Checkbutton(self, text="Star Wars or Star Trek", variable=self.varQ4F1)
        Q4C.pack(padx=10, pady=10)
        Q4C = Checkbutton(self, text="Can I have a drink", variable=self.varQ4F2)
        Q4C.pack(padx=10, pady=10)

        # truth table, header
        Q5L = Label(self, text="P")
        Q5L.pack(padx=10, pady=10)
        Q5L = Label(self, text="Q")
        Q5L.pack(padx=10, pady=10)
        Q5L = Label(self, text="AND")
        Q5L.pack(padx=10, pady=10)

        # truth table, data
        Q5Tr1 = Label(self, text="T")
        Q5Tr1.pack(padx=10, pady=10)
        Q5Tr2 = Label(self, text="T")
        Q5Tr2.pack(padx=10, pady=10)
        Q5Tr3 = Label(self, text="T")
        Q5Tr3.pack(padx=10, pady=10)
        Q5Tr4 = Label(self, text="T")
        Q5Tr4.pack(padx=10, pady=10)

        Q5F1 = Label(self, text="F")
        Q5F1.pack(padx=10, pady=10)
        Q5F2 = Label(self, text="F")
        Q5F2.pack(padx=10, pady=10)
        Q5F3 = Label(self, text="F")
        Q5F3.pack(padx=10, pady=10)
        Q5F4 = Label(self, text="F")
        Q5F4.pack(padx=10, pady=10)

        # truth table input
        Q5I = Entry(self, width=1, textvariable=self.varQ5T)
        Q5I.pack(padx=10, pady=10)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F1)
        Q5I.pack(padx=10, pady=10)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F2)
        Q5I.pack(padx=10, pady=10)
        Q5I = Entry(self, width=1, textvariable=self.varQ5F3)
        Q5I.pack(padx=10, pady=10)
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

        button = ttk.Button(self, text="Finish", command=self.submitTest())
        button.pack(padx=10, pady=10)

    def submitTest(self):
        questions = {
               'Q1': ('t1', self.varQ1A),
               'Q2': ('t2', self.varQ2A),
               'Q3': ('t3', self.varQ3A),
               'Q4': ('1:1:1:1', str(self.varQ4T1) + ':' + str(self.varQ4T2) + ':' + str(self.varQ4F1) + ':' + str(self.varQ4F2))
            }

        tfinish = datetime.now()
        timeElapsed = tfinish - self.tstart

        newResult = dqsClass.UserResult("0001", '0001', timeElapsed, questions)

        #db = shelve.open("shelved.dat", 'r')

        #db['0001'] = newResult

        #d.close()

        #controller.show_frame(studentMenu)

class lecturerMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=BACKGROUND_COLOUR_DARKER)

        label = Label(self, text="Lecturer Menu", font=LARGE_FONT, fg="white", bg=BACKGROUND_COLOUR_DARKER)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to login", command=lambda: controller.show_frame(login))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

        button2 = ttk.Button(self, text="View Results", command=lambda: controller.show_frame(view_results))
        button2.pack(padx=10, pady=10)


class view_results(Frame):  #Dom Routley
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

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

        buttonL1 = ttk.Button(self, text="Lesson 1 test", state=DISABLED)
        buttonL1.pack(padx=10, pady=6)

        buttonL2 = ttk.Button(self, text="Lesson 2 test", state=DISABLED)
        buttonL2.pack(padx=10, pady=6)


widthpixels = "1000"
heightpixels = "800"

root = Tk()
root.iconbitmap(default="favicon.ico") # Team 12 Yeahhhh Boiiiii
root.title("DQS - Learn")
root.geometry(widthpixels + "x" + heightpixels)
app = dqsLearn(root)
root.mainloop()