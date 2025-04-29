# BookBot

BookBot is a command-line text analysis tool that generates statistics about books or other text files. It was created as a project for [Boot.dev](https://www.boot.dev).

## Features

- Count the total number of words in a text file
- Count the frequency of each character in the text
- Generate a report with sorted character frequencies (alphabetic characters only)
- Simple command-line interface

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/tomclarke25/bookbot.git
   cd bookbot
   ```

2. No additional dependencies are required as BookBot uses only Python standard libraries.

## Usage

Run BookBot by providing the path to a text file as a command-line argument:

```
python main.py books/frankenstein.txt
```

### Example Output

```
=========== BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
r: 20818
h: 19725
l: 16659
d: 14595
u: 10795
c: 9613
m: 9577
f: 8807
p: 7429
g: 6641
w: 6095
y: 5747
b: 4900
v: 3720
k: 2088
x: 677
j: 504
q: 324
z: 243
```

## Project Structure

- `main.py`: The main program file that handles command-line arguments and generates the report
- `stats.py`: Contains functions for calculating word and character statistics
- `books/`: Directory containing sample text files for analysis
  - `frankenstein.txt`: Mary Shelley's "Frankenstein"
  - `mobydick.txt`: Herman Melville's "Moby Dick"
  - `prideandprejudice.txt`: Jane Austen's "Pride and Prejudice"

## How It Works

1. The program reads the specified text file
2. It counts the total number of words by splitting on whitespace
3. It counts the frequency of each character (case-insensitive)
4. It sorts the characters by frequency (highest to lowest)
5. It generates a formatted report showing the results

## License

This project is open source and available for educational purposes.
