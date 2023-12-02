import math
import csv
import os
"""
    This is a script that calculates the effective thermal resistance between two objects given the heat paths between them
    2023/10/15: finished implementing heat transfer equations for common shapes and functionality to calculate heat paths based on given parameters. Still need to check with Orrin on which conductance values we are using for high/mid/low cases and which materials. 
    2023/10/21: Added comments and filled in the dictionary storing conductance values
    2023/11/4: get the heat path datas from csv file
    2023/11/23: read the conductance values from heat path
    2023/12/1: 
"""

class sub_path:
  area = 0
  length = 1
  material1 = ""
  material2 = ""
  pressure = ""
  def __init__(self, area, length, material1, material2, pressure):
    self.area = area
    self.length = length
    self.material1 = material1
    self.material2 = material2
    self.pressure = pressure
    
#unit: W/m K
material_conductance_values = {
  "aluminum": 174,
  "steel": 54,
  "copper": 381,
  "brass": 170,
}

#low&high contact conductance values for high pressure. unit: W/m K
high_contact_conductance_values = {
  "steel": {"steel" : [3240., 7770.], "aluminum": [7930., 7930.]},
  "aluminum": {"aluminum" : [12840., 25170.], "steel": [7930., 7930.], "copper": [30880., 30880.]},
  "copper": {"aluminum" : [30880., 30880.]},
}
#low&high contact conductance values for medium pressure. unit: W/m K
mid_contact_conductance_values = {
  "steel": {"steel" : [2860., 6530.], "aluminum": [6110., 6110.]},
  "aluminum": {"aluminum" : [9370., 18950.], "steel": [6110., 6110.], "copper": [22660., 22660.]},
  "copper": {"aluminum" : [22660., 22660.]},
}

#low&high contact conductance values for low pressure. unit: W/m K
low_contact_conductance_values = {
  "steel": {"steel" : [2080., 3210.], "aluminum": [3140., 3140.]},
  "aluminum": {"aluminum" : [3820., 11050.], "steel": [3140., 3140.], "copper": [10300., 10300.]},
  "copper": {"aluminum" : [10300., 10300.]},
}

def read_material_conductance_values(filepath = ""):
  if(not os.path.exists(filepath)): return
  with open(filepath, newline='') as f:
    r = csv.reader(f)
    for row in r:
      if (row[0] == "steel"): material_conductance_values["steel"]=int(row[1])
      elif (row[0] == "aluminum"): material_conductance_values["aluminum"]=int(row[1])
      elif (row[0] == "copper"): material_conductance_values["copper"]=int(row[1])
      elif (row[0] == "brass"): material_conductance_values["brass"]=int(row[1])
        
def read_contact_conductance_values(filepath = ""):
  if(not os.path.exists(filepath)): return
  with open(filepath, newline='') as f:
    r = csv.reader(f)
    for row in r:
      if (row[0] == "Steel to Steel"): 
        low_contact_conductance_values["steel"]["steel"]=[float(row[2]), float(row[4])]
        row = next(r)
        mid_contact_conductance_values["steel"]["steel"]=[float(row[2]), float(row[4])]
        row = next(r)
        high_contact_conductance_values["steel"]["steel"]=[float(row[2]), float(row[4])]
      elif (row[0] == "Aluminum to Aluminum"): 
        low_contact_conductance_values["aluminum"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        mid_contact_conductance_values["aluminum"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        high_contact_conductance_values["aluminum"]["aluminum"]=[float(row[2]), float(row[4])]
        
      elif (row[0] == "Aluminum to Steel"): 
        low_contact_conductance_values["aluminum"]["steel"]=[float(row[2]), float(row[4])]
        low_contact_conductance_values["steel"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        mid_contact_conductance_values["aluminum"]["steel"]=[float(row[2]), float(row[4])]
        mid_contact_conductance_values["steel"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        high_contact_conductance_values["aluminum"]["steel"]=[float(row[2]), float(row[4])]
        high_contact_conductance_values["steel"]["aluminum"]=[float(row[2]), float(row[4])]
      elif (row[0] == "Copper to Aluminum"): 
        low_contact_conductance_values["aluminum"]["copper"]=[float(row[2]), float(row[4])]
        low_contact_conductance_values["copper"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        mid_contact_conductance_values["aluminum"]["copper"]=[float(row[2]), float(row[4])]
        mid_contact_conductance_values["copper"]["aluminum"]=[float(row[2]), float(row[4])]
        row = next(r)
        high_contact_conductance_values["aluminum"]["copper"]=[float(row[2]), float(row[4])]
        high_contact_conductance_values["copper"]["aluminum"]=[float(row[2]), float(row[4])]
"""
    This function deals with the contact resistance case. It asks for the second matrial with which the first is in contact, the pressure over the contact surface, and the contact surface area. 
    
    Parameters:
    material: the first material 
    high_low: whether the calculation is for the high conductance case or the low conductance case

    Returns the resistance
"""
def contact_resis(subpath, high_low):
  contact_conductance = 0
  if(subpath.pressure == "HIGH"): contact_conductance = high_contact_conductance_values[subpath.material1][subpath.material2][high_low]
  elif(subpath.pressure == "MID"): contact_conductance = mid_contact_conductance_values[subpath.material1][subpath.material2][high_low]
  elif(subpath.pressure == "LOW"): contact_conductance = low_contact_conductance_values[subpath.material1][subpath.material2][high_low]
  contact_resistance = subpath.length/(subpath.area*contact_conductance)
  return contact_resistance

"""
    This function deals with the heat path across a material. It asks for the geometry of the material and the relevant lengths for each shape.
    Returns the resistance
"""
def material_resis(subpath):
  material_conductance = material_conductance_values[subpath.material1]
  return subpath.length/(material_conductance*subpath.area)

"""
    This function calculates the total resistance across one heat path. 
"""
def get_path_resis(high_low, subpaths):
  path_resis = 0
  for subpath in subpaths:
    material1 = subpath.material1
    #if the pressure column is blank, treat it as material conductance
    if(subpath.pressure=="" or subpath.material2==""):
      path_resis+=material_resis(subpath)
    else:
      path_resis+=contact_resis(subpath, high_low)
  return path_resis

def csvrow_to_subpaths(row):
  subpaths = []
  #each subpath is consisted of 5 elements in the row
  for i in range(0, (len(row)-1)//5):
    subpaths.append(sub_path(float(row[5*i]), float(row[5*i+1]), row[5*i+2], row[5*i+3], row[5*i+4]))
  return subpaths
  
"""
reads csv file where each row is a complete heatpath(could be composed of multiple sections in series) and each row is in parralle to each other. 
also calls get_path_resis to calculate the resistance of each path and keep track of the sum of their recipracals
"""
def read_csv(filepath = 'C:/Users/harry/Downloads/Heat-path-calculation-tool/battery top bracket to EPS.csv'):
  eff_resistance = 0.0
  high_low = 0
  with open(filepath, newline='') as f:
    r = csv.reader(f)
    for row in r:
      #first row as one column to indicate whether we're calculating for the high k-value case or the low k-value case
      if(row[0] == "HIGH"): high_low = 1
      elif(row[0] == "LOW"): high_low = 0
      else: eff_resistance+=1.0/get_path_resis(high_low, csvrow_to_subpaths(row))
  return eff_resistance

read_material_conductance_values()
read_contact_conductance_values()
print("The effective resistance between the two objects is: ", 1.0/read_csv())
