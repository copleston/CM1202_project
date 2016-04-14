from tkinter import *
from tkinter import ttk  # css for tkinter
from tkinter import messagebox

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
        Frame.__init__(self, parent)

        label = Label(self, text="Student Menu", font=LARGE_FONT)
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
        canvas.pack(expand=YES, fill=Y, side=LEFT)
        #canvas.grid(row=2, column=0, rowspan=1)            

        Lb1 = Listbox(self, bg=BACKGROUND_RED, selectmode=SINGLE, selectbackground="#AD423E")#create listbox object,
        Lb1.insert(1, "Propositional Logic")
        Lb1.insert(2, "Combining Propositions")#add the listbox options
        Lb1.insert(3, "Truth Tables")
        Lb1.insert(4, "Implication")
        Lb1.insert(5, "Tautologies")
        Lb1.insert(6, "De Morgan's Laws")
        Lb1.pack(side=LEFT) #display listbox to screen, hug left of lesson slide

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
        button2.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)
        #button2.grid(row=4, column=2)

        button3 = ttk.Button(self, text="Next", command=lambda: next_slide(self))
        button3.pack(side=BOTTOM, anchor=SE, padx=10, pady=10)
        #button3.grid(row=4, column=4)


        next_slide(self)
        button2.config(state=DISABLED)


class test_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Logic - Test", font=LARGE_FONT)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)


class lecturerMenu(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = Label(self, text="Lecturer Menu", font=LARGE_FONT)
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