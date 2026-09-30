def neuron(inputs, weights, bias):
    total = 0
    for input, weight in zip(inputs, weights):
        total += input * weight
    return total + bias

def layer(inputs, weights, bias):
    outputs = []
    for w, b in zip(weights, bias):
        outputs.append(neuron(inputs, w, b))
    return outputs

inputs = [0.8, 0.9]
weights = [
    [0.5, 0.2],
    [0.1, 0.8],
    [0.7, -0.3]
]
bias = [
    0.1,
    0.2,
    0.3
]

outputs = layer(inputs, weights, bias)
print(outputs)