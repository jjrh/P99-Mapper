import sys
import argparse
import logging, logging.handlers, logging.config
import version_info
import MapEngine
logging.config.fileConfig('logging.conf')
logger = logging.getLogger()


def main():
    """ run the prog bro """
    

if __name__ == "__main__":

    ### parseargs stuff ###
    program_version = str(version_info.__VERSION)

    parser = argparse.ArgumentParser(
        prog='P99 Mapper',
        description=''' Displays Everquest maps ''',
        epilog='''------------------------ JJRH 2017                     -----------------------'''
    )

    # program information and logging stuff.
    parser.add_argument("--version", action='version', version='%(prog)s '+program_version)
    parser.add_argument("--quiet", help="(optional) suppresses output to stdio", action="store_true")
    parser.add_argument("--level", "-l",  help="(optional) valid arguments: DEBUG,1,10 or INFO,2,20 or ERROR,3,30, or CRITICAL,4,40")
    parser.add_argument("--testing", help="(optional) turn on to only run the main part, not the entire program", action="store_true")

    # file io
    parser.add_argument("-i","--input", help="MAP FILE", metavar='file')

    args = parser.parse_args()

    ### setup values ###
    input_file = None # map file

    ### QUIET ARGS ###
    if args.quiet:     #supress messages
        logger.disabled = True

    ### INPUT ARGS ###
    if args.input:
        input_file = args.input
    else:
        logger.error("No input file defined, program not running")
        parser.print_help()
        sys.exit()

    # checking the debug level
    if args.level:
        if args.level == "DEBUG" or args.level == "1" or args.level == "10":
            logger.setLevel(10)
        elif args.level == "INFO" or args.level == "2" or args.level == "200":
            logger.setLevel(20)
        elif args.level == "WARNING" or args.level == "3" or args.level == "30":
            logger.setLevel(30)
        elif args.level == "ERROR" or args.level == "4" or args.level == "40":
            logger.setLevel(40)
        elif args.level == "CRITICAL" or args.level == "5" or args.level == "50":
            logger.setLevel(50)
        elif args.level == "0":
            logger.setLevel(0)
        else:
            parser.print_help()
            sys.exit()

    # GO GO GO
    MapEngine.INIT_PYGAME()
        

