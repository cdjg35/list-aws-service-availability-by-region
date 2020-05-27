#!/usr/bin/env python
# -*- encoding: utf-8 -*-

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
import six
import sys
from unidecode import unidecode

from bs4 import BeautifulSoup
from prettytable import PrettyTable

# -------------------------------------------------------------------------------- #
# Default Values                                                                   #
# -------------------------------------------------------------------------------- #
# A set of default values to be used but allow them to be overridden.              #
# -------------------------------------------------------------------------------- #

region_table_url = 'https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/'

aws_region_list = [
                    {'region': 'ap-northeast-1', 'fullname': 'Asia Pacific (Tokyo)',       'region_table_name': 'Tokyo'},
                    {'region': 'ap-northeast-2', 'fullname': 'Asia Pacific (Seoul)',       'region_table_name': 'Seoul'},
                    {'region': 'ap-northeast-3', 'fullname': 'Asia Pacific (Osaka-Local)', 'region_table_name': 'Osaka'},
                    {'region': 'ap-south-1',     'fullname': 'Asia Pacific (Mumbai)',      'region_table_name': 'Mumbai'},
                    {'region': 'ap-southeast-1', 'fullname': 'Asia Pacific (Singapore)',   'region_table_name': 'Singapore'},
                    {'region': 'ap-southeast-2', 'fullname': 'Asia Pacific (Sydney)',      'region_table_name': 'Sydney'},
                    {'region': 'ca-central-1',   'fullname': 'Canada (Central)',           'region_table_name': 'Montreal'},
                    {'region': 'cn-north-1',     'fullname': 'China (Beijing)',            'region_table_name': 'Beijing'},
                    {'region': 'cn-northwest-1', 'fullname': 'China (Ningxia)',            'region_table_name': 'Ningxia'},
                    {'region': 'eu-central-1',   'fullname': 'EU (Frankfurt)',             'region_table_name': 'Frankfurt'},
                    {'region': 'eu-north-1',     'fullname': 'EU (Stockholm)',             'region_table_name': 'Stockholm'},
                    {'region': 'eu-west-1',      'fullname': 'EU (Ireland)',               'region_table_name': 'Ireland'},
                    {'region': 'eu-west-2',      'fullname': 'EU (London)',                'region_table_name': 'London'},
                    {'region': 'eu-west-3',      'fullname': 'EU (Paris)',                 'region_table_name': 'Paris'},
                    {'region': 'sa-east-1',      'fullname': 'South America (Sao Paulo)',  'region_table_name': 'Sao Paulo'},
                    {'region': 'us-east-2',      'fullname': 'US East (Ohio)',             'region_table_name': 'Ohio'},
                    {'region': 'us-east-1',      'fullname': 'US East (N. Virginia)',      'region_table_name': 'Northern Virginia'},
                    {'region': 'us-gov-east-1',  'fullname': 'AWS GovCloud (US-East)',     'region_table_name': 'GovCloud (US-East)'},
                    {'region': 'us-gov-west-1',  'fullname': 'AWS GovCloud (US)',          'region_table_name': 'GovCloud (US-West)'},
                    {'region': 'us-west-1',      'fullname': 'US West (N. California)',    'region_table_name': 'Northern California'},
                    {'region': 'us-west-2',      'fullname': 'US West (Oregon)',           'region_table_name': 'Oregon'},
                  ]


# -------------------------------------------------------------------------------- #
# Main()                                                                           #
# -------------------------------------------------------------------------------- #
# This is the actual 'script' and the functions/sub routines are called in order.  #
# -------------------------------------------------------------------------------- #

def main(cmdline=None):
    parser = make_parser()

    args = parser.parse_args(cmdline)

    if args.search_region is not None and args.exclude_region is not None:
        print("Error: You cannot search AND exclude regions - just one or the other - Aborting")
        return 1

    if args.search_region is not None:
        args.search_region = validate_region_list(args.search_region)

    if args.exclude_region is not None:
        args.exclude_region = validate_region_list(args.exclude_region)

    if args.search_service is not None and args.exclude_service is not None:
        print("Error: You cannot search AND exclude services - just one or the other - Aborting")
        return 1

    if args.search_service is not None:
        args.search_service = get_service_list(args.search_service, args.case_insensitive)

    if args.exclude_service is not None:
        args.exclude_service = get_service_list(args.exclude_service, args.case_insensitive)

    contents = get_page_contents(region_table_url)
    countries, regions, services, results, countries_per_tab = process_page_contents(contents, args.use_regions)

    if not args.no_results:
        display_results(countries, regions, services, results, countries_per_tab, args)


# -------------------------------------------------------------------------------- #
# Make Parser                                                                      #
# -------------------------------------------------------------------------------- #
# Setup the command line parser.                                                   #
# -------------------------------------------------------------------------------- #

