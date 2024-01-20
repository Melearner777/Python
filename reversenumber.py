# Program to split a sentence into words and convert them to uppercase within the list

# Input: Get a sentence from the user
sentence = input("Enter a sentence: ")

# Step 1: Split the sentence into words
words_list = sentence.split()

# Step 2: Initialize an empty list to store the uppercase words
uppercase_words_list = []

# Step 3: Iterate through each word in the list
for word in words_list:
    # Step 3: Convert the word to uppercase and append it to the new list
    uppercase_words_list.append(word.upper())

# Step 4: Print the list of uppercase words
print("List of Uppercase Words:", uppercase_words_list)
