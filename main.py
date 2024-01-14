import argparse, os, sys
sys.path.append(os.path.abspath(str(os.getcwd())+"/src"))
import fileio, calculation

#command line parsing
Parser=argparse.ArgumentParser(description="Calculates the total resistance for given heat paths")
Parser.add_argument("--input","-i",
                    metavar="FILE",
                    required=True,
                    nargs=1,
                    dest="ifile",
                    help="a csv file that contains information about the heat paths")
Parser.add_argument("--output", "-o",
                    metavar="FILE",
                    required=False,
                    nargs=1,
                    dest="ofile",
                    help="writes thermal resistance to the given file instead of printing to console")
Parser.add_argument("--append",'-a',
                    required=False,
                    action='store_true',
                    dest="append",
                    help="append to the given output file instead of overwriting")
args=Parser.parse_args()

#getting info from files and calculate thermal resistance
thermal_paths = fileio.get_paths(args.ifile[0])
cond_val = fileio.get_condval(os.path.abspath(str(os.getcwd())+"/data/conductance_values.json"))
result = str(calculation.therm_res(thermal_paths, cond_val))

#output
if (args.ofile is not None):
    if(args.append):
        fileio.file_output(args.ofile[0], ','+result, "a")
    else:
        fileio.file_output(args.ofile[0], result, "w")

else:
    print(result)