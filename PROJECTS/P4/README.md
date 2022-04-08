# Secret Picture Decoder

In this project, you will write a short program that reads and decodes a csv file containing a secret picture.

The entire program should be no more than 30 lines, to set your expectations.

## Input

Your input is a csv file.

The first line contains two numbers such as `10,30`. This means your secret picture has 10 lines and 30 columns.

The remainder of the file is a jumbled mess of 3 fields per line such as `42,20,"H"`. This means, an `H` goes in the 21st column of the 43rd line (counting from 0).

## Outline

Here is an outline of one possible solution:

```python
from sys import argv
import csv

def main(filename):
	# Open the file
	# Wrap the file with a csv reader
	# Get only the first line using next()
	# Decode the number of lines and columns
	# Create a board filled with spaces. For example:
	#     board = [[' ' for x in range(int(dimensions[1]))] for y in range(int(dimensions[0]))]
	# For all the remaining lines in reader:
	#     Decode line, column and letter.
	#     Put letter into the right place in board
	# For each line in board:
	#     For each letter in line:
	#         Print letter without a newline
	#     Print a newline

if __name__ == "__main__":
	if len(argv) > 1:
		main(argv[1])
	else:
		print('Must specify a data file.')
```

This line:

```python
board = [[' ' for x in range(int(dimensions[1]))] for y in range(int(dimensions[0]))]
```

assumes you read the first line of the csv file into a variable called `dimensions`.

Breaking this line down, it has two parts:

```python
[' ' for x in range(int(dimensions[1]))]
```

creates a list containing a space for each column (number of columns given by `int(dimensions[1])`).

This next part:

```python
for y in range(int(dimensions[0]))]
```

creates one such list of spaces for each row (rows given by `int(dimensions[0])`)

## Running the program

Run your program giving one of the following two files as a command line argument.

[file 1](./data1.txt)

[file 2](./data2.txt)

For example (on the mac): `python3 myproj.py data1.txt`

If you don't crash and all else is correct, you'll see a picture!
