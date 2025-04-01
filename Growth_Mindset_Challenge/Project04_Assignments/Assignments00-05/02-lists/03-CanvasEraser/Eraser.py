#Libraries
import random
import tkinter as tk

'''----------Making An Eraser for Canvas--------------'''

class EraserApp():
    def __init__(self,root):
        self.root =root
        self.root.title("Magic Eraser Canvas")

        #Creating a canvas
        self.canvas = tk.Canvas(root, width=500, height=500, bg="white")
        self.canvas.pack()

        #Setting up the Grid 
        self.cell_size = 25
        self.grid = []

        #Randomizing colors for unique effect
        colors = ["#1E90FF", "#4169E1", "#4682B4", "#5F9EA0", "#6495ED"]

        #Drawing Colorful grid
        for i in range(0, 500, self.cell_size):
            row = []
            for j in range(0, 500, self.cell_size):
                color = random.choice(colors)
                rect = self.canvas.create_rectangle(j, i, j+self.cell_size, i+self.cell_size, fill=color, outline="black")
                row.append(rect)
            self.grid.append(row)

        #Making the shape of eraser in circular form
        self.eraser = self.canvas.create_oval(0, 0, 50, 50, fill="gray", outline="black")

        #Binding mouse events for dragging
        self.canvas.bind("<B1-Motion>", self.move_eraser)

    # Creating a function just to clarify the abilities of eraser
    def move_eraser(self, event):
        """Move eraser and erase cells it touches."""
        x1, y1, x2, y2 = self.canvas.coords(self.eraser)
        dx, dy = event.x - (x1 + (x2 - x1) / 2), event.y - (y1 + (y2 - y1) / 2)
        self.canvas.move(self.eraser, dx, dy)

        #for eraser overlapping cells with a fadding effect
        for row in self.grid:
            for rect in row:
                rx1, ry1, rx2, ry2 = self.canvas.coords(rect)
                if not (rx2 < x1 or rx1 > x2 or ry2 < y1 or ry1 > y2):
                    self.canvas.itemconfig(rect, fill="white", outline="white")

if __name__ == '__main__':
    root = tk.Tk()
    app = EraserApp(root)
    root.mainloop()

