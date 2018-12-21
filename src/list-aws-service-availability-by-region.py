#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------------- #
# Description                                                                      #
# -------------------------------------------------------------------------------- #
#                                                                                  #
# -------------------------------------------------------------------------------- #
# Example Usage:                                                                   #
#                                                                                  #
#    ./list-aws-service-availability-by-region.py                                  #
# -------------------------------------------------------------------------------- #

from __future__ import print_function

import argparse
import requests
import sys
import unidecode

import os.path

from bs4 import BeautifulSoup
from prettytable import PrettyTable

# -------------------------------------------------------------------------------- #
# Default Values                                                                   #
# -------------------------------------------------------------------------------- #
# A set of default values to be used but allow them to be overridden.              #
# -------------------------------------------------------------------------------- #

region_table_url = 'https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/'

aws_region_list = [
                    {'region': 'ap-northeast-1', 'fullname': 'Asia Pacific (Tokyo)'},
                    {'region': 'ap-northeast-2', 'fullname': 'Asia Pacific (Seoul)'},
                    {'region': 'ap-northeast-3', 'fullname': 'Asia Pacific (Osaka-Local)'},
                    {'region': 'ap-south-1',     'fullname': 'Asia Pacific (Mumbai)'},
                    {'region': 'ap-southeast-1', 'fullname': 'Asia Pacific (Singapore)'},
                    {'region': 'ap-southeast-2', 'fullname': 'Asia Pacific (Sydney)'},
                    {'region': 'ca-central-1',   'fullname': 'Canada (Central)'},
                    {'region': 'cn-north-1',     'fullname': 'China (Beijing)'},
                    {'region': 'cn-northwest-1', 'fullname': 'China (Ningxia)'},
                    {'region': 'eu-central-1',   'fullname': 'EU (Frankfurt)'},
                    {'region': 'eu-north-1',     'fullname': 'EU (Stockholm)'},
                    {'region': 'eu-west-1',      'fullname': 'EU (Ireland)'},
                    {'region': 'eu-west-2',      'fullname': 'EU (London)'},
                    {'region': 'eu-west-3',      'fullname': 'EU (Paris)'},
                    {'region': 'sa-east-1',      'fullname': 'South America (Sao Paulo)'},
                    {'region': 'us-east-2',      'fullname': 'US East (Ohio)'},
                    {'region': 'us-east-1',      'fullname': 'US East (N. Virginia)'},
                    {'region': 'us-gov-east-1',  'fullname': 'AWS GovCloud (US-East)'},
                    {'region': 'us-gov-west-1',  'fullname': 'AWS GovCloud (US)'},
                    {'region': 'us-west-1',      'fullname': 'US West (N. California)'},
                    {'region': 'us-west-2',      'fullname': 'US West (Oregon)'},
                  ]


# -------------------------------------------------------------------------------- #
# Main()                                                                           #
# -------------------------------------------------------------------------------- #
# This is the actual 'script' and the functions/sub routines are called in order.  #
# -------------------------------------------------------------------------------- #

def main(cmdline=None):
    parser = make_parser()

    args = parser.parse_args(cmdline)

    if args.search_region is not None and not valid_aws_region(args.search_region):
        print("Invalid search option: %s" % args.search_region)
        print("Valid regions:- \n%s" % get_valid_regions())
        return 1

    if args.exclude_region is not None and not valid_aws_region(args.exclude_region):
        print("Invalid exclude option: %s" % args.exclude_region)
        print("Valid regions:- \n%s" % get_valid_regions())
        return 1

    contents = get_page_contents(region_table_url)
    regions, services, results = process_page_contents(contents)

    display_results(regions, services, results, args.search_region, args.exclude_region)


# -------------------------------------------------------------------------------- #
# Make Parser                                                                      #
# -------------------------------------------------------------------------------- #
# Setup the command line parser.                                                   #
# -------------------------------------------------------------------------------- #

def make_parser():
    parser = argparse.ArgumentParser(description='List AWS Service Availability by Region')

    parser.add_argument('-e', '--exclude-region', type=str, help='The region to exclude from the results', default=None)
    parser.add_argument('-n', '--no-results', help='Do not show the final table of results', action='store_true')
    parser.add_argument('-s', '--search-region', type=str, help='The region to search the results for', default=None)
    return parser


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def get_page_contents(url):
    r = requests.get("https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/")
    return r.content


def process_page_contents(contents):
    soup = BeautifulSoup(contents, 'lxml')

    tables = soup.find('div', {'class': 'aws-comp'}).find_all('table')

    regions = ['']
    services = []
    t = []
    for table in tables:
        rows = table.find_all('tr')
        r = []
        first_row = True
        for row in rows:
            columns = row.find_all('td')
            c = []
            first_column = True
            for column in columns:
                cell = column.get_text().strip()
                cell = cell.replace(unichr(160), "N")               # Convert &nbsp; to N
                cell = cell.replace(unichr(10003), "Y")             # Convert a 'check mark' to Y
                cell = 'N' if not cell else cell

                if first_row and not first_column:
                    regions.append(cell)
                elif first_column and not first_row:
                    if cell not in services:
                        services.append(cell)
                    c.append(cell)
                elif cell != 'Services Offered:':
                    c.append(cell)
                first_column = False
            if len(c) > 0:
                r.append(c)
            first_row = False
        t.append(r)

    return regions, services, t


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #


def get_region_from_name(search_name):
    for r in aws_region_list:
        if (r['fullname'] == search_name):
            return r['region']
    print('%s is NOT found in the list' % search_name)
    return None


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def valid_aws_region(region):
    for r in aws_region_list:
        if (r['region'] == region):
            return True
    return False


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def get_valid_regions():
    region_list = []

    for r in aws_region_list:
        region_list.append(r['region'])

    region_chunks = list(chunks(region_list, 12))
    region_string = '\n'.join(', '.join(sub) for sub in region_chunks)

    return region_string


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def in_region(locations, search_region):
    regions = []

    for loc in locations:
        region = get_region_from_name(loc)
        if region == search_region:
            return True

    return False


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def pad_or_truncate(list, target_len, str='N'):
    return list[:target_len] + [str]*(target_len - len(list))


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def get_row_by_service(service, table, min_number):
    rows = []

    for row in table:
        if row[0] == service:
            rows = row[1:]
            break

    padded_rows = pad_or_truncate(rows, min_number)
    return padded_rows


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def get_rows_by_service_wrapper(service, tables):
    rows = []

    rows.append(service)
    rows += get_row_by_service(service, tables[0], 8)
    rows += get_row_by_service(service, tables[1], 5)
    rows += get_row_by_service(service, tables[2], 8)

    return rows


# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------- #

def display_results(regions, services, results, search=None, exclude=None):
    table = PrettyTable()

    table.field_names = regions

    for service in services:
        row = get_rows_by_service_wrapper(service, results)
        table.add_row(row)

    table.hrules = True
    print(table)


# -------------------------------------------------------------------------------- #
# Main() really this time                                                          #
# -------------------------------------------------------------------------------- #
# This runs when the application is run from the command it grabs sys.argv[1:]     #
# which is everything after the program name and passes it to main the return      #
# value from main is then used as the argument to sys.exit, which you can test for #
# in the shell. program exit codes are usually 0 for ok, and non-zero for          #
# something going wrong.                                                           #
# -------------------------------------------------------------------------------- #

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# -------------------------------------------------------------------------------- #
# End of Script                                                                    #
# -------------------------------------------------------------------------------- #
# This is the end - nothing more to see here.                                      #
# -------------------------------------------------------------------------------- #
