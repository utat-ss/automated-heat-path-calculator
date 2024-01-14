from math import pi, log

"""
Compute material resistance for rectangular cross section
May also be used to calculate contact resistance
"""
def rec_cs(k, A, L = 1):
  return L/(k*A)

"""
Compute material resistance for cylindrical cross section
"""
def cyl_cs(k, r1, r2, L):
  return (log(r1/r2))/(2*pi*L*k)

"""
Compute material resistance for sphereical object
"""
def sph(k, r1, r2):
  return (r2-r1)/(4*pi*r2*r1*k)
