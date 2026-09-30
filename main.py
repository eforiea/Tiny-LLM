def neuron(input, weights):
    sum = (input[0] * weights[0]) + (input[1] * weights[1])
    return sum

def loss(prediction, target):
    return (target - prediction) ** 2

input = [0.8, 0.2]
weights = [0.5, 0.5]
target = 1
while True:
    prediction = neuron(input, weights)
    loss_value = loss(prediction, target)
    if loss_value < 0.01:
        break
    if (target - prediction) > 0:
        if input[0] >= input[1]:
            weights[0] += 0.1
        else:
            weights[1] += 0.1
    else:
        if input[0] >= input[1]:
            weights[0] -= 0.1
        else:
            weights[1] -= 0.1

print(weights)