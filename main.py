with open("sample.txt", "r") as file: # Open the file in read mode
    content=file.read() # Read the content of the file
    words = content.split() # Split the content into words

hashes = [] # Initialize an empty list to store hashed letter counts for each word

for word in words: # Iterate through each word
    letters = []
    for letter in word: # Iterate through each letter in the word
        letters.append(letter) # Append the letter to the letters list
    letters.sort() # Sort the letters in alphabetical order
    letters = ''.join(letters) # Join the sorted letters back into a string
    hashes.append(hash(letters)) # Append the hash of the sorted letters to the hashes list

while hashes: # While there are hashes in the list
    hash = hashes[0] # Get the first hash
    # Find all words with the same hash (anagrams) and print them
    for i in range(0, len(hashes)): # Iterate through the rest of the hashes
        if hashes[i] == hash: # If the current hash matches the first hash
            print(f"{words[i]} ", end="") # Print the corresponding word
    print()
    
    # Remove all occurrences of this hash and corresponding words
    indices_to_remove = []
    for i in range(len(hashes)):
        if hashes[i] == hash:
            indices_to_remove.append(i)
    
    # Remove in reverse order to avoid index shifting issues
    for i in reversed(indices_to_remove):
        hashes.pop(i)
        words.pop(i)