parts = ["I", "like", "cats", "dogs", "birds"]

def encode(text):
    tokens = [parts.index(x) for x in text.split()]
    return tokens

def decode(tokens):
    text = " ".join([parts[x] for x in tokens])
    return text

tokens = encode("I like cats")
print(tokens)

text = decode(tokens)
print(text)