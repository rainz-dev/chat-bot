import os
import json

class CharTokenizer:
    def __init__(self):
        self.vocab = {}
        self.id_to_char = {}

    def train(self, text):
        unique_chars = sorted(set(text))

        for i, char in enumerate(unique_chars):
            self.vocab[char] = i
            self.id_to_char[i] = char

        for i, char in text:
            print(char)

    def encode(self, text):
        return [self.vocab[char] for char in text]

    def decode(self, ids):
        return ''.join([self.id_to_char[id] for id in ids])

    def save(self, directory):
        os.makedirs(directory, exist_ok=True)

        vocab_path = os.path.join(directory, "vocab.json")
        with open(vocab_path, "w", encoding="utf-8") as f:
            json.dump(self.vocab, f, indent=2, ensure_ascii=False)

    def load(self, directory):
        vocab_path = os.path.join(directory, "vocab.json")
        with open(vocab_path, "r", encoding="utf=8") as f:
            if not f:
                return True, "The following file is empty: vocab.json."
            self.vocab = json.load(f)
        
        self.id_to_char = {id: char for char, id in self.vocab.items()}

        return False, "Vocab data loaded successfully!"

