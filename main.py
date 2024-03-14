import argparse


HOST_DISCOVERY = []
SCAN = []
PORT_SPEC = []
OUTPUT = []
TARGETS = []

program_description = ('TARGET SPECIFICATION:\n'
                       'Use hostnames, IP addresses, networks, etc in the following format:\n'
                       ' website.com, 192.168.0.1; 10.0.0-255.1-254\n'
                       '-iL <inputfilename>: Input from list of hosts/networks\n'
                       '-iR <num hosts>: Choose random targets\n'
                       'HOST DISCOVERY:\n'
                       '-sL: List Scan - simply list targets to scan\n'
                       '-sn: Ping Scan - disable port scan\n'
                       '-Pn: Treat all hosts as online -- skip host discovery\n'
                       'SCAN TECHNIQUES:\n'
                       '-sS/sT/sA: TCP SYN/Connect()/ACK\n'
                       '-sU: UDP Scan\n'
                       '-sN/sF/sX: TCP Null, FIN, and Xmas scans\n'
                       )

def custom_parser(args):
    for arg in args:
        if arg.startswith('-'):
            # parse functions
            print('')
        else:
            # add to targets
            print('')


def main():
    parser = argparse.ArgumentParser(
        usage='PyScanner [Scan Type(s)] [Options] {target specification}',
        description=program_description,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('arguments', nargs='*', help='Arguments')

    args = parser.parse_args()

    # custom_parser(args)
    print(args)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
