import numpy as np

# in_channel = 3 : kernel 3 channel
# out_channel = 128 : 128 kernel
input_data = np.random.random((800, 600, 3))  # in_channel = 3


# kernel_width = 3
# kernel_height = 3
# kernel_channel_num = 3
# kernel_num = 128


def cross_conv_impl(input_dataset, in_channel, out_channel, kernel_width, kernel_height, stride):
    cross_conv = np.ones((kernel_width, kernel_height, in_channel, out_channel))
    for i in range(in_channel):
        for j in range(out_channel):
            cross_conv[0][0][i][j] = 0
            cross_conv[0][2][i][j] = 0
            cross_conv[2][0][i][j] = 0
            cross_conv[2][2][i][j] = 0  # cross convolution kernel with 4 corner equals 0 in 3x3 kernel
    new_width = int((input_dataset.shape[0] - kernel_width) / stride + 1)
    new_height = int((input_dataset.shape[1] - kernel_height) / stride + 1)
    output = np.zeros((new_width, new_height, out_channel))
    for m in range(out_channel):
        for n in range(in_channel):
            for x in range(new_width):
                for y in range(new_height):
                    a = input_dataset[x:x + kernel_width, y:y + kernel_height, n]
                    b = cross_conv[:, :, n, m]
                    c = np.dot(a, b)
                    d = np.concatenate(c).sum()
                    output[x][y][m] += d

    return output


feature_map = cross_conv_impl(input_data, 3, 128, 3, 3, 1)
