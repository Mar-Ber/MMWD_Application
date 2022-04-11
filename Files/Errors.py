import tkinter as tk

class MapError_0():#more locals than map nodes
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Number of locals can not exceed number of points in a map. \nPlease adjust either number of points or number of locals.').grid(row=0, column=0)
             
class MapError_1():#not complete map
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Map is not complete. \nPlease fill empty places in matrix.').grid(row=0, column=0)
        
class MapError_2():#dead end point
    def __init__(self, root, row_idx):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.row_idx = row_idx
        self.root.title("Error")
        tk.Label(self.root, text='Map has dead ends in rows with indices: {0}. \nPlease add at least one neighbor.'.format(row_idx)).grid(row=0, column=0)
        
class MapError_3():#negative local number
    def __init__(self, root, row_idx):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.row_idx = row_idx
        self.root.title("Error")
        tk.Label(self.root, text='Negative entries for local placement in spaces with indices: {0}.'.format(row_idx)).grid(row=0, column=0)
        
class MapError_4():#empty local entry
    def __init__(self, root, row_idx):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.row_idx = row_idx
        self.root.title("Error")
        tk.Label(self.root, text='Empty entries for local placement in spaces with indices: {0}.'.format(row_idx)).grid(row=0, column=0)
        
class MapError_5():#exceeding local number
    def __init__(self, root, row_idx):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.row_idx = row_idx
        self.root.title("Error")
        tk.Label(self.root, text='Entries for local placement in spaces with indices: {0} exceed map size.'.format(row_idx)).grid(row=0, column=0)
   
class MapError_6():#exceeding local number
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Repeated locals indices.').grid(row=0, column=0)

class MapError_7():#nonpositive locals/points number
    def __init__(self, root, case):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.case = case
        self.root.title("Error")
        if(case==0):
            tk.Label(self.root, text='Nonpositive number of locals.').grid(row=0, column=0)
        if(case==1):
            tk.Label(self.root, text='Number of map points lesser than 5.').grid(row=0, column=0)
            
class DriverError_0():#bike parameters error
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Incorrect BIKE parameters.\nPlease verify the requirements of drivers\' parameters in the Instruction Menu.').grid(row=0, column=0)
        
class DriverError_1():#motorbike parameters error
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Incorrect MOTORBIKE parameters.\nPlease verify the requirements of drivers\' parameters in the Instruction Menu.').grid(row=0, column=0)
        
class DriverError_2():#scooter parameters error
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Incorrect SCOOTER parameters.\nPlease verify the requirements of drivers\' parameters in the Instruction Menu.').grid(row=0, column=0)
        
class DriverError_3():#other parameters error
    def __init__(self, root):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.root.title("Error")
        tk.Label(self.root, text='Incorrect OTHER parameters.\nPlease verify the requirements of drivers\' parameters in the Instruction Menu.').grid(row=0, column=0)
        
class OrdersError_0():#wrong orders parameters
    def __init__(self, root, idx_mistake):
        self.root = root
        self.frame = tk.Frame(self.root)
        self.idx_mistake = idx_mistake
        self.root.title("Error")
        tk.Label(self.root, text='Incorrect order parameters for orders with numbers: {0}.'.format(idx_mistake)).grid(row=0, column=0)
 