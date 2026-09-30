parts = {
    "I": [0, 0, 0, 1], #[id, action, animal, pronoun]
    "like": [1, 1, 0, 0],
    "cats": [2, 0, 1, 0],
    "dogs": [3, 0, 1, 0],
    "birds": [4, 0, 1, 0]
    }

def encode(text):
    tokens = [parts[x] for x in text.split()]
    return tokens

def decode(tokens):
    words = []
    for x in tokens:
        for key,val in parts.items():
            if x == val:
                words.append(key)
    text = " ".join(words)
    return text

tokens = encode("I like cats")
print(tokens)

text = decode(tokens)
print(text)