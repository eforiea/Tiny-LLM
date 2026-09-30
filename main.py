def neuron(input, weights):
    sum = (input[0] * weights[0]) + (input[1] * weights[1])
    return sum

print(neuron([0.8, 0.2], [0.5, 0.5])) #result: 0.5
print(neuron([0.8, 0.2], [1.0, 0.0])) # 0.8
print(neuron([0.8, 0.2], [0.0, 1.0])) # 0.2
print(neuron([0.8, 0.2], [2.0, -1.0])) # 1.4