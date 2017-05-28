import json
import urllib
import tkinter as tk
from tkinter import ttk

import matplotlib
import pandas as pd
import numpy as np
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib import animation
from matplotlib import style


LARGE_FONT = ('Verdana', 12)
style.use('ggplot')

figure = Figure(figsize=(5, 5), dpi=100)
subplot = figure.add_subplot(111)
        

def animate(i):
    pull_data = open('sample_data.txt', 'r').read()
    data_list = pull_data.split('\n')
    x_list = []
    y_list = []

    for each_line in data_list:
        if len(each_line) > 1:
            x, y = each_line.split(',')
            x_list.append(int(x))
            y_list.append(int(y))

    subplot.clear()
    subplot.plot(x_list, y_list)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default='icon.ico')
        tk.Tk.wm_title(self, 'Sea of BTC client')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='ALPHA Bitcoin trading application use at your own risk. There is no promise of warranty', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self, 
            text='Agree', 
            command=lambda: controller.show_frame(BTCe_Page)
        )
        button1.pack()
        button2 = ttk.Button(self, text='Disagree', command=quit)
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Page One', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self,
            text='Back to Home',
            command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()


class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text='Graph Page', font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(
            self,
            text='Back to Home',
            command=lambda: controller.show_frame(StartPage)
        )
        button1.pack()

        canvas = FigureCanvasTkAgg(figure, self)
        canvas.show()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        
        toolbar = NavigationToolbar2TkAgg(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


if __name__ == '__main__':
    app = SeaofBTCapp()
    anime = animation.FuncAnimation(figure, animate, interval=1000)
    app.mainloop()
