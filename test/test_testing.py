import sys
sys.path.append("../src")
import calculation, fileio, formula, structure

def test_rec_cs_regular():
    assert formula.rec_cs(3, 5, 0.5) == 1/30

def test_rec_cs_nothird():
    assert formula.rec_cs(3, 5) == 1/15

def test_rec_cs_zero():
    assert formula.rec_cs(3, 5, 0) == 1/15

def test_rec_cs_negative():
    assert formula.rec_cs(3, -5, 0.5) == 1/30