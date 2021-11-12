import tkinter as tk

root = tk.Tk()

c = tk.Canvas(root, bg="white", height=700, width=700)

# Drawing pacman's face
radius = 150
center_pos = (350, 350)
coord = center_pos[0] - radius, center_pos[1] - radius, center_pos[0] + radius, center_pos[1] + radius
pacman_face = c.create_arc(coord, start=-40, extent=-280, fill="yellow")

# Drawing pacman's eye
eye_rad = 15
eye_pos = (350 + eye_rad, 350 - radius/2)
coord = eye_pos[0] - eye_rad, eye_pos[1] - eye_rad, eye_pos[0] + eye_rad, eye_pos[1] + eye_rad
pacman_eye = c.create_oval(coord, fill="black")

c.pack()

root.mainloop()