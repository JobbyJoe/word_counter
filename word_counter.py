# word_counter.py
def count_words(text):
	words = text.split()
	return len(words)

def count_unique_words(text):
	words = set(text.split())
	return len(words)

def save_count_to_file(count, filename="word_count.txt"):
	with open(filename, "w") as file:
		file.write(f"Word count: {count}\n")

if __name__ == "__main__":
	text = input("Enter some text: ")
	count = count_words(text)
	unique_count = count_unique_words(test)
	print("Word count:", count)
	print("Unique word count:", unique_count)
	save_count_to_file(count)
