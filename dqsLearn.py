from tkinter import *
from tkinter import ttk  # css for tkinter

LARGE_FONT = ("Verdana", 12)

class dqsLearn(Frame): # include inheritance as parameters
    def __init__(self, *args, **kwargs): # args(arguments) = any number of variables kwargs(kewyword arguments) = passing dictionaries/data structures
        # tk.Tk.__init__(self, *args, **kwargs)
        Frame.__init__(self, *args, **kwargs) # Initialise the frame

        container = Frame() # Assign container as a frame which we can alter
        # allow the container to expand into the entire window
        container.pack(side="top", fill="both", expand=True)
        # set up the containing window
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

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
        Frame.__init__(self, parent)

        label = Label(self, text="Login Page", font=LARGE_FONT)
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
        Frame.__init__(self, parent)

        label = Label(self, text="Logic - Lesson", font=LARGE_FONT)
        label.pack(padx=10, pady=10) # temp placement

        button1 = ttk.Button(self, text="Back to menu", command=lambda: controller.show_frame(studentMenu))  # only calls the function when the button is pressed
        button1.pack(padx=10, pady=10)

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


root = Tk()
root.iconbitmap(default="favicon.ico") # Team 12 Yeahhhh Boiiiii
root.title("DQS - Learn")
app = dqsLearn(root)
root.mainloop()