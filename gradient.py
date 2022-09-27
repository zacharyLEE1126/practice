import random

import numpy as np

def get_examples(number):
    x = [int(40 * random.random()) for i in range(number)]
    examples = []
    for i in range(len(x)):
        if x[i] > 20:
            examples.append((x[i], 1))
        else:
            examples.append((x[i], 0))

    return examples


def mean_square_error(y_calc, y_real):
    if len(y_calc) == len(y_real):
        error = np.sum(np.square(y_calc - y_real)) / len(y_calc)
        return error


def gradient_descent(x_input, y_input, num_iteration, alpha, threshold):  # alpha = recursive rate
    w = 0.01
    b = 1  # initialize index w and b
    x_input = np.array(x_input)
    y_input = np.array(y_input)
    iterations = num_iteration
    alpha = alpha
    threshold = threshold
    previous_cost = None
    count = 0
    n = float(len(x_input))
    for i in range(iterations):
        y_calc = x_input * w + b
        current_cost = mean_square_error(y_calc, y_input)
        if previous_cost and abs(current_cost - previous_cost) <= threshold:
            print("Number of iterations = ", count)
            break
        previous_cost = current_cost

        w_gradient = -(2 / n) * np.dot(x_input, (y_input - y_calc))  # base on partial derivative of MSE
        b_gradient = -(2 / n) * np.sum(y_input - y_calc)

        w = w - (alpha * w_gradient)
        b = b - (alpha * b_gradient)
        count += 1

    return w, b
#zzl

num = 10000  # num of samples
examples_out = get_examples(num)
x = []
y = []
for j in range(num):
    x.append(examples_out[j][0])
    y.append(examples_out[j][1])

[w_test, b_test] = gradient_descent(x, y, 100000, 0.0001, 1e-6)
print("w=", w_test, "b=", b_test)

# generate test dataset for testing w and b
num_test = 100
examples_test = get_examples(num_test)
examples_test = np.array(examples_test)
accuracy_count = 0
for m in range(num_test):
    x_test = examples_test[m][0]
    y_test = x_test * w_test + b_test
    if x_test > 20 and y_test > 0.5:
        accuracy_count += 1
    elif x_test <= 20 and y_test <= 0.5:
        accuracy_count += 1
accurate_rate = accuracy_count / num_test
print('For given number of dataset, the accuracy rate is %f' % accurate_rate)
