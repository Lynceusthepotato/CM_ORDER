import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm
import matplotlib
import scipy.stats
import scipy as sp
from matplotlib.figure import Figure

matplotlib.use("TkAgg")
root = tk.Tk()
root.title("Normal Distributions")


def updateGraph(a, b, c, d):
    global CDF
    numberbelow = cdf.get()
    sizeOfTable = d.get()
    if numberbelow == '' or numberbelow == "Enter number to find CDF":
        numberbelow = 0
    if sizeOfTable == '' or sizeOfTable == "Enter the size of the table":
        sizeOfTable = 5
    tofindcdf = float(numberbelow)
    mean = a.get()
    standard_deviation = b.get()
    random = c.get()
    if mean == '' or mean == "Enter the mean":
        mean = 0
    if standard_deviation == '' or standard_deviation == "Enter the standard deviation":
        standard_deviation = 1
    sOT = float(sizeOfTable)
    mu = float(mean)
    sigma = float(standard_deviation)
    rvs = int(random)
    plt.clf()
    x_samples = norm.rvs(size=rvs)
    domain = np.linspace(-sOT, sOT, 1000)
    CDF = sp.stats.norm.cdf(tofindcdf, loc=mu, scale=sigma)
    # plt.hist(x_samples, density=1)
    plt.plot(domain, norm.pdf(domain, mu, sigma))
    f.canvas.draw()


f = plt.figure()
canvas = FigureCanvasTkAgg(f, master=root)
plot_widget = canvas.get_tk_widget()

plot_widget.grid(row=2, column=0)
toolbarFrame = Frame(master=root)
toolbarFrame.grid(row=5, column=0)
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

fora = Entry(root, width=35)
fora.grid(row=0, column=1, columnspan=1)
fora.insert(0, "Enter the mean")

forb = Entry(root, width=35)
forb.grid(row=0, column=2, columnspan=1)
forb.insert(0, "Enter the standard deviation")

forc = Entry(root, width=35)
forc.grid(row=0, column=3, columnspan=1)

ford = Entry(root, width=35)
ford.grid(row=2, column=1, columnspan=1)
ford.insert(0, "Enter the range of x")


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
    # For some reason if the out put is just one decimal it doesnt change the text it just stack them
    printCDF_Label = Label(root, text=CDF)
    printCDF_Label.grid(row=3, column=2)


cdf_Button = Button(root, text="Generate CDF", command=printCDF)
cdf_Button.grid(row=3, column=1)

cdf = Entry(root, width=40)
cdf.grid(row=3, column=0)
cdf.insert(0, "Enter number to find CDF")

tk.IntVar()
tk.Button(root, text="Generate", command=lambda: updateGraph(fora, forb, forc, ford)).grid(row=4, column=0)

root.mainloop()
