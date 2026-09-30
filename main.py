def neuron(inputs, weights):
    return (
        inputs[0] * weights[0] +
        inputs[1] * weights[1]
    )

def layer(inputs, weights):
    outputs = []
    for weight in weights:
        outputs.append(neuron(inputs, weight))
    return outputs

inputs = [0.8, 0.9]
weights = [
    [0.5, 0.2],
    [0.1, 0.8],
    [0.7, -0.3]
]

outputs = layer(inputs, weights)