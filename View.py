import tkinter as tk


class View:

    def setGridView(self, grid):

        r = 0
        for row in grid:
            self.fr_map.columnconfigure(r, weight=1)
            self.fr_map.rowconfigure(r, weight=1)
            c = 0
            for tile in row:
                frame = tk.Frame(
                    master=self.fr_map,
                    relief=tk.RAISED,
                    borderwidth=1
                )

                canvas = tk.Canvas(master=frame)
                canvas.text = canvas.create_text(0,
                                0,
                                text=tile)
                
            
           

                # Set propagate to false to prevent frames from wrapping content
                frame.propagate(0)
                frame.grid(row=r, column=c, sticky="nsew")

                # label = tk.Label(master=frame, text=col)
                # label.pack()

                c += 1
            r += 1
        self.updateGridTextPosition()


    def updateGridTextPosition(self):
        """ reposition text in frame map frames """
        
        self.fr_map.update_idletasks()
        frame : tk.Frame
        for frame in self.fr_map.winfo_children():
            canvas : tk.Canvas
            for canvas in frame.winfo_children():
                canvas.coords(canvas.text, frame.winfo_width()/2,
                                frame.winfo_height()/2)
                print (canvas.coords(canvas.text))
                canvas.pack()      


    # def save_file(self):
    #     """Save the current file as a new file."""

    #     filepath = asksaveasfilename(

    #         defaultextension="txt",
    #         filetypes=[("Sausage Files", "*.csv"), ("All Files", "*.*")],
    #     )

    #     if not filepath:
    #         return

    #     with open(filepath, "w") as output_file:
    #         text = self.txt_edit.get("1.0", tk.END)
    #         output_file.write(text)

    #     self.window.title(f"Sausage Solver - {filepath}")

    def onConfigure(self, event):
        print("onConfigure")
        self.updateGridTextPosition()
        # print(str(fr_map.winfo_children()))

    def __init__(self, window):
        self.window = window
        self.fr_map = tk.Frame(window)
        self.txt_edit = tk.Text(window)
        self.fr_buttons = tk.Frame(window)
        window.title("Sausage Solver")

        # One row, which grows proportionally
        self.window.rowconfigure(0, weight=1, minsize=200)

        # The main window has two columns, the first of which has a fixed width,
        # and this one, which will grow and shrink proportionally
        self.window.columnconfigure(1, weight=3, minsize=200)

        self.btn_open = tk.Button(self.fr_buttons, text="Open")
        self.btn_save = tk.Button(self.fr_buttons, text="Save As...")

        self.btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
        self.btn_save.grid(row=1, column=0, sticky="ew", padx=5)

        self.fr_buttons.grid(row=0, column=0, sticky="ns")
        # txt_edit.grid(row=0, column=1, sticky="nsew")
        self.fr_map.grid(row=0, column=1, sticky="nsew")

        self.fr_map.bind(sequence='<Configure>', func=self.onConfigure)
