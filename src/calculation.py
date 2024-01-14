import structure
from formula import rec_cs

"""
    Deals with the contact resistance case. It asks for the second matrial with which the first is in contact, the pressure over the contact surface, and the contact surface area. 
    Return the resistance
"""
def contact_res(subpath, high_low, contact_cond_val):
  contact_mats=subpath.material1+'-'+subpath.material2
  contact_cond=contact_cond_val[subpath.pressure][contact_mats][high_low]
  return rec_cs(contact_cond, subpath.area, subpath.length)

"""
    Deals with the heat path across a material. It asks for the geometry of the material and the relevant lengths for each shape.
    Return the resistance
"""
def material_res(subpath, material_cond_val):
  material_cond = material_cond_val[subpath.material1]
  return rec_cs(material_cond, subpath.area, subpath.length)

"""
    Return the total resistance across one heat path. 
"""
def get_path_resis(high_low, subpaths, cond_val):
  path_res = 0.0
  for subpath in subpaths:
    if(subpath.pressure=="" or subpath.material2==""):
      path_res+=material_res(subpath, cond_val['material'])
    else:
      path_res+=contact_res(subpath, high_low, cond_val['contact'])
  
  return path_res

"""
    Return the recipocal of the sum of recipocal heatpaths
"""
def therm_res(thermal_paths, cond_val):
    eff_res = 0.0
    high_low = 0
    if(thermal_paths[0][0] == "HIGH"): high_low = 1

    for row in thermal_paths[1:]:
      eff_res+=1/get_path_resis(high_low, structure.row_to_subpaths(row), cond_val)

    return 1/eff_res