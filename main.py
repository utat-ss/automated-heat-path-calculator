import argparse, os, sys
sys.path.append(os.path.abspath(str(os.getcwd())+"/src"))
import fileio, calculation

#command line parsing
Parser=argparse.ArgumentParser(description="Calculates the total resistance for a given heat path")
Parser.add_argument("--input","-i",
                    metavar="FILE",
                    required=True,
                    nargs=1,
                    dest="ifile",
                    help="a csv file that contains information about the heat path")
Parser.add_argument("--output", "-o",
                    metavar="FILE",
                    required=False,
                    nargs=1,
                    dest="ofile",
                    help="a file containing the total thermal resistance")
args=Parser.parse_args()

#getting info from files and calculate thermal resistance
thermal_paths = fileio.get_paths(args.ifile[0])
cond_val = fileio.get_condval(os.path.abspath(str(os.getcwd())+"/data/conductance_values.json"))
result = calculation.therm_res(thermal_paths, cond_val)