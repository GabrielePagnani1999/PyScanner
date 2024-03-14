import argparse

program_description = ('TARGET SPECIFICATION:\n'
                       'Use hostnames, IP addresses, networks, etc in the following format:\n'
                       ' website.com, 192.168.0.1; 10.0.0-255.1-254\n'
                       '-iL <inputfilename>: Input from list of hosts/networks\n'
                       '-iR <num hosts>: Choose random targets\n'
                       'HOST DISCOVERY:\n'
                       # '-sL: List Scan - simply list targets to scan\n'
                       '-sn: Ping Scan - disable port scan\n'
                       # '-Pn: Treat all hosts as online -- skip host discovery\n'
                       'SCAN TECHNIQUES:\n'
                       '-sS/sT/sA: Stealth/Connect/ACK scans\n'
                       '-sU: UDP Scan\n'
                       '-sN/sF/sX: TCP Null, FIN, and Xmas scans\n'
                       )


def parse_arguments():
    parser = argparse.ArgumentParser(
        usage='PyScanner [Scan Type(s)] [Options] {target specification}',
        description=program_description,
        formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    parser.add_argument('--ping-scan', '-sn', action='store_true', help='Perform ping scan')
    parser.add_argument('--tcp-scan', '-sT', action='store_true', help='Perform TCP Connect scan')
    parser.add_argument('--stealth-scan', '-sS', action='store_true', help='Perform Stealth scan')
    parser.add_argument('--xmas-scan', '-sX', action='store_true', help='Perform Xmas scan')
    parser.add_argument('--fin-scan', '-sF', action='store_true', help='Perform FIN scan')
    parser.add_argument('--ack-scan', '-sA', action='store_true', help='Perform ACK scan')
    parser.add_argument('--udp-scan', '-sU', action='store_true', help='Perform UDP scan')
    parser.add_argument('targets', nargs='+', help='Target specification')

    return parser.parse_args()
