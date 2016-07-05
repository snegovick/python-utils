NO_ARG = 1
OPT_ARG = 2
MANDATORY_ARG = 3

def parse_options(argv, expected_options):
    opt = None
    for o in argv:
        if o[0] == "-":
            if o in expected_options:
                opt = o
                expected_options[opt]['value'] = True
        elif opt:
            expected_options[opt]['value'] = o
            opt = None

def print_options(expected_options):
    for k, v in expected_options.iteritems():
        arg = ''
        if v['arg'] == OPT_ARG:
            arg = ' [arg]'
        elif v['arg'] == MANDATORY_ARG:
            arg = ' <arg>'
        print '\033[1m\t'+k+arg+'\033[0m'
        print '\t\t'+v['description']
        print

if __name__=="__main__":
    import sys
    usage = "usage"
    options = {"--help": None, "-wh": None, "-d": None, "-h": None, "-s": None, "-dvr": None, "-host": None, "-port": None}
    parse_options(sys.argv[1:], options)
    sys.argv = sys.argv[:1]
    from camera_source import camerasrc

    if options["--help"] == True:
        print usage
        exit()

    device = "/dev/video0"
    if options["-d"] == None:
        print "device name is not set, suggesting /dev/video0"
    else:
        device = options["-d"]
