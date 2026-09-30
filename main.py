def neuron(input, weights):
    return (input[0] * weights[0]) + (input[1] * weights[1])

def loss(prediction, target):
    return (target - prediction) ** 2

def gradient(input, prediction, target):
    return [
        2 * (prediction - target) * input[0],
        2 * (prediction - target) * input[1]
    ]

input = [0.8, 0.9]
weights = [0.52, 0.2]
target = 1
learning_rate = 0.1

while True:

    prediction = neuron(input, weights)

    loss_value = loss(prediction, target)

    print(loss_value)

    if loss_value < 0.01:
        break

    gradients = gradient(input, prediction, target)

    weights[0] -= learning_rate * gradients[0]
    weights[1] -= learning_rate * gradients[1]

print(weights)