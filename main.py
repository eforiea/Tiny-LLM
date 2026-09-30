def neuron(input, weights):
    sum = (input[0] * weights[0]) + (input[1] * weights[1])
    return sum

def loss(input, weights, target):
    prediction = neuron(input, weights)
    return (target - prediction) ** 2

def loss_change(input, weights, target, index):
    primary_loss = loss(input, weights, target)
    weights[index] += 0.1
    scondary_loss = loss(input, weights, target)
    weights[index] -= 0.1
    return (scondary_loss - primary_loss)

def gradient(input, weights, target, index):
    delta_loss = loss_change(input, weights, target, index)
    return (delta_loss / 0.1)

input = [0.8, 0.9]
weights = [0.5, 0.2]
target = 1
learning_rate = 0.1

while True:
    gradients = [gradient(input, weights, target, 0), gradient(input, weights, target, 1)]
    loss_value = loss(input, weights, target)
    print(loss_value)
    if loss_value < 0.01:
        break
    weights[0] -= learning_rate * gradients[0]
    weights[1] -= learning_rate * gradients[1]

print(weights)