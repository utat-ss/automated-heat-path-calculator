import math

pi = math.pi
log = math.log

"""
Compute material resistance for rectangular cross section
May also be used to calculate contact resistance
"""
def rec_cs(k, A, L = 1):
  if (L == 0):
    return math.abs(1/(k*A))
  return math.abs(L/(k*A))

"""
Compute material resistance for cylindrical cross section
"""
def cyl_cs(k, r1, r2, L):
  return math.abs((log(r1/r2))/(2*pi*L*k))

"""
Compute material resistance for sphereical object
"""
def sph(k, r1, r2):
  return math.abs((r2-r1)/(4*pi*r2*r1*k))
