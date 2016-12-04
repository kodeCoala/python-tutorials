#! /usr/bin/env python

# Read argparse  python docs for mare details
# This also has a logging example
import argparse
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s')
log = logging.getLogger()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This a basic argument parsing example",
                                     epilog="./pass_args.py -")

    parser.add_argument('-c', '--country', help="add country", required=True)
    parser.add_argument('-i', '--inbound', help="add date", required=True)
    parser.add_argument('-o', '--outbound', help="add date", required=True)

    args = parser.parse_args()
    log.info("country={}".format(args.country))
    log.info("inbound={}".format(args.inbound))
    log.info("outbound={}".format(args.outbound))


