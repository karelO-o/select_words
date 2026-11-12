import pandas as pd
from wordfreq import zipf_frequency

# Load data
df = pd.read_csv('./Warriner2013.csv')

# Split data into three categories
positive_words = df[(df["valence_mean"] > 7.5) & (df["word_english"].str.len() <= 5)]
negative_words = df[(df["valence_mean"] < 2.5) & (df["word_english"].str.len() <= 5)]
neutral_words = df[(df["valence_mean"].between(4.8, 5.2)) & (df["word_english"].str.len() <= 5)]

# Randomly sample 50 words into each category
positive_select = positive_words.sample(n=50, random_state=12)["word_english"].tolist()
negative_select = negative_words.sample(n=50, random_state=12)["word_english"].tolist()
neutral_select = neutral_words.sample(n=50, random_state=12)["word_english"].tolist()

# Item order by word frequency
def order_by_frequency(words):
    temp = []
    for word in words:
        temp.append((zipf_frequency(word, "en"), word))  # (frequency, word)
    temp.sort(reverse=True)

    ordered = []
    for frequency, word in temp:
        ordered.append(word)
    return ordered

# Print selected words in each category
# Take only first 20 words in each array
print("🟢 Positive Words:", order_by_frequency(positive_select)[:20])
print("🔴 Negative Words:", order_by_frequency(negative_select)[:20])
print("⚪ Neutral Words:", order_by_frequency(neutral_select)[:20])
