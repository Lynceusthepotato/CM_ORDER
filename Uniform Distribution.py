import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import matplotlib
import scipy.stats
import scipy as sp
from matplotlib.figure import Figure

matplotlib.use("TkAgg")
root = tk.Tk()
root.title("Uniform Distributions")

STD = 0
MU = 0
mean_std = "bruh"


def updateGraph(a, b, c):
    global STD, MU, CDF
    start = a.get()
    end = b.get()
    numberbelow = cdf.get()
    if numberbelow == '' or numberbelow == "Enter number to find probability below that number":
        numberbelow = 0
    tofindcdf = float(numberbelow)
    random = c.get()
    loc_a = float(start)
    loc_b = float(end) - float(start)
    rvs = int(random)
    plt.clf()
    x = sp.stats.uniform(loc=loc_a, scale=loc_b)
    STD = x.std()
    MU = x.mean()
    CDF = x.cdf(tofindcdf)
    global mean_std
    mean_std = "Mean : ", MU, "Standard Deviation : ", STD
    x_samples = x.rvs(rvs)
    plt.hist(x_samples, density=1, bins=50, edgecolor="k")
    plt.plot(x_samples, x.pdf(x_samples), lw=5)
    f.canvas.draw()


f = plt.figure(1)

canvas = FigureCanvasTkAgg(f, master=root)
plot_widget = canvas.get_tk_widget()

plot_widget.grid(row=2, column=0)
toolbarFrame = Frame(master=root)
toolbarFrame.grid(row=5, column=0)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

fora = Entry(root, width=35)
fora.grid(row=0, column=1, columnspan=1)
fora.insert(0, "enter the minimum")

forb = Entry(root, width=35)
forb.grid(row=0, column=2, columnspan=1)
forb.insert(0, "enter the maximum")

forc = Entry(root, width=35)
forc.grid(row=0, column=3, columnspan=1)


def rvsChanger(number):
    forc.delete(0, END)
    forc.insert(0, int(number))


rvs_Label = Label(root, text="RVS")
rvs_Label.grid(row=1, column=0)

button_1 = Button(root, text="500", padx=20, pady=10, command=lambda: rvsChanger(500))
button_2 = Button(root, text="1000", padx=20, pady=10, command=lambda: rvsChanger(1000))
button_3 = Button(root, text="1500", padx=20, pady=10, command=lambda: rvsChanger(1500))

button_1.grid(row=1, column=1)
button_2.grid(row=1, column=2)
button_3.grid(row=1, column=3)


def printCDF():
    printCDF_Label = Label(root, text=CDF)
    printCDF_Label.grid(row=3, column=2)


def printmean_std():
    # For some reason if the out put is just one decimal it doesnt change the text it just stack them
    mean_std_Label = Label(root, text=mean_std)
    mean_std_Label.grid(row=2, column=2)


mean_std_Button = Button(root, text="Generate mean and std", command=printmean_std)
mean_std_Button.grid(row=2, column=1)

cdf_Button = Button(root, text="Generate CDF", command=printCDF)
cdf_Button.grid(row=3, column=1)

cdf = Entry(root, width=40)
cdf.grid(row=3, column=0)
cdf.insert(0, "Enter number to find probability below that number")

tk.IntVar()
tk.Button(root, text="Generate", command=lambda: updateGraph(fora, forb, forc)).grid(row=4, column=0)

root.mainloop()
