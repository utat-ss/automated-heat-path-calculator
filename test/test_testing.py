import os, sys
sys.path.append(os.path.abspath(str(os.getcwd())+"/src"))
import src

formula = src.formula

def test_rec_cs_regular():
    assert formula.rec_cs(3, 5, 0.5) == 30

def test_rec_cs_nothird():
    assert formula.rec_cs(3, 5) == 15

def test_rec_cs_zero():
    assert formula.rec_cs(3, 5, 0) == 15

def test_rec_cs_negative():
    assert formula.rec_cs(3, -5, 0.5) == 30