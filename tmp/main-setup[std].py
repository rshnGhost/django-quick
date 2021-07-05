import sys, getopt

inputfile = []
outputfile = []

def main(argv):
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=","ofile="])
    except getopt.GetoptError:
        print(str(sys.argv[0])+' -i <inputfile> -o <outputfile>')
        print(str(sys.argv[0])+' --ifile <inputfile> --ofile <outputfile>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(str(sys.argv[0])+' -i <inputfile> -o <outputfile>')
            print(str(sys.argv[0])+' --ifile <inputfile> --ofile <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile.append(arg)
        elif opt in ("-o", "--ofile"):
            outputfile.append(arg)
    print('Input file is', inputfile)
    print('Output file is', outputfile)

if __name__ == "__main__":
main(sys.argv[1:])
