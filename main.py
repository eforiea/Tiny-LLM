def neuron(inputs, weights, bias):
    total = inputs * weights
    return total + bias

def relu(x):
    return max(0, x)

def loss(predictions, targets):
    loss_value = (targets - predictions) ** 2
    return loss_value

x = 2

w1 = 3
b1 = 1

w2 = 4
b2 = 2

target = 20
learning_rate = 0.01

while True:
    z1 = neuron(x, w1, b1)
    z2 = neuron(z1, w2, b2)

    prediction = z2
    loss_value = loss(prediction, target)

    print(loss_value)
    if loss_value < 0.01:
        break

    w2_gradient = 2*(prediction - target)*z1
    b2_gradient = 2*(prediction - target)
    w1_gradiant = 2*(prediction - target)*w2*x
    b1_gradiant = 2*(prediction - target)*w2

    w2 -= learning_rate * w2_gradient
    b2 -= learning_rate * b2_gradient
    w1 -= learning_rate * w1_gradiant
    b1 -= learning_rate * b1_gradiant

print(f"z1: {z1}")
print(f"prediction: {prediction}")
print(f"loss: {loss_value}")