def neuron(input):
    sum = input[0] + input[1]
    if sum >= 1.0:
        return "animal"
    if sum >= 0.5:
        return "action"
    if sum < 0.5:
        return "pronoun"

print(neuron([0.8, 0.2]))
print(neuron([0.1, 0.9]))
print(neuron([0.3, 0.2]))
print(neuron([0.2, 0.2]))