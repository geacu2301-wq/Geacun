def words_emrge_frequency(text):
    words = text.split()
    word_freq = {}
    for w in words:
        if w in word_freq:
            word_freq[w] += 1
        else:
            word_freq[w] = 1
    return word_freq

text = input()
result = words_emrge_frequency(text)
print("Word frequencies:")
for word, freq in result.items():
    print(f"{word}: {freq}")

sorted_words = sorted(result.items(), key=lambda x: x[1], reverse=True)

top5 = dict(sorted_words[:5])
print("\nTop 5 most frequent words:")
for word, freq in top5.items():
    print(f"{word}: {freq}")
total_words = len(text.split())
top5_total = sum(top5.values())
print("\nTotal number of words:", total_words)
proportion = (top5_total / total_words) * 100
print(f"Proportion of 5 most common words: {top5_total} / {total_words} = {proportion:.2f}%")