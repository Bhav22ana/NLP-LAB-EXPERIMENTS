import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

# Download required resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# For newer NLTK versions (3.9+), uncomment the following line if needed:
# nltk.download('averaged_perceptron_tagger_eng')

# Get input from user
text = input("Enter a sentence: ")

# Tokenize sentence
tokens = word_tokenize(text)

# Perform POS tagging
tagged_words = pos_tag(tokens)

# Display tokens
print("\nTokens:")
print(tokens)

# Display POS tags
print("\nPOS Tags:")
for word, tag in tagged_words:
    print(word, "->", tag)

# Simple tag meanings
print("\nTag Meanings:")
print("NN  -> Noun")
print("NNS -> Plural Noun")
print("NNP -> Proper Noun")
print("VB  -> Verb (Base Form)")
print("VBD -> Verb (Past Tense)")
print("VBG -> Verb (Gerund/Present Participle)")
print("VBN -> Verb (Past Participle)")
print("VBP -> Verb (Present Tense)")
print("VBZ -> Verb (3rd Person Singular)")
print("JJ  -> Adjective")
print("RB  -> Adverb")
print("PRP -> Pronoun")
print("DT  -> Determiner")

# Count tagged words
print("\nTotal Words:", len(tokens))