def make_parser():
    parser = argparse.ArgumentParser(description='List AWS Service Availability by Region')

    parser.add_argument('-i', '--case-insensitive', help='Make search/exclude matching case insensitive', action='store_true')
    parser.add_argument('-e', '--exclude-region', type=str, help='The region to exclude from the results', default=None)
    parser.add_argument('-E', '--exclude-service', type=str, help='The service to exclude from the results', default=None)
    parser.add_argument('-n', '--no-results', help='Do not show the final table of results', action='store_true')
    parser.add_argument('-r', '--use-regions', help='Use aws region names instead of country names', action='store_true')
    parser.add_argument('-s', '--search-region', type=str, help='The region to search the results for', default=None)
    parser.add_argument('-S', '--search-service', type=str, help='The service to search the results for', default=None)
    return parser


# -------------------------------------------------------------------------------- #
# Validate Region List                                                             #
# -------------------------------------------------------------------------------- #
# Validate the user supplied list of regions and skip any that are not valid.      #
# -------------------------------------------------------------------------------- #

def validate_region_list(region_string=None):
    regions = []

    if region_string is not None:
        region_list = region_string.strip().split(',')

        for reg in region_list:
            region = reg.lower()
            if valid_aws_region(region):
                regions.append(region)
            else:
                print("%s is not a valid region - skipping" % region)
    return regions


# -------------------------------------------------------------------------------- #
# Get Service List                                                                 #
# -------------------------------------------------------------------------------- #
# Generate a list of services based on a user supplied comma separated list. If    #
# needed lowercase the list.                                                       #
# -------------------------------------------------------------------------------- #

def get_service_list(service_list, case_insensitive):
    services = []

    services = service_list.strip().split(',')
    if case_insensitive:
        services = map(lambda x: x.lower(), services)
    return services


# -------------------------------------------------------------------------------- #
# Get Page Content                                                                 #
# -------------------------------------------------------------------------------- #
# Pull the information from the Amazon regional table web page.                    #
# -------------------------------------------------------------------------------- #

def get_page_contents(url):
    r = requests.get("https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/")
    return r.content


# -------------------------------------------------------------------------------- #
# Process Page Contents                                                            #
# -------------------------------------------------------------------------------- #
# Process the HTML and pull out the tables from the various tabs that we require.  #
# Use this to generate 4 lists of information that will be used for display.       #
# -------------------------------------------------------------------------------- #

def process_page_contents(contents, use_regions=False):
    regions = ['']
    countries = ['']
    services = []
    results = []
    countries_per_tab = []

    soup = BeautifulSoup(contents, 'lxml')
    tables = soup.find_all('table')

    for table in tables:
        cpt = 0
        table_rows = table.find_all('tr')

        rows = []
        first_row = True
        for tr in table_rows:
            table_cells = tr.find_all('td')
            cells = []
            first_column = True
            for td in table_cells:
                cell = td.get_text().strip()

                cell = cell.replace(six.unichr(10003), "Y")             # Convert a 'check mark' to Y
                cell = unidecode(cell)					# Decode the rest
                cell = 'N' if not cell else cell

                if first_row and not first_column:
                    cell = cell.replace('*', "")
                    countries.append(cell)

                    region_name = get_region_from_region_table_name(cell)
                    regions.append(region_name)

                    cpt += 1
                elif first_column and not first_row:
                    if cell not in services:
                        services.append(cell)
                    cells.append(cell)
                elif cell != 'Services Offered:':
                    cells.append(cell)
                first_column = False
            if len(cells) > 0:
                rows.append(cells)
            first_row = False
        results.append(rows)
        countries_per_tab.append(cpt)

    return countries, regions, services, results, countries_per_tab


# -------------------------------------------------------------------------------- #
# Valid AWS Region                                                                 #
# -------------------------------------------------------------------------------- #
# Check the mast awe_region_list and check to see if the given name is in it.      #
# -------------------------------------------------------------------------------- #

def valid_aws_region(region):
    for r in aws_region_list:
        if (r['region'] == region):
            return True
    return False


# -------------------------------------------------------------------------------- #
# Get Region From Region Table Name                                                #
# -------------------------------------------------------------------------------- #
# The region table web page uses non standard names for the locations, so this     #
# allows us to locate the aws standard region name/code.                           #
# -------------------------------------------------------------------------------- #

def get_region_from_region_table_name(region_table_name):
    for r in aws_region_list:
        if (r['region_table_name'] == region_table_name):
            return r['region']
    return region_table_name


