import os

script_dir = os.path.dirname(os.path.abspath(__file__))
corpus_path = os.path.join(script_dir, "data", "corpus.txt")
saved_vocab_path = os.path.join(script_dir, "saved_tokenizer")

from tokenizer import CharTokenizer

with open(corpus_path, "r") as f:
    text = f.read()

tokenizer = CharTokenizer()

print("\nLoading tokenizer...")
is_empty, message = tokenizer.load(saved_vocab_path)
print(message)

print("Training tokenizer...")
tokenizer.train(text)
print(tokenizer.vocab)

sample = "Hello World!"
encoded = tokenizer.encode(sample)
decoded = tokenizer.decode(encoded)

print(f"Original: {sample}")
print(f"Encoded: {encoded}")
print(f"Decoded: {decoded}")