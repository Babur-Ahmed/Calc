#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division
from Tkinter import *
from math import *
import webbrowser


'''
TODO:
Create a calculator with a complete graphic user interface (GUI).
Calculator must have the following functionality:
1- Performance of all arithmetic operations.
2- Addition, subtraction, multiplication and division functions.
3- Square root, cube root, cubes, squares and decimals.
4- Generation of mathematical tables in a separate window.
5- CE, C.
6- About and exit dropdown menu.
'''


class Calculator:

    @classmethod
    def __init__(cls, master):
        master.wm_title('Calculator')
        # Create text box which shows input and output
        cls.resultbox = Entry(master, width=22, justify='right',
                              font="Helvetica 15")
        cls.resultbox.bind('<Return>', cls.evalonreturn)
        cls.resultbox.grid(row=0, column=0, columnspan=5, sticky=W)
        cls.resultbox.focus_set()

        # Create dropdown menu
        cls.menu = Menu(master)
        master.config(menu=cls.menu)

        cls.subMenu = Menu(cls.menu, tearoff=0)
        cls.subMenu.add_separator()
        cls.menu.add_cascade(label='Help', menu=cls.subMenu)
        cls.subMenu.add_command(label='About', command=cls.displayAboutMenu)
        cls.subMenu.add_separator()
        cls.subMenu.add_command(label='Exit', command=master.destroy)

        # Add number buttons
        cls.x = '789456123'
        cls.i = 0
        cls.number_buttons = []
        for current_row in xrange(1, 4):
            for current_column in xrange(1, 4):
                cls.b = Button(master, text=cls.x[cls.i], width=7, height=4)
                cls.number_buttons.append(cls.b)
                cls.number_buttons[cls.i].grid(
                    row=current_row, column=current_column, pady=0, sticky='W')
                cls.number_buttons[cls.i]['command'] = lambda currbtn = cls.x[cls.i]: cls.resultbox.insert(
                    END, currbtn)
                cls.i += 1

        # Zero button
        cls.zerobttn = Button(master, text='0', width=7, height=4,
                              command=lambda: cls.resultbox.insert(END, '0'))
        cls.zerobttn.grid(row=4, column=2)

        # Clear button
        cls.clearbttn = Button(master, text='C', width=7, height=4,
                               command=lambda: cls.resultbox.delete(0, END))
        cls.clearbttn.grid(row=5, column=4)

        # Raise to power Button
        cls.expbttn = Button(master, text='Power', width=7, height=4,
                             command=lambda: cls.resultbox.insert(END, 'pow()'))
        cls.expbttn.grid(row=5, column=2)

        # Square root Button
        cls.sqrtbttn = Button(master, text='√', width=7, height=4,
                              command=lambda: cls.resultbox.insert(END, 'sqrt()'))
        cls.sqrtbttn.grid(row=5, column=3)

        # Decimal button
        cls.decimalbttn = Button(master, text='.', width=7, height=4,
                                 command=lambda: cls.resultbox.insert(END, '.'))
        cls.decimalbttn.grid(row=4, column=1)

        # Math table generator button
        cls.mathtables = Button(master, text='Generate\n Math\n Tables',
                                width=7, height=4, command=cls.mathtablegenwindow)
        cls.mathtables.grid(row=5, column=1)

        # Evaluate button
        cls.equals = Button(master, text='=', width=7, height=4, command=cls.evalonequals)
        cls.equals.grid(row=4, column=3)

        # Addition button
        cls.add = Button(master, text='+', width=7, height=4,
                         command=lambda: cls.resultbox.insert(END, '+'))
        cls.add.grid(row=1, column=4)

        # Subtraction button
        cls.subtract = Button(master, text='-', width=7, height=4,
                              command=lambda: cls.resultbox.insert(END, '-'))
        cls.subtract.grid(row=2, column=4)

        # Multiplication button
        cls.multiply = Button(master, text='x', width=7, height=4,
                              command=lambda: cls.resultbox.insert(END, '*'))
        cls.multiply.grid(row=3, column=4)
        # Division button
        cls.divide = Button(master, text='÷', width=7, height=4,
                            command=lambda: cls.resultbox.insert(END, '/'))
        cls.divide.grid(row=4, column=4)

    @classmethod
    def evalonreturn(cls, event):
        # Error catch when nothing is input
        try:
            if (cls.resultbox.get() == ''):
                pass
            else:
                cls.result = eval(cls.resultbox.get())
                cls.resultbox.delete(0, END)
                cls.resultbox.insert(END, cls.result)
        except SyntaxError:
            pass

    @classmethod
    def evalonequals(cls):
        # Error catch when nothing is input
        try:
            if (cls.resultbox.get() == ''):
                pass
            else:
                cls.resultequals = eval(cls.resultbox.get())
                cls.resultbox.delete(0, END)
                cls.resultbox.insert(END, cls.resultequals)
        except SyntaxError:
            pass

    @classmethod
    def mathtablegenwindow(cls):
        cls.tablerange = Tk()
        cls.tablerange.resizable(False, False)
        cls.tablerange.wm_title('Math table range')
        cls.intlabel = Label(cls.tablerange, text='Integer')
        cls.intlabel.grid(row=0, column=0)
        cls.intenter = Entry(cls.tablerange)
        cls.intenter.grid(row=0, column=1)
        cls.startlabel = Label(cls.tablerange, text='Starting range\n of table')
        cls.startlabel.grid(row=1, column=0)
        cls.startrangein = Entry(cls.tablerange)
        cls.startrangein.grid(row=1, column=1)
        cls.endlabel = Label(cls.tablerange, text='End range\n of table')
        cls.endlabel.grid(row=2, column=0)
        cls.endrangein = Entry(cls.tablerange)
        cls.endrangein.grid(row=2, column=1)
        cls.inbutton = Button(cls.tablerange, text='OK', command=cls.mathtablegen)
        cls.inbutton.grid(row=3, columnspan=2)
        cls.tablerange.mainloop()

    @classmethod
    def mathtablegen(cls):
        #To catch a display of an error in interpreter if user presses 'OK' button without inputting anything
        try:
            cls.a = cls.intenter.get()
            cls.b = cls.startrangein.get()
            cls.c = cls.endrangein.get()

            cls.mathtablewin = Tk()
            cls.mathtablewin.wm_title('Math Tables')
            cls.n1 = int(cls.a)
            cls.n2 = int(cls.b)
            cls.n3 = int(cls.c)
            cls.output = ''
            for x in range(cls.n2, (cls.n3 + 1), 1):
                cls.ha = cls.n1 * x
                cls.output = cls.output + "{0} * {1} = {2}\n".format(cls.n1, x, cls.ha)
            mathtab = Label(cls.mathtablewin, text=cls.output)
            mathtab.pack()
            cls.mathtablewin.mainloop()
        except ValueError:
            cls.mathtablewin.destroy()
            pass

    @classmethod
    def webevent(cls, event):
        webbrowser.open_new(r"https://docs.python.org/2/library/math.html")

    @classmethod
    def displayAboutMenu(cls):
        cls.about_window = Tk()
        cls.about_window.wm_title('About')
        # cls.about_window.geometry('150x100')
        cls.about_label1 = Label(cls.about_window, text='''
This calculator comes packed with the
built-in python math module, giving it more
accessibilty to mathematical functions.
The proper syntax should merely be entered in
the input box for your expressions to be evaluated.
Documentation for the module can be found at:''', justify='left')
        cls.about_label1.grid(row=0, column=0)
        cls.weblink = Label(
            cls.about_window, text='https://docs.python.org/2/library/math.html', fg='blue', cursor='hand2', justify=LEFT)
        cls.weblink.bind('<Button-1>', cls.webevent)
        cls.weblink.grid(row=1, column=0)
        cls.about_label2 = Label(cls.about_window, text='''
-------------WARNING-------------
This calculator uses python's built-in eval()
function. Do not input any rogue code in the entry
box for the sake of your machine. Use at your
own risk.
-------------------------------------
Made by Babur Ahmed.
16th July, 2017
        ''', justify=LEFT)
        cls.about_label2.grid(row=2, column=0)
        cls.about_window.mainloop()


root = Tk()

root.resizable(False, False)
calcstart = Calculator(root)

root.mainloop()