# -------------------------------------------------------------------------------- #
# Pad or Truncate                                                                  #
# -------------------------------------------------------------------------------- #
# Take a list and either pad it out or truncate it down to a given size.           #
#                                                                                  #
# If you pad it out you can specify a default value to use, if you truncate it it  #
# will use the first N entries.                                                    #
# -------------------------------------------------------------------------------- #

def pad_or_truncate(list, target_len, str='N'):
    return list[:target_len] + [str]*(target_len - len(list))


# -------------------------------------------------------------------------------- #
# Get Row by Service                                                               #
# -------------------------------------------------------------------------------- #
# Search across a table for a given service row, the service string is in the      #
# first column, this is important for stiching together the 3 different data       #
# tables that were created when we processed the webpage content. Pad if needed.   #
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
# Get Rows by Service Wrapper                                                      #
# -------------------------------------------------------------------------------- #
# A wrapper to process all 3 tables and pull out the information that we needed.   #
# -------------------------------------------------------------------------------- #

def get_rows_by_service_wrapper(service, tables, countries_per_tab):
    rows = []

    rows.append(service)

    for i in range(len(countries_per_tab)):
        rows += get_row_by_service(service, tables[i], countries_per_tab[i])
    return rows


# -------------------------------------------------------------------------------- #
# Extract Columns                                                                  #
# -------------------------------------------------------------------------------- #
# Copy spcific columns by index() from a given list.                               #
# -------------------------------------------------------------------------------- #

def extract_columns(list, indexes):
    results = []

    if len(indexes):
        results.append(list[0])
        for i in indexes:
            results.append(list[i])
    else:
        results = list

    return results


# -------------------------------------------------------------------------------- #
# Exclude Columns                                                                  #
# -------------------------------------------------------------------------------- #
# Copy all columns except those of a specific index.                               #
# -------------------------------------------------------------------------------- #

def exclude_columns(list, indexes):
    results = []

    for i in range(len(list)):
        if i not in indexes:
            results.append(list[i])

    return results


# -------------------------------------------------------------------------------- #
# Filter Columns                                                                   #
# -------------------------------------------------------------------------------- #
# Simple wrapper to handle the search/exclude/nothing combintion.                  #
# -------------------------------------------------------------------------------- #

def filter_columns(list, indexes, filter):
    results = []

    if filter == 1:
        results = extract_columns(list, indexes)
    elif filter == 2:
        results = exclude_columns(list, indexes)
    else:
        results = list
    return results


# -------------------------------------------------------------------------------- #
# Build Index List                                                                 #
# -------------------------------------------------------------------------------- #
# Based on a list of search/exclude terms create a list their index().             #
# -------------------------------------------------------------------------------- #

def build_index_list(list, search_list):
    indexes = []

    for item in search_list:
        try:
            index = list.index(item)
            indexes.append(index)
        except ValueError:
            pass

    return indexes


# -------------------------------------------------------------------------------- #
# Display Results                                                                  #
# -------------------------------------------------------------------------------- #
# Up until this point there has been no includsion or exclusion of any rows or     #
# columns and we have the complete data set. This function takes all of the data   #
# any inclusion or exclusion lists for services/regions and works out what data    #
# should be shown to the end user.                                                 #
#                                                                                  #
# The aim/key to this is to be as dynamic as possible, so if Amazon add more       #
# services to the webpage or more countries, or more tabs then the code should be  #
# able to handle that without requiring any changes.                               #
# -------------------------------------------------------------------------------- #

def display_results(countries, regions, services, results, countries_per_tab, args=None):
    indexes = []

    filter = 3

    #
    # Create a list of indexes for any given include/exclude regions.
    #
    if args.search_region is not None:
        filter = 1
        indexes = build_index_list(regions, args.search_region)
    elif args.exclude_region is not None:
        filter = 2
        indexes = build_index_list(regions, args.exclude_region)

    table = PrettyTable()

    #
    # Filter the table headings so that only the required ones are there
    #
    if args.use_regions:
        table.field_names = filter_columns(regions, indexes, filter)
    else:
        table.field_names = filter_columns(countries, indexes, filter)

    #
    # Process each service and display if wanted.
    #
    for service in services:
        display_service = service						# Keep for display purposes

        if args.case_insensitive:						# case-insensitive ??
            service = service.lower()

        include = False								# Default to don't show

        if args.search_service is not None:					# Are we searching?
            if any(s in service for s in args.search_service):			# Partial string match
                include = True
        else:									# No search terms so include
            include = True

        if args.exclude_service is not None:					# Anything to exclude?
            if any(s in service for s in args.exclude_service):			# Partial string match
                include = False

        if include:								# Do we need to show it ??
            row = get_rows_by_service_wrapper(display_service, results, countries_per_tab)
            row = filter_columns(row, indexes, filter)				# Filter the columns
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
