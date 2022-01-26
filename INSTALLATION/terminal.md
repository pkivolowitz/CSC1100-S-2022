# Some Terminal Lessons

You will be using the MacOS terminal a great deal. It would be best if you glued the terminal to your dock. Use Spotlight Search and enter "terminal" without the quotes. Then, right click on the terminal icon in the dock and select Options → Keep in Dock.

Here is a very brief first taste of using the terminal.

## cd

When you enter the terminal, you are "in" your home directory. Navigating directories will be a critical skill when using the terminal. The "cd" command changes the directory you are "in".

| command | meaning |
| --- | --- |
| `cd` |  cd by itself moves you back to your home directory |
| `cd dir_name` | attempts to change the directory you are "in" to the named directory. |
| `cd ..` | moves you up one directory level |

## pwd

The pwd command "prints the working directory" - i.e. it will print the full path of the directory you are "in" right now.

## ls

The ls command prints a "list" of the current directory OR another file system entity if you specify one.

| command | meaning |
| --- | --- |
| `ls`  | lists the contents of the current directory |
| `ls dir_name`  | lists the contents of the indicated directory |

## ls -l

It is possible to modify the operation of various commands using "command line options". The -l (dash el) option to ls causes it to print its "long" listing - details about the contents such as dates and sizes.

## mkdir

You will need to create new folders / directories. This is done with mkdir.

| command | meaning |
| --- | --- |
| `mkdir new_dir_name`  | attempts to create the indicated directory |