import tkinter as tk
from draw import Triangle, VectorTriangle

if __name__ == '__main__':
    root = tk.Tk()

    canv = tk.Canvas(root, bg="white", height=1700, width=1700)

    t1 = VectorTriangle([3,7,5])
    t1.draw_on_tkcanvas(canv, "red")

    t2 = Triangle([8,8,8])
    t2.draw_on_tkcanvas(canv, "blue", pos=(20, 270))

    t3 = VectorTriangle([10,13,15])
    t3.draw_on_tkcanvas(canv, "green", pos=(520, 270))

    canv.pack()

    root.mainloop()