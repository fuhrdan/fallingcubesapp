import tkinter as tk

class FallingCubesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Falling Cubes")
        
        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()
        
        self.canvas.bind("<Button-1>", self.create_cube)
        self.cubes = []
        
    def create_cube(self, event):
        size = 20  # Cube size
        x1, y1 = event.x - size // 2, event.y - size // 2
        x2, y2 = event.x + size // 2, event.y + size // 2
        cube = self.canvas.create_rectangle(x1, y1, x2, y2, fill="blue")
        self.cubes.append((cube, y1))
        self.fall(cube, y1)
        
    def fall(self, cube, y):
        max_y = 380  # Bottom limit
        if y < max_y:
            self.canvas.move(cube, 0, 5)
            self.root.after(50, self.fall, cube, y + 5)

if __name__ == "__main__":
    root = tk.Tk()
    app = FallingCubesApp(root)
    root.mainloop()
