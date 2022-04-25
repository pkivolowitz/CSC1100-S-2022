# This program will read and plot gold prices since 1950 (to 2018)
# It attempts to open the data file specified on the command line.
# If the command line does not include a file name, print an error
# and exit.
# The data file will be a csv containing two columns (date and price).
# To use CSV, we have to open the file and then wrap it in a csv
# reader. The first line of the file contains headings, which can
# be skipped.

from sys import argv
from matplotlib import pyplot as plt
import csv

def main():
	with open(argv[1]) as in_file:
		reader = csv.reader(in_file)
		# chose not to use DictReader() - if I wanted to use DictReader()
		# this next line would NOT be used...
		next(reader)
		# Create the lists that will hold the data as it is read.
		dates = []
		prices = []
		# Read every available line adding the contents to dates and prices.
		for line in reader:
			# line is a list which should have two members - make sure this
			# is correct. Skip any line which doesn't meet this expectation.
			if len(line) != 2:
				continue
			# If I get here, line contains two items.
			# line[0] is the date (string)
			# line[1] is the price (string)
			# Add the newest line's contents to the two lists.
			dates.append(line[0])
			prices.append(float(line[1]))
		# When we get here the data has been read and the file closed.
		# Now, we can start formatting out graph. But dates is still
		# composed of strings... what to do?
		x_axis = range(len(dates))
		plt.plot(x_axis, prices)
		plt.xticks(x_axis, dates, rotation=45)
		plt.show()

if __name__ == "__main__":
	if len(argv) < 2:
		print('Must supply a file name.')
		exit(-1)
	main()
