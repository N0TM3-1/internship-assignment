# Internship assignment: Anagram finder

This program finds and groups anagrams from a list of words provided in a text file.

## Description

The anagram finder reads words from `sample.txt` and groups words that are anagrams of each other. Anagrams are words that contain the same letters but in a different order (e.g., "act", "cat", "tac").

## Requirements

- Python 3.x (tested with Python 3.11.2)
- No external dependencies required

## How to Build and Run

### Prerequisites

Make sure you have Python installed on your system. You can check if Python is installed by running:

```bash
python --version
```

or

```bash
python3 --version
```

### Running the Program

1. **Clone or download the project** to your local machine.

2. **Navigate to the project directory**:

   ```bash
   cd internship-assignment
   ```

3. **Ensure the input file exists**: The program expects a file named `sample.txt` in the same directory. A sample file is already provided with test words.

4. **Run the program**:
   ```bash
   python main.py
   ```
   or if you have both Python 2 and 3 installed:
   ```bash
   python3 main.py
   ```

### Expected Output

The program will output groups of anagrams, with each group on a separate line. For example:

```
act cat
tree
race care acre
bee
```

### Using Your Own Word List

To use your own word list:

1. Replace the contents of `sample.txt` with your own words (one word per line)
2. Run the program as described above

### File Structure

```
internship-assignment/
├── main.py          # Main program file
├── sample.txt       # Input file containing words
└── README.md        # This file
```

## How It Works

1. The program reads all words from `sample.txt`
2. For each word, it sorts the letters alphabetically and creates a hash
3. Words with the same hash are anagrams
4. The program groups and displays all anagrams together

## Troubleshooting

- **File not found error**: Make sure `sample.txt` exists in the same directory as `main.py`
- **Permission denied**: Ensure you have read permissions for the `sample.txt` file
- **No output**: Check that `sample.txt` contains words and is not empty
