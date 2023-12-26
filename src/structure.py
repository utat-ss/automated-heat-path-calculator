class subpath:
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

"""
    Returns a list containing subpath objects
"""
def row_to_subpaths(row):
  subpaths = []
  #each subpath is consisted of 5 elements in the row
  for i in range(0, (len(row)-1)//5):
    area=float(row[5*i])
    length=float(row[5*i+1])
    
    material1=row[5*i+2].lower()
    material2=row[5*i+3].lower()

    pressure=row[5*i+4].lower()
    subpaths.append(subpath(area, length, material1, material2, pressure))

  return subpaths