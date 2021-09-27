import tkinter as tk

# initialize window
from tkinter import LEFT

root = tk.Tk()
root.geometry('600x600+0+0')
root.title('Buttons')


def settings():
    settings_win = tk.Toplevel()
    settings_win.geometry("1000x1000")
    settings_win.title("Settings")


photo = tk.PhotoImage(file="se.png")
photo_image = photo.subsample(7, 10)
settings_Btn = tk.Button(root, text="Settings", image=photo_image, command=settings, bg="green", compound=LEFT)
settings_Btn.place(x=20, y=50)

photo2 = tk.PhotoImage(file="analytics1.png")
photo_image2 = photo2.subsample(5, 7)
reports_Btn = tk.Button(root, text="Reports", image=photo_image2, command=settings, bg="green", compound=LEFT)
reports_Btn.place(x=20, y=100)

photo3 = tk.PhotoImage(file="peso.png")
photo_image3 = photo3.subsample(12, 21)
payroll_Btn = tk.Button(root, text="Payroll", image=photo_image3, command=settings, bg="green", compound=LEFT)
payroll_Btn.place(x=20, y=150)

photo4 = tk.PhotoImage(file="logout.png")
photo_image4 = photo4.subsample(12, 19)
logout_Btn = tk.Button(root, text="Logout", image=photo_image4, command=settings, bg="green", compound=LEFT)
logout_Btn.place(x=20, y=200)

photo5 = tk.PhotoImage(file="dashboard.png")
photo_image5 = photo5.subsample(25, 20)
dashboard_Btn = tk.Button(root, text="Dashboard", image=photo_image5, command=settings, bg="green", compound=LEFT)
dashboard_Btn.place(x=20, y=250)

photo6 = tk.PhotoImage(file="loans.png")
photo_image6 = photo6.subsample(12, 19)
loans_Btn = tk.Button(root, text="Loans", image=photo_image6, command=settings, bg="green", compound=LEFT)
loans_Btn.place(x=20, y=300)



root.mainloop()
