import tkinter as tk
import Classes as Cls
import Functions as Fun
import Errors as Err
import copy
import time as tm
import functools
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class Main_menu:
    def __init__(self):
        
        self.root = tk.Tk()
        self.root.title("Main menu")

        self.firstFrame_title = tk.Frame(self.root, width=700, height = 200)
        self.firstFrame_title.grid(row=0, column=0, padx=4, pady=4)
        
        self.secondFrame = tk.Frame(self.root, width=700, height = 400)
        self.secondFrame.grid(row=4, column=0, padx=4, pady=4)

        self.title = tk.Label(self.firstFrame_title,text="MATHEMATICAL METHODS OF DECISION SUPPORT", font='arial 14 bold').grid(row=0,column=0, pady = [50,0])
        self.subtitle = tk.Label(self.firstFrame_title,text="MMWD Delivery Company - \"Metropolical Mathematically Weighted Deliveries\"", font='12').grid(row=1,column=0, pady = [0,50],padx=30)
        
        self.instructions_menu_generate_Button = tk.Button(self.secondFrame,height=1, width=20,text="Instructions",font='arial 11',command = self.instructions_menu_generate).grid(row=0,column=0, pady=20)
        self.map_menu_generate_Button = tk.Button(self.secondFrame,height=1, width=20,text="Map",font='arial 11',command = self.map_menu_generate).grid(row=1,column=0, pady=20)
        self.drivers_menu_generate_Button = tk.Button(self.secondFrame,height=1, width=20,text="Drivers",font='arial 11',command = self.drivers_menu_generate).grid(row=2,column=0, pady=20)
        self.orders_menu_generate_Button = tk.Button(self.secondFrame,height=1, width=20,text="Orders",font='arial 11',command = self.orders_menu_generate).grid(row=3,column=0, pady=20)
        self.results_menu_generate_Button = tk.Button(self.secondFrame,height=1, width=20,text="Results",font='arial 11',command = self.results_menu_generate).grid(row=4,column=0, pady=20)
        
    def instructions_menu_generate(self):
        self.instructions_menu = tk.Toplevel(self.root)
        self.app = InstructionsMenu(self.instructions_menu)
        
    def map_menu_generate(self):
        self.map_menu = tk.Toplevel(self.root)
        self.app = MapMenu(self.map_menu)
        
    def drivers_menu_generate(self):
        self.drivers_menu = tk.Toplevel(self.root)
        self.app = DriversMenu(self.drivers_menu)
        
    def orders_menu_generate(self):
        self.orders_menu = tk.Toplevel(self.root)
        self.app = OrdersMenu(self.orders_menu)
        
    def results_menu_generate(self):
        self.results_menu = tk.Toplevel(self.root)
        self.app = ResultsMenu(self.results_menu)
      
    def start(self):
        self.root.mainloop()
          
class InstructionsMenu:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.TOP, pady=30, padx = 30)
        self.root.title("Instructions menu")
        
        self.title = tk.Label(self.frame,text="Instructions", font='arial 14 bold').pack(side=tk.TOP, pady=[0,30])
        
        self.S = tk.Scrollbar(self.frame)
        self.editarea = tk.Text(self.frame,bg='#E0E0E0',font='arial 11',wrap=tk.WORD)
        self.S.pack(side=tk.RIGHT, fill=tk.Y)
        self.editarea.pack(side=tk.LEFT, fill=tk.Y)
        self.S.config(command=self.editarea.yview)
        self.editarea.config(yscrollcommand=self.S.set)

        with open("Instructions.txt", "r") as txtr:
            data = txtr.read()
        self.editarea.insert(tk.END, data)
        
        self.editarea.tag_configure("center", justify='center')
        self.editarea.tag_add("center", 1.0, "end")
        
        tk.Button(self.root, text='Understood',height=1, width=20, command = lambda: self.root.destroy()).pack(side=tk.BOTTOM, pady=[0,30])
        
class MapMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Map menu")
        self.padding_settings = 50
        
        self.left_frame = tk.Frame(self.root, relief=tk.GROOVE, bd=2)
        self.left_frame.grid(row=1, column=0, padx=[30,4], pady=30)
        self.right_frame = tk.Frame(self.root)
        self.right_frame.grid(row=1, column=1, padx=[4,30], sticky='n')
        self.right_frame_up = tk.Frame(self.right_frame, relief=tk.GROOVE, bd=2)
        self.right_frame_up.grid(row=0, column=0, pady=30, sticky='n')
        self.right_frame_down = tk.Frame(self.right_frame)
        self.right_frame_down.grid(row=1, column=0, sticky='s')
        
        tk.Label(self.root,text="MAP SETTINGS",font='arial 14 bold').grid(row=0,column=0,padx=self.padding_settings, pady=[10,0],columnspan=2)
        tk.Label(self.left_frame,text="RANDOM MAP").grid(row=0,column=0,padx=self.padding_settings, pady=[0,10])
        tk.Label(self.right_frame_up,text="CUSTOMIZED MAP").grid(row=0,column=0,padx=self.padding_settings, pady=[0,10])

        #NUMBER OF POINTS
        self.Label1 = tk.Label(self.left_frame,text="Number of points: ").grid(row=2,column=0,padx=self.padding_settings)
        self.number_of_points_in = tk.IntVar()
        self.entry1 = tk.Entry(self.left_frame, textvariable=self.number_of_points_in).grid(row=3,column=0,padx=self.padding_settings)
        self.number_of_points_in.set(5)

        #NUMBER OF LOCALS
        self.Label2 = tk.Label(self.left_frame,text="Number of locals: ").grid(row=4,column=0,padx=self.padding_settings)
        self.number_of_locals_in = tk.IntVar()
        self.entry2 = tk.Entry(self.left_frame, textvariable=self.number_of_locals_in).grid(row=5,column=0,padx=self.padding_settings)
        self.number_of_locals_in.set(3)

        #EDGE_PROBABILITY
        self.Label3 = tk.Label(self.left_frame,text="Edge probability: ").grid(row=6,column=0,padx=self.padding_settings)
        self.edge_probability_in = tk.DoubleVar()
        self.entry3 = tk.Entry(self.left_frame, textvariable=self.edge_probability_in).grid(row=7,column=0,padx=self.padding_settings)
        self.edge_probability_in.set(0.9)

        #MIN DISTANCE
        self.Label4 = tk.Label(self.left_frame,text="Minimum distance\n between nodes: ").grid(row=8,column=0,padx=self.padding_settings)
        self.min_distance_in = tk.DoubleVar()
        self.entry4 = tk.Entry(self.left_frame, textvariable=self.min_distance_in).grid(row=9,column=0,padx=self.padding_settings)
        self.min_distance_in.set(1)

        #MAX DISTANCE
        self.Label5 = tk.Label(self.left_frame,text="Maximum distance\n between nodes: ").grid(row=10,column=0,padx=self.padding_settings)
        self.max_distance_in = tk.DoubleVar()
        self.entry5 = tk.Entry(self.left_frame, textvariable=self.max_distance_in).grid(row=11,column=0,padx=self.padding_settings)
        self.max_distance_in.set(20)

        #NUMBER OF POINTS (custom)
        self.Label1_ = tk.Label(self.right_frame_up,text="Number of points: ").grid(row=1,column=0,padx=self.padding_settings)
        self.number_of_points2_in = tk.IntVar()
        self.entry1_ = tk.Entry(self.right_frame_up, textvariable=self.number_of_points2_in).grid(row=2,column=0,padx=self.padding_settings)
        self.number_of_points2_in.set(5)
        
        #NUMBER OF LOCALS (custom)
        self.Label2_ = tk.Label(self.right_frame_up,text="Number of locals: ").grid(row=3,column=0,padx=self.padding_settings)
        self.number_of_locals2_in = tk.IntVar()
        self.entry2_ = tk.Entry(self.right_frame_up, textvariable=self.number_of_locals2_in).grid(row=4,column=0,padx=self.padding_settings)
        self.number_of_locals2_in.set(3)
        
        self.map_menu_Button = tk.Button(self.left_frame,height=1, width=20,text="Randomize Map",command = self.generate_map_random).grid(row=12,column=0,pady=30)
        self.map_menu_Button = tk.Button(self.right_frame_up,height=1, width=20,text="Custom Map",command = self.generate_map_custom).grid(row=5,column=0,pady=30)
        
        self.quitButton = tk.Button(self.right_frame_down,height=1, width=20, text = 'Back', command = lambda: self.root.destroy()).grid(row=0,column=0,padx=self.padding_settings)
        
    #update wartosci zmiennych
    def generate_map_random(self):
        if(int(self.number_of_locals_in.get()) <=0):
            self.error = tk.Toplevel(self.root)
            self.error_window = Err.MapError_7(self.error, 0)
        elif(int(self.number_of_points_in.get()) <5):
            self.error = tk.Toplevel(self.root)
            self.error_window = Err.MapError_7(self.error, 1)
        else:
            global number_of_points, number_of_locals, edge_probability, min_distance, max_distance
            number_of_points = self.number_of_points_in.get()
            number_of_locals = self.number_of_locals_in.get()
            edge_probability = self.edge_probability_in.get()
            min_distance = self.min_distance_in.get()
            max_distance = self.max_distance_in.get()
            if(number_of_locals > number_of_points):
                self.error = tk.Toplevel(self.root)
                self.error_window = Err.MapError_0(self.error)
            else:
                self.map_menu_random_generate()
        
    def generate_map_custom(self):
        if(int(self.number_of_locals2_in.get()) <=0):
            self.error = tk.Toplevel(self.root)
            self.error_window = Err.MapError_7(self.error, 0)
        elif(int(self.number_of_points2_in.get()) <5):
            self.error = tk.Toplevel(self.root)
            self.error_window = Err.MapError_7(self.error, 1)
        else:
            global number_of_points, number_of_locals
            number_of_points = self.number_of_points2_in.get()
            number_of_locals = self.number_of_locals2_in.get()
            if(number_of_locals > number_of_points):
                self.error = tk.Toplevel(self.root)
                self.error_window = Err.MapError_0(self.error)
            else:
                self.map_menu_custom_generate()
    
    def map_menu_random_generate(self):
        self.map_menu_random = tk.Toplevel(self.root)
        self.app = RandomMap(self.map_menu_random)
        
    def map_menu_custom_generate(self):
        self.map_menu_custom = tk.Toplevel(self.root)
        self.app = CustomMap(self.map_menu_custom)
        
