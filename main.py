from argument_parser import parse_arguments


HOST_DISCOVERY = []
SCAN = []
PORT_SPEC = []
OUTPUT = []
TARGETS = []


def main():
    args = parse_arguments()
    print(args)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
