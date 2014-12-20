# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 21:37 2014

@author: Nick
"""
from tkinter.filedialog import askopenfilename
import csv
import tkinter as tk


class Application(tk.Frame):

	def __init__(self, master=None):
		master.minsize(width=666, height=666)
		master.maxsize(width=666, height=666)
		tk.Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		csv_data=[]
		self.csv_data = csv_data

		'''Button 1-------------------------------------------------------'''
		button1 = tk.Button(self)
		button1["text"] = "Open and Select File"
		button1["command"] = lambda: self.get_file()

		'''Button 2-------------------------------------------------------'''
		button2 = tk.Button(self)
		button2["text"] = "Show Commidties"
		button2["command"] = lambda: self.show_com_list()
		#button2 = tk.Button(self, text="Analyse Data", command=lambda: self.show_com_list())
		
		'''Button 3-------------------------------------------------------'''
		button3 = tk.Button(self)
		button3["text"] = "Show More Commidties"
		button3["command"] = lambda:self.otherbuttonlabel()
		#self.button2 = tk.Button(self, text="Analyse Data", command=lambda: self.otherlabel())
		
		'''Button QUIT---------------------------------------------------'''
		self.QUIT = tk.Button(self, 
								text="QUIT", 
								fg="red",
								command=root.destroy)
		self.QUIT.grid(row=6, column=2)

		'''Geometry section, all the widget calls------------------------'''
		button1.grid(row=2, column=2, padx=5, pady=5)
		button2.grid(row=3, column=2)
		button3.grid(row=4, column=2)

	def get_file(self):
		#com_list = com_list.get()
		#ask the user what file to analyse, it needs to be a ; deliminated csv file.
		file_name =  askopenfilename()
		print('Open file :',file_name)
		#Open and read the CSV
		f = open(file_name)
		csv_f = list(csv.reader(f, delimiter=';'))
		#Create list of Comidities
		com_list = []
		for e in csv_f[2:]:
			com_list.append(e[2])
		self.csv_data = com_list

	def show_com_list(self):
		#com_list = com_list.get()
		if self.csv_data is None: 
			raise Exception("No data loaded yet")
		listbox2 = tk.Listbox(self)
		listbox2.grid(row=8, column=3)
		listbox2.insert(END, "Comidities")
		for e in self.csv_data:
			listbox2.insert(END, e)

	def otherbuttonlabel(self):    
		if self.csv_data is None: 
			raise Exception("No data loaded yet")
		return tk.Label(self, text="TOD").grid(row=8, column=2)


class Team(object):
	#Function to add somthing to a list without duplications
	def addToList(self, str_to_add):
		if str_to_add not in self:
			self.append(str_to_add)


'''-----------------------------------------------------------------------'''
#Make the GUI Swim
root = tk.Tk()
app = Application(master=root)
app.mainloop()