class RandomMap():
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Generated random map")
        self.drivers_settings_padding = 10
        
        self.firstFrame = tk.Frame(self.root, width=700, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=4, pady=4, columnspan=3)
        
        self.secondFrame = tk.Frame(self.root, width=700, height = 400)
        self.secondFrame.grid(row=1, column=0, padx=4, pady=4)
        
        self.thirdFrame = tk.Frame(self.root, width=700, height = 100)
        self.thirdFrame.grid(row=2, column=0, padx=4, pady=4)
        
        self.thirdFrame_left = tk.Frame(self.thirdFrame,width=350, height = 50)
        self.thirdFrame_left.grid(row=0, column=0, padx=4, pady=4)
        
        self.thirdFrame_left_head = tk.Frame(self.thirdFrame,width=350, height = 25)
        self.thirdFrame_left_head.grid(row=0, column=0, padx=4)
        self.thirdFrame_left_body = tk.Frame(self.thirdFrame,width=350, height = 25)
        self.thirdFrame_left_body.grid(row=1, column=0, padx=4)
        
        self.thirdFrame_right = tk.Frame(self.thirdFrame,width=350, height = 50)
        self.thirdFrame_right.grid(row=0, column=1, padx=4, pady=4, rowspan=2)
        #map_canvas
        self.canvas = tk.Canvas(self.secondFrame, width=400, height=400)
        self.canvas.grid(row=0, column=0,padx=[150,0])

        scroll_x = tk.Scrollbar(self.secondFrame, orient="horizontal", command=self.canvas.xview)
        scroll_x.grid(row=1, column=0, sticky="ew",padx=[150,0])

        scroll_y = tk.Scrollbar(self.secondFrame, orient="vertical", command=self.canvas.yview)
        scroll_y.grid(row=0, column=1, sticky="ns",padx=[0,150])

        self.canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set,relief=tk.RIDGE)
        #locals_canvas
        self.canvas_locals = tk.Canvas(self.thirdFrame_left_body, width=150, height=30)
        self.canvas_locals.grid(row=0, column=0)
        
        scroll_x_locals = tk.Scrollbar(self.thirdFrame_left_body, orient="horizontal", command=self.canvas_locals.xview)
        scroll_x_locals.grid(row=1, column=0, sticky="ew", pady=[0,30])
        
        self.canvas_locals.configure(xscrollcommand=scroll_x_locals.set,relief=tk.RIDGE)
        
        tk.Label(self.firstFrame,text="RANDOM MAP",font='arial 14 bold').grid(row=1,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
                       
        self.generate()
        
        tk.Button(self.thirdFrame_right,height=1, width=20,text="New random map",command = self.generate).grid(row=0,column=0)
        tk.Button(self.thirdFrame_right,height=1, width=20,text="Back",command = lambda: self.root.destroy()).grid(row=1,column=0)
                     
    def generate(self):
        global map_, locals_
        map_= Fun.map_generator(number_of_points, min_distance, max_distance, edge_probability) 
        locals_ = Fun.define_locals(number_of_points, number_of_locals)
        
        self.canvas.delete("all")
        for i in range(0,number_of_points): 
            if(i == 0):
                for j in range(0,number_of_points):
                    self.canvas.create_text(35*i,35*(j+1),text=j,font=('14'))
                self.canvas.create_text(35*i,35*(j+1),text='\n')
            for j in range(0,number_of_points): 
                if(j == 0):
                    self.canvas.create_text(35*(i+1),35*j,text=i,font=('14'))
                self.canvas.create_text(35*(i+1),35*(j+1),text=map_[j][i])
            self.canvas.create_text(35*(i+1),35*(j+1),text='\n')
                
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        tk.Label(self.thirdFrame_left_head,text="\nPlacement of locals: ").grid(row=0,column=0)

        self.canvas_locals.delete("all")
        for i in range(0,len(locals_)): 
                self.canvas_locals.create_text(35*(i+1),15, text=locals_[i])
        self.canvas_locals.configure(scrollregion=self.canvas.bbox("all"))
        
class CustomMap():
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Custom map")
        self.drivers_settings_padding = 10
        
        self.firstFrame = tk.Frame(self.root, width=700, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=4, pady=4, columnspan=3)
        
        self.secondFrame = tk.Frame(self.root, width=700, height = 400)
        self.secondFrame.grid(row=1, column=0, padx=4, pady=4)
        
        self.thirdFrame = tk.Frame(self.root, width=700, height = 100)
        self.thirdFrame.grid(row=2, column=0, padx=4, pady=4)
        
        self.thirdFrame_left = tk.Frame(self.thirdFrame,width=350, height = 50)
        self.thirdFrame_left.grid(row=0, column=0, padx=4, pady=4)
        
        self.thirdFrame_left_head = tk.Frame(self.thirdFrame,width=350, height = 25)
        self.thirdFrame_left_head.grid(row=0, column=0, padx=4)
        self.thirdFrame_left_body = tk.Frame(self.thirdFrame,width=350, height = 25)
        self.thirdFrame_left_body.grid(row=1, column=0, padx=4)
        
        self.thirdFrame_right = tk.Frame(self.thirdFrame,width=350, height = 50)
        self.thirdFrame_right.grid(row=0, column=1, padx=4, pady=4, rowspan=2)
        #map_canvas
        self.canvas = tk.Canvas(self.secondFrame, width=400, height=400)
        self.canvas.grid(row=0, column=0,padx=[150,0])

        scroll_x = tk.Scrollbar(self.secondFrame, orient="horizontal", command=self.canvas.xview)
        scroll_x.grid(row=1, column=0, sticky="ew",padx=[150,0])

        scroll_y = tk.Scrollbar(self.secondFrame, orient="vertical", command=self.canvas.yview)
        scroll_y.grid(row=0, column=1, sticky="ns",padx=[0,150])

        self.canvas.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set,relief=tk.RIDGE)
        
        #locals_canvas
        self.canvas_locals = tk.Canvas(self.thirdFrame_left_body, width=150, height=30)
        self.canvas_locals.grid(row=0, column=0)
        
        scroll_x_locals = tk.Scrollbar(self.thirdFrame_left_body, orient="horizontal", command=self.canvas_locals.xview)
        scroll_x_locals.grid(row=1, column=0, sticky="ew", pady=[0,30])
        
        self.canvas_locals.configure(xscrollcommand=scroll_x_locals.set,relief=tk.RIDGE)
        
        tk.Label(self.firstFrame,text="CUSTOM MAP",font='arial 14 bold').grid(row=1,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
              
        self.generate()
        
        tk.Button(self.thirdFrame_right,height=1, width=20,text="Save",command = self.save).grid(row=0,column=0)
        tk.Button(self.thirdFrame_right,height=1, width=20,text="Clear",command = self.clear).grid(row=1,column=0)
        tk.Button(self.thirdFrame_right,height=1, width=20,text="Back",command = lambda: self.root.destroy()).grid(row=2,column=0)
        
    def clear(self):
        self.canvas.delete("all")
        self.canvas_locals.delete("all")
        self.generate()
    
    def generate(self):
        global inf_
        inf_ = float('inf')
        self.locals_in = [inf_]*number_of_locals
        self.map_in = [inf_]*number_of_points
        for elem in range(len(self.map_in)):
            self.map_in[elem]=[inf_]*number_of_points
        
        for i in range(0,number_of_points): 
            if(i == 0):
                for j in range(0,number_of_points):
                    self.canvas.create_text(35*i,35*(j+1),text=j,font=('14'))
                self.canvas.create_text(35*i,35*(j+1),text='\n')
            for j in range(0,number_of_points): 
                if(j == 0):
                    self.canvas.create_text(35*(i+1),35*j,text=i,font=('14'))
                if(i == j):
                    self.map_in[j][i] = inf_
                    self.canvas.create_text(35*(i+1), 35*(j+1), text=self.map_in[j][i])
                else:
                    self.map_in[j][i] = tk.Entry(self.canvas, width=5)
                    self.canvas.create_window(35*(i+1), 35*(j+1), window=self.map_in[j][i])
            self.canvas.create_text(35*(i+1),35*(j+1),text='\n')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        
        tk.Label(self.thirdFrame_left_head,text="\nPlacement of locals: ").grid(row=0,column=0)
 
        for i in range(0,number_of_locals): 
                self.locals_in[i] = tk.Entry(self.canvas_locals, width=5)
                self.canvas_locals.create_window(35*(i+1), 15, window=self.locals_in[i])
        self.canvas_locals.configure(scrollregion=self.canvas.bbox("all"))
        
    def save(self):
        check_1 = 0
        for i in range(0,number_of_points): 
            for j in range(0,number_of_points):
                if(i != j and len(self.map_in[j][i].get()) == 0):
                    check_1+=1
        if(check_1 != 0):
            self.error_1 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_1(self.error_1)
            
        check_2 = 0
        row_idx_map = []
        for i in range(0,number_of_points):  
            temp = 0               
            for j in range(0,number_of_points):
                if(i != j and len(self.map_in[i][j].get()) != 0 and int(self.map_in[i][j].get()) <= 0):
                    temp += 1
            if(temp == number_of_points-1):
                check_2 += 1
                row_idx_map.append(i)
        if(check_2 != 0):
            self.error_2 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_2(self.error_2, row_idx_map)
            
        check_3_1 = 0
        check_3_2 = 0
        check_3_3 = 0
        row_idx_locals_minus = []
        row_idx_locals_empty = []
        row_idx_locals_exceeds = []
        for i in range(0,number_of_locals):
            if(len(self.locals_in[i].get()) != 0 and int(self.locals_in[i].get()) < 0):
                check_3_1 += 1
                row_idx_locals_minus.append(i)
            if(len(self.locals_in[i].get()) == 0):
                check_3_2 += 1
                row_idx_locals_empty.append(i)
            if(len(self.locals_in[i].get()) != 0 and int(self.locals_in[i].get()) > number_of_points-1):
                check_3_3 += 1
                row_idx_locals_exceeds.append(i)
        if(check_3_1 != 0):
            self.error_3 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_3(self.error_3, row_idx_locals_minus)
        if(check_3_2 != 0):
            self.error_4 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_4(self.error_4, row_idx_locals_empty)
        if(check_3_3 != 0):
            self.error_5 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_5(self.error_5, row_idx_locals_exceeds)
            
        check_4 = 0
        for i in range(0,number_of_locals):
            if(len(self.locals_in[i].get()) != 0):
                temp = self.locals_in[i].get()
                for j in range(i+1,number_of_locals):
                    if(self.locals_in[i].get() == self.locals_in[j].get()):
                        check_4 += 1
                
        if(check_4 != 0):
            self.error_6 = tk.Toplevel(self.root)
            self.error_window = Err.MapError_6(self.error_6)
        
        if(check_1 == check_2 == check_3_1 == check_3_2 == check_3_3 == check_4 == 0):
            global map_, locals_
            locals_ = [inf_]*number_of_locals
            map_ = [inf_]*number_of_points
            for elem in range(len(self.map_in)):
                map_[elem]=[inf_]*number_of_points
                
            for i in range(0,number_of_points): 
                for j in range(0,number_of_points): 
                    if(i == j or int(self.map_in[j][i].get()) <= 0):
                        map_[j][i] = inf_
                    else:
                        map_[j][i] = int(self.map_in[j][i].get())
                
            for i in range(0,number_of_locals): 
                locals_[i] =  int(self.locals_in[i].get())

class DriversMenu():
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Drivers menu")
        self.drivers_settings_padding = 10
        
        #INTRO
        self.firstFrame = tk.Frame(self.root, width=692, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=4, pady=4)
        self.drivers_label = tk.Label(self.firstFrame,text="DRIVERS SETTINGS",font='arial 14 bold').grid(row=1,column=1,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        
        #BIKE
        self.secondFrame = tk.Frame(self.root, relief=tk.GROOVE, bd=2, width=692, height = 100)
        self.secondFrame.grid(row=1, column=0, padx=4, pady=4)
        self.frame_right_bike = tk.Frame(self.secondFrame, width=100, height = 10)
        self.frame_right_bike.grid(row=0,column=1)
        self.frame_left_bike = tk.Frame(self.secondFrame, width=592, height = 10)
        self.frame_left_bike.grid(row=0,column=0)
        self.frame_head_bike = tk.Frame(self.frame_left_bike, width=592, height = 10)
        self.frame_head_bike.grid(row=0,column=0)
        self.frame_body_bike = tk.Frame(self.frame_left_bike, width=592, height = 90)
        self.frame_body_bike.grid(row=1,column=0)

        self.drivers_label_bike = tk.Label(self.frame_head_bike,text="BIKE").grid(row=0,column=3,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)

        self.Label1_bike = tk.Label(self.frame_body_bike,text="Speed: ").grid(row=1,column=1,padx=self.drivers_settings_padding)
        self.bike_speed_in = tk.DoubleVar()
        self.entry1_bike = tk.Entry(self.frame_body_bike, textvariable=self.bike_speed_in).grid(row=2,column=1,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.bike_speed_in.set(15)
        
        self.Label2_bike = tk.Label(self.frame_body_bike,text="Capacity: ").grid(row=1,column=2,padx=self.drivers_settings_padding)
        self.bike_capacity_in = tk.DoubleVar()
        self.entry2_bike = tk.Entry(self.frame_body_bike, textvariable=self.bike_capacity_in).grid(row=2,column=2,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.bike_capacity_in.set(20)
        
        self.Label3_bike = tk.Label(self.frame_body_bike,text="Fuel cost: ").grid(row=1,column=3,padx=self.drivers_settings_padding)
        self.bike_fuel_in = tk.DoubleVar()
        self.entry3_bike = tk.Entry(self.frame_body_bike, textvariable=self.bike_fuel_in).grid(row=2,column=3,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.bike_fuel_in.set(0)
        
        self.Label4_bike = tk.Label(self.frame_body_bike,text="Quantity: ").grid(row=1,column=4,padx=self.drivers_settings_padding)
        self.number_of_bikes_in = tk.IntVar()
        self.entry4_bike = tk.Entry(self.frame_body_bike, textvariable=self.number_of_bikes_in).grid(row=2,column=4,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.number_of_bikes_in.set(1)

        self.logo_bike = tk.PhotoImage(file="bike.gif")
        self.paste_bike = tk.Label(self.frame_right_bike, image=self.logo_bike).grid(row=1,column=0)
        
        #MOTORBIKE
        self.thirdFrame = tk.Frame(self.root, relief=tk.GROOVE, bd=2, width=692, height = 100)
        self.thirdFrame.grid(row=3, column=0, padx=4, pady=4)
        self.frame_right_motorbike = tk.Frame(self.thirdFrame, width=100, height = 10)
        self.frame_right_motorbike.grid(row=0,column=1)
        self.frame_left_motorbike = tk.Frame(self.thirdFrame, width=300, height = 10)
        self.frame_left_motorbike.grid(row=0,column=0)
        self.frame_head_motorbike = tk.Frame(self.frame_left_motorbike, width=300, height = 10)
        self.frame_head_motorbike.grid(row=0,column=0)
        self.frame_body_motorbike = tk.Frame(self.frame_left_motorbike, width=300, height = 90)
        self.frame_body_motorbike.grid(row=1,column=0)

        self.drivers_label_motorbike = tk.Label(self.frame_head_motorbike,text="MOTORBIKE").grid(row=0,column=3,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)

        self.Label1_motorbike = tk.Label(self.frame_body_motorbike,text="Speed: ").grid(row=1,column=1,padx=self.drivers_settings_padding)
        self.motorbike_speed_in = tk.DoubleVar()
        self.entry1_motorbike = tk.Entry(self.frame_body_motorbike, textvariable=self.motorbike_speed_in).grid(row=2,column=1,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.motorbike_speed_in.set(30)
        
        self.Label2_motorbike = tk.Label(self.frame_body_motorbike,text="Capacity: ").grid(row=1,column=2,padx=self.drivers_settings_padding)
        self.motorbike_capacity_in = tk.DoubleVar()
        self.entry2_motorbike = tk.Entry(self.frame_body_motorbike, textvariable=self.motorbike_capacity_in).grid(row=2,column=2,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.motorbike_capacity_in.set(30)
        
        self.Label3_motorbike = tk.Label(self.frame_body_motorbike,text="Fuel cost: ").grid(row=1,column=3,padx=self.drivers_settings_padding)
        self.motorbike_fuel_in = tk.DoubleVar()
        self.entry3_motorbike = tk.Entry(self.frame_body_motorbike, textvariable=self.motorbike_fuel_in).grid(row=2,column=3,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.motorbike_fuel_in.set(0.05)
        
        self.Label4_motorbike = tk.Label(self.frame_body_motorbike,text="Quantity: ").grid(row=1,column=4,padx=self.drivers_settings_padding)
        self.number_of_motorbikes_in = tk.IntVar()
        self.entry4_motorbike = tk.Entry(self.frame_body_motorbike, textvariable=self.number_of_motorbikes_in).grid(row=2,column=4,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.number_of_motorbikes_in.set(1)
        
        self.logo_motorbike = tk.PhotoImage(file="motorbike.gif")
        self.paste = tk.Label(self.frame_right_motorbike, image=self.logo_motorbike).grid(row=1,column=0)
        
        #SCOOTER
        self.fourthFrame = tk.Frame(self.root, relief=tk.GROOVE, bd=2, width=692, height = 100)
        self.fourthFrame.grid(row=2, column=0, padx=4, pady=4)
        self.frame_right_scooter = tk.Frame(self.fourthFrame, width=100, height = 10)
        self.frame_right_scooter.grid(row=0,column=1)
        self.frame_left_scooter = tk.Frame(self.fourthFrame, width=592, height = 10)
        self.frame_left_scooter.grid(row=0,column=0)
        
        self.frame_head_scooter = tk.Frame(self.frame_left_scooter, width=592, height = 10)
        self.frame_head_scooter.grid(row=0,column=0)
        self.frame_body_scooter = tk.Frame(self.frame_left_scooter, width=592, height = 90)
        self.frame_body_scooter.grid(row=1,column=0)
        
        self.drivers_label_scooter = tk.Label(self.frame_head_scooter,text="SCOOTER").grid(row=0,column=3,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)

        self.Label1_scooter = tk.Label(self.frame_body_scooter,text="Speed: ").grid(row=1,column=1,padx=self.drivers_settings_padding)
        self.scooter_speed_in = tk.DoubleVar()
        self.entry1_scooter = tk.Entry(self.frame_body_scooter, textvariable=self.scooter_speed_in).grid(row=2,column=1,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.scooter_speed_in.set(20)
        
        self.Label2_scooter = tk.Label(self.frame_body_scooter,text="Capacity: ").grid(row=1,column=2,padx=self.drivers_settings_padding)
        self.scooter_capacity_in = tk.DoubleVar()
        self.entry2_scooter = tk.Entry(self.frame_body_scooter, textvariable=self.scooter_capacity_in).grid(row=2,column=2,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.scooter_capacity_in.set(10)
        
        self.Label3_scooter = tk.Label(self.frame_body_scooter,text="Fuel cost: ").grid(row=1,column=3,padx=self.drivers_settings_padding)
        self.scooter_fuel_in = tk.DoubleVar()
        self.entry3_scooter = tk.Entry(self.frame_body_scooter, textvariable=self.scooter_fuel_in).grid(row=2,column=3,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.scooter_fuel_in.set(0.005)
        
        self.Label4_scooter = tk.Label(self.frame_body_scooter,text="Quantity: ").grid(row=1,column=4,padx=self.drivers_settings_padding)
        self.number_of_scooters_in = tk.IntVar()
        self.entry4_scooter = tk.Entry(self.frame_body_scooter, textvariable=self.number_of_scooters_in).grid(row=2,column=4,padx=self.drivers_settings_padding,pady=[0,2*self.drivers_settings_padding])
        self.number_of_scooters_in.set(1)
        
        self.logo_scooter = tk.PhotoImage(file="scooter.gif")
        self.paste_scooter = tk.Label(self.frame_right_scooter, image=self.logo_scooter).grid(row=1,column=0)
        
        #OTHER
        self.fivethFrame = tk.Frame(self.root, width=692, height = 100)
        self.fivethFrame.grid(row=4, column=0, padx=4, pady=4)
        self.frame_right_other = tk.Frame(self.fivethFrame, width=100, height = 10)
        self.frame_right_other.grid(row=0,column=1)
        self.frame_left_other = tk.Frame(self.fivethFrame, relief=tk.GROOVE, bd=2, width=300, height = 10)
        self.frame_left_other.grid(row=0,column=0)
        
        self.frame_head_other = tk.Frame(self.frame_left_other, width=300, height = 10)
        self.frame_head_other.grid(row=0,column=0)
        self.frame_body_other = tk.Frame(self.frame_left_other, width=300, height = 90)
        self.frame_body_other.grid(row=1,column=0)
        
        self.drivers_label_other = tk.Label(self.frame_head_other,text="OTHER").grid(row=0,column=3,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)

        self.Label1_other = tk.Label(self.frame_body_other,text="Driver cost: ").grid(row=1,column=1,padx=self.drivers_settings_padding)
        self.driver_cost_in = tk.DoubleVar()
        self.entry1_other = tk.Entry(self.frame_body_other, textvariable=self.driver_cost_in).grid(row=2,column=1,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.driver_cost_in.set(0.8)
        
        self.Label2_other = tk.Label(self.frame_body_other,text="Work time: ").grid(row=1,column=2,padx=self.drivers_settings_padding)
        self.work_time_in = tk.DoubleVar()
        self.entry2_other = tk.Entry(self.frame_body_other, textvariable=self.work_time_in).grid(row=2,column=2,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.work_time_in.set(4)
        
        self.back_Button = tk.Button(self.frame_right_other,height=1, width=20,text="Back",command = lambda: self.root.destroy()).grid(row=1,column=0,padx=[100,self.drivers_settings_padding])
        self.save_Button = tk.Button(self.frame_right_other,height=1, width=20,text="Save",command = self.save).grid(row=0,column=0,padx=[100,self.drivers_settings_padding])
        
    def save(self):
        global bike_speed, bike_capacity, bike_fuel, number_of_bikes
        global motorbike_speed, motorbike_capacity, motorbike_fuel, number_of_motorbikes
        global scooter_speed, scooter_capacity, scooter_fuel, number_of_scooters
        global driver_cost, work_time
        
        check_bike = 0
        if(float(self.bike_speed_in.get()) <= 0 or float(self.bike_capacity_in.get()) < 0 or float(self.bike_fuel_in.get()) < 0 or int(self.number_of_bikes_in.get()) < 0):
            check_bike += 1
        if(check_bike != 0):
            self.error_bike = tk.Toplevel(self.root)
            self.error_window = Err.DriverError_0(self.error_bike)
        
        check_motorbike = 0
        if(float(self.motorbike_speed_in.get()) <= 0 or float(self.motorbike_capacity_in.get()) < 0 or float(self.motorbike_fuel_in.get()) <= 0 or int(self.number_of_motorbikes_in.get()) < 0):
            check_motorbike += 1
        if(check_motorbike != 0):
            self.error_motorbike = tk.Toplevel(self.root)
            self.error_window = Err.DriverError_1(self.error_motorbike)
        
        check_scooter = 0
        if(float(self.scooter_speed_in.get()) <= 0 or float(self.scooter_capacity_in.get()) < 0 or float(self.scooter_fuel_in.get()) <= 0 or int(self.number_of_scooters_in.get()) < 0):
            check_scooter += 1
        if(check_scooter != 0):
            self.error_scooter = tk.Toplevel(self.root)
            self.error_window = Err.DriverError_2(self.error_scooter)
            
        check_other = 0
        if(float(self.driver_cost_in.get()) <= 0 or float(self.work_time_in.get()) <= 0):
            check_other += 1 
        if(check_other != 0):
            self.error_other = tk.Toplevel(self.root)
            self.error_window = Err.DriverError_3(self.error_other)
        
        if(check_bike == check_motorbike == check_scooter == check_other == 0):
            bike_speed = self.bike_speed_in.get()
            bike_capacity = self.bike_capacity_in.get()
            bike_fuel = self.bike_fuel_in.get()
            number_of_bikes = self.number_of_bikes_in.get()
            
            motorbike_speed = self.motorbike_speed_in.get()
            motorbike_capacity = self.motorbike_capacity_in.get()
            motorbike_fuel = self.motorbike_fuel_in.get()
            number_of_motorbikes = self.number_of_motorbikes_in.get()
            
            scooter_speed = self.scooter_speed_in.get()
            scooter_capacity = self.scooter_capacity_in.get()
            scooter_fuel = self.scooter_fuel_in.get()
            number_of_scooters = self.number_of_scooters_in.get()
            
            driver_cost = self.driver_cost_in.get()
            work_time = self.work_time_in.get()
            
            bike = Cls.Vehicle(speed = bike_speed, capacity = bike_capacity, fuel_c = bike_fuel)
            motorbike = Cls.Vehicle(speed = motorbike_speed, capacity = motorbike_capacity, fuel_c = motorbike_fuel)
            scooter = Cls.Vehicle(speed = scooter_speed, capacity = scooter_capacity, fuel_c = scooter_fuel)
            global list_of_drivers
            list_of_drivers = []

            for num in range(0,number_of_bikes):
                list_of_drivers.append(Cls.Driver(bike, driver_cost, work_time))
            for num in range(0,number_of_scooters):
                list_of_drivers.append(Cls.Driver(scooter, driver_cost, work_time))
            for num in range(0,number_of_motorbikes):
                list_of_drivers.append(Cls.Driver(motorbike, driver_cost, work_time))
             
class OrdersMenu:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Orders menu")
        self.drivers_settings_padding = 10
        
        #INTRO
        self.firstFrame = tk.Frame(self.root, width=692, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=4, pady=4)
        self.drivers_label = tk.Label(self.firstFrame,text="ORDERS SETTINGS",font='arial 14 bold').grid(row=1,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        
        self.secondFrame = tk.Frame(self.root, width=692, height = 100)
        self.secondFrame.grid(row=1, column=0, padx=4, pady=4)
        self.frame_right = tk.Frame(self.secondFrame, width=100, height = 10)
        self.frame_right.grid(row=0,column=1,padx=[4,30])
        self.frame_left = tk.Frame(self.secondFrame, width=592, height = 10)
        self.frame_left.grid(row=0,column=0,padx=[30,4])
        self.frame_optional = tk.Frame(self.secondFrame, width=592, height = 10)
        self.frame_optional.grid(row=1,column=1,padx=[0,4])
        
        self.Label1_other = tk.Label(self.frame_left,text="Unit price: ").grid(row=0,column=0,padx=self.drivers_settings_padding)
        self.unit_price_in = tk.DoubleVar()
        self.entry1_other = tk.Entry(self.frame_left, textvariable=self.unit_price_in).grid(row=1,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.unit_price_in.set(2)
        
        self.Label2_other = tk.Label(self.frame_left,text="Number of orders: ").grid(row=2,column=0,padx=self.drivers_settings_padding)
        self.number_of_orders_in = tk.IntVar()
        self.entry2_other = tk.Entry(self.frame_left, textvariable=self.number_of_orders_in).grid(row=3,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.number_of_orders_in.set(100)
                
        self.Label4_other = tk.Label(self.frame_left,text="Minimum of delivery\ntime interval: ").grid(row=4,column=0,padx=self.drivers_settings_padding)
        self.min_delivery_time_in = tk.DoubleVar()
        self.entry4_other = tk.Entry(self.frame_left, textvariable=self.min_delivery_time_in).grid(row=5,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.min_delivery_time_in.set(1)
        
        self.Label3_other = tk.Label(self.frame_left,text="Maximum of delivery\ntime interval: ").grid(row=6,column=0,padx=self.drivers_settings_padding)
        self.max_delivery_time_in = tk.DoubleVar()
        self.entry3_other = tk.Entry(self.frame_left, textvariable=self.max_delivery_time_in).grid(row=7,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.max_delivery_time_in.set(2)
        
        self.Label6_other = tk.Label(self.frame_left,text="Minimum weight: ").grid(row=8,column=0,padx=self.drivers_settings_padding)
        self.min_weight_in = tk.DoubleVar()
        self.entry6_other = tk.Entry(self.frame_left, textvariable=self.min_weight_in).grid(row=9,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.min_weight_in.set(1)
        
        self.Label5_other = tk.Label(self.frame_left,text="Maximum weight: ").grid(row=10,column=0,padx=self.drivers_settings_padding)
        self.max_weight_in = tk.DoubleVar()
        self.entry5_other = tk.Entry(self.frame_left, textvariable=self.max_weight_in).grid(row=11,column=0,padx=self.drivers_settings_padding,pady=self.drivers_settings_padding)
        self.max_weight_in.set(5)

        self.Label5_other = tk.Label(self.frame_left,text="Placement of locals: ").grid(row=12,column=0,padx=self.drivers_settings_padding)
        
        self.localsFrame = tk.Frame(self.frame_left, width=692, height = 100)
        self.localsFrame.grid(row=13, column=0, padx=4, pady=4)
        for i in range(0,len(locals_)): 
            e = tk.Label(self.localsFrame, width=5, text=locals_[i])
            e.grid(row=0, column=i)
                 
        self.S = tk.Scrollbar(self.frame_right)
        self.T = tk.Text(self.frame_right, height=25, width=80)
        self.S.pack(side=tk.RIGHT, fill=tk.Y)
        self.T.pack(side=tk.LEFT, fill=tk.Y)
        self.S.config(command=self.T.yview)
        self.T.config(yscrollcommand=self.S.set)
        self.T.insert(tk.END,"Generated orders will appear here.\n")
        
        tk.Button(self.frame_left,height=1, width=20,text="Save/Refresh",command = self.save).grid(row=14,column=0,padx=self.drivers_settings_padding, pady=[30,0])
        tk.Button(self.frame_left,height=1, width=20,text="Back",command = lambda: self.root.destroy()).grid(row=15,column=0,padx=self.drivers_settings_padding)
        
        tk.Label(self.frame_optional, text='If you want to customize the orders list click here:',font='arial 10 bold').grid(row=0,column=0,pady=[0,30])
        tk.Button(self.frame_optional,height=1, width=20,text="Customize",command = self.orders_custom_generate).grid(row=0,column=1,padx=self.drivers_settings_padding,pady=[0,30])
        
    def save(self):
        global unit_price, number_of_orders, max_delivery_time, min_delivery_time, max_weight, min_weight
        global list_of_orders, copy_of_list_of_orders
        unit_price = self.unit_price_in.get()
        number_of_orders = self.number_of_orders_in.get()
        
        max_delivery_time = self.max_delivery_time_in.get()
        min_delivery_time = self.min_delivery_time_in.get()
        
        max_weight = self.max_weight_in.get()
        min_weight = self.min_weight_in.get()
        
        list_of_orders = Fun.orders_generator(number_of_orders, min_delivery_time, max_delivery_time, min_weight, max_weight, number_of_points, locals_)
        copy_of_list_of_orders = Fun.copy.deepcopy(list_of_orders)
        
        self.T.delete('1.0', tk.END)
        for elem in list_of_orders: 
                self.T.insert(tk.END, '({0}) Delivery time: {1}   Weight: {2}   Start point: {3}   End point: {4}\n'.format(elem.number, elem.delivery_time, elem.weight, elem.start_p, elem.end_p))
        
    def orders_custom_generate(self):
        self.orders_menu_custom = tk.Toplevel(self.root)
        self.app = CustomOrders(self.orders_menu_custom)
            
class CustomOrders:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Custom orders menu")
        self.padding_settings = 20
        
        #INTRO
        self.firstFrame = tk.Frame(self.root, width=500, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=[30,30], pady=4)
        self.drivers_label = tk.Label(self.firstFrame,text="CUSTOM ORDERS",font='arial 14 bold').grid(row=1,column=0,padx=self.padding_settings,pady=self.padding_settings)
        
        self.parametersFrame = tk.Frame(self.root, width=500, height = 100)
        self.parametersFrame.grid(row=1, column=0, padx=[30,30], pady=4)
        
        self.Label1_other = tk.Label(self.parametersFrame,text="Unit price: ").grid(row=0,column=0,padx=[self.padding_settings,0],pady=[0,self.padding_settings])
        self.unit_price_in = tk.DoubleVar()
        self.entry1_other = tk.Entry(self.parametersFrame, textvariable=self.unit_price_in).grid(row=0,column=1,padx=self.padding_settings,pady=[0,self.padding_settings])
        self.unit_price_in.set(2)
        
        self.Label2_other = tk.Label(self.parametersFrame,text="Number of orders: ").grid(row=0,column=2,padx=[self.padding_settings,0],pady=[0,self.padding_settings])
        self.number_of_orders_in = tk.IntVar()
        self.entry2_other = tk.Entry(self.parametersFrame, textvariable=self.number_of_orders_in).grid(row=0,column=3,padx=self.padding_settings,pady=[0,self.padding_settings])
        self.number_of_orders_in.set(100)
        
        tk.Button(self.parametersFrame,text="Generate blank pattern",command = self.custom_order_canvas).grid(row=0,column=4,padx=self.padding_settings,pady=[0,self.padding_settings])
        
        self.secondFrame = tk.Frame(self.root, width=500, height = 500)
        self.secondFrame.grid(row=2, column=0, padx=30, pady=4, rowspan=2)
        self.thirdFrame = tk.Frame(self.root, width=592, height = 10)
        self.thirdFrame.grid(row=4,column=0,padx=[0,4])
        
        self.Label5_other = tk.Label(self.thirdFrame,text="Placement of locals: ").grid(row=0,column=0,padx=[30,180],pady=[30,4],rowspan=2)
        
        self.localsFrame = tk.Frame(self.thirdFrame)
        self.localsFrame.grid(row=2, column=0, padx=[30,180], pady=[4,30])
        for i in range(0,len(locals_)): 
            e = tk.Label(self.localsFrame, width=5, text=locals_[i])
            e.grid(row=0, column=i)
                 
        #custom_orders_empty_canvas
        self.canvas = tk.Canvas(self.secondFrame, width=600, height=400,bg='white')
        self.canvas.grid(row=0, column=0,padx=[30,0])
        scroll_y = tk.Scrollbar(self.secondFrame, orient="vertical", command=self.canvas.yview)
        scroll_y.grid(row=0, column=1, sticky="ns",padx=[0,30])
        self.canvas.configure(yscrollcommand=scroll_y.set,relief=tk.RIDGE)
        self.canvas.create_text(100,20,text='Empty canvas will appear here.')
        
        tk.Button(self.thirdFrame,height=1, width=20,text="Save/Refresh",command = self.save).grid(row=0,column=1,padx=[180,30], pady=[30,0])
        tk.Button(self.thirdFrame,height=1, width=20,text="Clear",command = lambda: self.canvas.delete("all")).grid(row=1,column=1,padx=[180,30],pady=[0,0])
        tk.Button(self.thirdFrame,height=1, width=20,text="Back",command = lambda: self.root.destroy()).grid(row=2,column=1,padx=[180,30],pady=[0,30])
        
    def custom_order_canvas(self):
        self.canvas.delete("all")
        
        global unit_price, number_of_orders
        unit_price = self.unit_price_in.get()
        number_of_orders = self.number_of_orders_in.get()
        
        headers=['Number','Delivery Time','Weight','Start Point','End Point']
        self.delivery_time_in = [0]*number_of_orders
        self.weight_in = [0]*number_of_orders
        self.start_point_in = [0]*number_of_orders
        self.end_point_in = [0]*number_of_orders
        
        for i in range(0,number_of_orders): 
            if(i == 0):
                for j in range(0,len(headers)):
                    self.canvas.create_text(115*j+65,105*i+20,text=headers[j],font=('Arial 10'))
                self.canvas.create_text(115*j+65,105*i+20,text='\n')
            for j in range(0,2): 
                if(j == 0):
                    self.canvas.create_text(115*j+65,35*(i+1)+20,text=i)
                else:
                    self.delivery_time_in[i] = tk.Entry(self.canvas, width=10)
                    self.canvas.create_window(115*(j+0)+65, 35*(i+1)+20, window=self.delivery_time_in[i])
                    self.weight_in[i] = tk.Entry(self.canvas, width=10)
                    self.canvas.create_window(115*(j+1)+65, 35*(i+1)+20, window=self.weight_in[i])
                    self.start_point_in[i] = tk.Entry(self.canvas, width=10)
                    self.canvas.create_window(115*(j+2)+65, 35*(i+1)+20, window=self.start_point_in[i])
                    self.end_point_in[i] = tk.Entry(self.canvas, width=10)
                    self.canvas.create_window(115*(j+3)+65, 35*(i+1)+20, window=self.end_point_in[i])
        self.canvas.create_text(115*j+65,35*(number_of_orders+1)+20,text='\n')
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def save(self):
        idx_mistake = []
        check = 0
        for i in range(0, number_of_orders):
            if(len(self.delivery_time_in[i].get()) == 0 or len(self.weight_in[i].get()) == 0 or len(self.start_point_in[i].get()) == 0 or len(self.end_point_in[i].get()) == 0):
                check += 1
                idx_mistake.append(i)
            elif(float(self.delivery_time_in[i].get()) < 0 or float(self.weight_in[i].get()) < 0 or float(self.start_point_in[i].get()) < 0 or float(self.end_point_in[i].get()) < 0):
                check += 1
                idx_mistake.append(i)
            elif(int(self.start_point_in[i].get()) not in locals_):
                check += 1
                idx_mistake.append(i)
            elif(int(self.end_point_in[i].get()) > number_of_points-1):
                check += 1
                idx_mistake.append(i)
                
        if(check != 0):
            self.error_orders = tk.Toplevel(self.root)
            self.error_window = Err.OrdersError_0(self.error_orders, idx_mistake)
            
        else:
            global list_of_orders, copy_of_list_of_orders
            list_of_orders = []
            for i in range(0, number_of_orders):
                list_of_orders.append(Cls.Order(i, self.delivery_time_in[i].get(), self.weight_in[i].get(), self.start_point_in[i].get(), self.end_point_in[i].get()))
        
            copy_of_list_of_orders = Fun.copy.deepcopy(list_of_orders)
        
class ResultsMenu:
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Results menu")
        self.padding_settings = 20
        
        #INTRO
        self.firstFrame = tk.Frame(self.root, width=700, height = 100)
        self.firstFrame.grid(row=0, column=0, padx=[30,30], pady=4)
        self.drivers_label = tk.Label(self.firstFrame,text="RESULTS",font='arial 14 bold').grid(row=1,column=0,padx=self.padding_settings,pady=self.padding_settings)
        
        self.parametersFrame = tk.Frame(self.root, width=700, height = 100)
        self.parametersFrame.grid(row=1, column=0, padx=[30,30], pady=4)
        
        self.number_of_iterations_in = tk.IntVar()
        self.reset_time_in = tk.IntVar()
        self.drivers_label = tk.Label(self.parametersFrame, text="Number of iterations").grid(row=3,column=0,padx=self.padding_settings,pady=[0,self.padding_settings])
        tk.Entry(self.parametersFrame, textvariable=self.number_of_iterations_in).grid(row=3,column=1,padx=self.padding_settings,pady=[0,self.padding_settings])
        self.number_of_iterations_in.set(100)
        self.drivers_label = tk.Label(self.parametersFrame, text="Tabu list reset time").grid(row=3,column=2,padx=self.padding_settings,pady=[0,self.padding_settings])
        tk.Entry(self.parametersFrame, textvariable=self.reset_time_in).grid(row=3,column=3,padx=self.padding_settings,pady=[0,self.padding_settings])
        self.reset_time_in.set(10)
        
        self.secondFrame = tk.Frame(self.root, width=900, height = 500)
        self.secondFrame.grid(row=2, column=0, padx=30, pady=4, rowspan=2)
        
        self.thirdFrame = tk.Frame(self.root, width=900, height = 100)
        self.thirdFrame.grid(row=3, column=1, padx=30, pady=30)
        
        self.T = tk.Text(self.secondFrame, height=25, width=80)
        self.S = tk.Scrollbar(self.secondFrame, orient="vertical", command=self.T.yview)
        self.S2 = tk.Scrollbar(self.secondFrame, orient="horizontal", command=self.T.xview)
        self.S.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
        self.S2.pack(side=tk.BOTTOM, fill=tk.X, expand=True)
        self.T.pack(side=tk.LEFT, fill='both')
        self.T.config(xscrollcommand=self.S2.set, yscrollcommand=self.S.set)
        self.T.insert(tk.END,"Results will appear here.\n")
        
        self.thirdFrame_scroll = tk.Frame(self.thirdFrame)
        
        self.canvas_plots = tk.Canvas(self.thirdFrame_scroll, height=200, width=100)
        self.frame2=tk.Frame(self.thirdFrame_scroll)
        self.S_plots = tk.Scrollbar(self.thirdFrame_scroll, orient="vertical", command=self.canvas_plots.yview)
        self.canvas_plots.create_window((0,0),window=self.frame2,anchor='n')
        self.canvas_plots.configure(yscrollcommand=self.S_plots.set, scrollregion="0 0 0 %s" % self.frame2.winfo_height())
        
        self.S_plots.pack(side=tk.RIGHT, fill=tk.Y, expand=True)

        self.canvas_plots.pack(side=tk.LEFT)
        self.S_plots.pack(side=tk.RIGHT, fill = tk.Y)
        self.thirdFrame_scroll.pack()

        self.thirdFrame_buttons = tk.Frame(self.thirdFrame)
        self.thirdFrame_buttons.pack()
        self.refresh_Button = tk.Button(self.thirdFrame_buttons,height=1, width=20,text="Refresh",command = self.refresh).pack(anchor='center')
        self.back_Button = tk.Button(self.thirdFrame_buttons,height=1, width=20,text="Back",command = lambda: self.root.destroy()).pack(anchor='center')
          
        self.margin = tk.Frame(self.root)
        self.margin.grid(row=4, column=1, padx=[30,30], pady=[4,30])
        
    def refresh(self):
        self.T.delete('1.0', tk.END)
        global number_of_iterations, reset_time
        number_of_iterations = self.number_of_iterations_in.get()
        reset_time = self.reset_time_in.get()
        
        global list_of_drivers_
        list_of_orders_ = copy.deepcopy(list_of_orders)
        list_of_drivers_ = copy.deepcopy(list_of_drivers)
        global sum_of_rates, sum_of_time, sum_of_orders, tabu_time, reference_value, max_index
        sum_of_rates = 0
        sum_of_orders = 0
        tabu_time = []
        sum_of_time = 0
        for i in range(0, number_of_bikes+number_of_scooters+number_of_motorbikes):
            orders_ = []
            start_time = tm.time()
            list_of_orders_ = Fun.tabu_search(list_of_drivers_[i], map_, list_of_orders_, unit_price, number_of_iterations, reset_time)
            tabu_time.append(round(tm.time()-start_time,5))
            sum_of_time += tabu_time[-1]
            self.T.insert(tk.END, 'Driver {0}:\n\tRate: {1}\n\tTrack: {2}\n'.format(i+1, round(list_of_drivers_[i].rate,1), list_of_drivers_[i].solution))
            for elem in list_of_drivers_[i].orders:
                orders_.append(elem.number)
                sum_of_orders += 1
            max_index = list_of_drivers_[i].list_of_rate.index(list_of_drivers_[i].rate)
            self.T.insert(tk.END, '\tGreatest rate iteration number: {0}\n'.format(max_index))
            self.T.insert(tk.END, '\tRealized orders: {0}\n'.format(orders_))
            sum_of_rates += list_of_drivers_[i].rate
        self.T.insert(tk.END, '\nSum of rates: {0}'.format(round(sum_of_rates,1)))
        self.T.insert(tk.END, '\nSum of realized orders: {0}/{1}'.format(sum_of_orders, len(list_of_orders)))
        self.T.insert(tk.END, '\nAlgorithm duration time: {0} seconds'.format(round(sum_of_time,3)))
        
        sum_of_weight = 0
        sum_of_costs = 0
        for elem in list_of_orders:
            sum_of_weight += elem.weight
        gain = sum_of_weight*unit_price
        for elem in list_of_drivers:
            sum_of_costs += elem.work_time*elem.vehicle.speed*(elem.vehicle.fuel_c+driver_cost)
        reference_value = gain-sum_of_costs
        self.T.insert(tk.END, '\nReference value: {0}'.format(round(reference_value,1)))

        self.frame2.destroy()
        self.frame2=tk.Frame(self.thirdFrame_scroll)
        for i in range(0, number_of_bikes+number_of_scooters+number_of_motorbikes):
           button = tk.Button(self.frame2,text="Driver {0}".format(i+1),height=1, width=10, command=functools.partial(self.plot_results,i))
           button.pack()
           
        self.canvas_plots.create_window((0,0),window=self.frame2,anchor='nw')
        
        self.frame2.update()
        self.canvas_plots.configure(yscrollcommand=self.S_plots.set, scrollregion="0 0 0 %s" % self.frame2.winfo_height())
        self.S_plots.pack(side=tk.RIGHT, fill=tk.Y, expand=True)
        self.canvas_plots.pack(side=tk.LEFT)
        self.S_plots.pack(side=tk.RIGHT, fill = tk.Y)
        self.thirdFrame_scroll.pack()
        
    def plot_results(self, driver_idx):
        self.plot_generate = tk.Toplevel(self.root)
        self.app = Plot(self.plot_generate, driver_idx)
        
class Plot:
    def __init__(self, root, driver_idx):
        self.root = root
        self.root.title("Results plot")
        self.driver_idx = driver_idx

        list_of_rate_ = list_of_drivers_[self.driver_idx].list_of_rate
        fig=Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.plot(range(0, number_of_iterations+1),list_of_rate_, 'o')
        
        params = np.polyfit(range(0, number_of_iterations+1), list_of_rate_, 1)
        function = np.poly1d(params)
        a.plot(range(0, number_of_iterations+1), function(range(0, number_of_iterations+1)), 'r-')
        
        a.plot(list_of_rate_.index(max(list_of_rate_)),max(list_of_rate_),color='orange', marker='o')
        
        a.set_title ("Results of every iteration for Driver {0}".format(driver_idx+1), fontsize=16)
        a.set_ylabel("Rate", fontsize=14)
        a.set_xlabel("Number of iteration", fontsize=14)
        a.grid(True)
        a.set_xlim((1, number_of_iterations))
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.get_tk_widget().pack()
        canvas.draw()
        
menu = Main_menu()
menu.start()
