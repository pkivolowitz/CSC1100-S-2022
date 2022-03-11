# Bingo

The point of this project is to work with nested Python data types. In this case, you will build a bingo board out of a dictionary nested within a list nested within a list.

A secondary goal is to practice breaking down complicated problems into simpler problems using functions.

## Outline of the highest level

```text
initialize stuff
for each ball:
    increment the turn number
	apply the ball to the board (function call)
	check for winning conditions and handle (function call)
print results
```

## Drilling down initialization

### *"initialize stuff"*

```text
initialize the turn counter
initialize win status
initialize the board (this is a function call)
initialize the balls (this is a function call)
```

#### *"initialize the turn counter"*

At the end of the game, print how many ball drawings it took to win. This by itself is interesting, but it will also allow us to kind of play bingo as a class. We'll all run our own programs and who ever has the lowest number of turns to win, will be the winner.

After every ball is drawn in the main loop, the turn counter should be incremented.

#### *"initialize win status"*

The main loop of the game will continue while you've not won.

#### *"initialize the board"*

This function is somewhat complicated. See "The board".

#### *"initialize the balls"*

I wrote a separate function to initialize the balls.

The balls to be drawn are a list of integers from 1 to 75 that has been [shuffled](https://www.w3schools.com/python/ref_random_shuffle.asp). You can make a list from a range quite easily. The resulting list can be shuffled to put the sequence of integers (the balls) into a randomized order.

The following shows something **similar**:

```python
things = list(range(1,11))
shuffle(things)
```

`shuffle()` comes from the `random` module. It is not described in Zybooks so see the link given above.

## Drilling down into the main loop

### *"increment the turn counter"*

This is self-explanatory.

### *"apply the ball to the board"*

Each time through the main loop of the game, you'll consider a different ball. *apply the ball to the board* means the function you will write that checks the board for the presence of the current ball.

Even though (given the ball number) you technically only need to check one column, applying ball can be done via brute force - compare the current value to the value in every position on your board (of course, if you should find the value is present you can break out of the loop after marking the cell in the board as "called").

## *"check for winning conditions and handle"*

This needs a lot of drilling down in itself as there are many ways to win at bingo. The way I am proposing you do this is by breaking down all the ways to win into several functions so that the whole top level win-checker becomes just this:

```python
def CheckBoard(board):
    return CheckRows(board) or CheckColumns(board) or CheckDiagonals(board)
```

This is an example of one of Computer Science's "Great Ideas" called *abstraction*. Breaking down complex things into less complex things so that complexity can be hidden.

In my code, above, I divided checking all the different ways to win into their own functions. In fact, I found it convenient to break down `CheckDiagonals()` even further into:

```python
def CheckDiagonals(board):
    return CheckDiagonal1(board) or CheckDiagonal2(board)
```

## The board

A bingo board consists of 5 columns. Each column contains 5 numbers chosen from a group of 15. The first column may contain 1 through 15. The second column may contain 16 through 30 and so on. Notice the numbers column `n` (starting at 1) may contain are `(n - 1) * 15 + 1` through `n * 15`.

In this program the board will be built in the following way:

```text
* a board is a list 5 members long
   * each of these members is a list 5 members long
      * each of these members is a dictionary with two keys
```

The keys in the (innermost) dictionary are:

| key | value |
| --- | ----- |
| `ball` | identifies the ball that matches this spot on the board |
| `called` | `True` if the ball matching this spot has been called. False otherwise. |

Note that the middle spot (the third member of the third column) begins with its `called` set to `True`. All other spots beging with `called` being `False`.

I called the variable holding my entire board `board`. To access a single cell in my board, I would do it like this:

```python
board[column][row]['ball']
```

or

```python
board[column][row]['called']
```

## Printing without a new line

A reminder that you can avoid emitting a new line by specifying the value of the optional named parameter `end` to be an empty string.

```python
print('there will be no new line after this:', end='')
```

## Work rules

You may work together with a partner for this project. If you do so:

* **ONE** of you hands in the code - the code must include a comment indicating who your partner is
* The **OTHER** partner hands in a **text file** that indicates who the other partner is.

## What to hand in

See previous. Remember to zip up the python file.

## Due date

You have all of break and then a full week after break.
