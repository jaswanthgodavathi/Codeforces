a = input().strip()
words = [word for word in a.split("WUB") if word]
original_song = " ".join(words)
print(original_song)

