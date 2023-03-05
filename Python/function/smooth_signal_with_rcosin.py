import numpy as np
import matplotlib.pyplot as plt


def rectangular_pulse(t, width):
    """
    Computes the values of a rectangular pulse for a given time array and pulse width.

    Args:
    t (array): Array of time values.
    width (float): Width of the rectangular pulse.

    Returns:
    array: The values of the rectangular pulse.
    """
    y = np.zeros_like(t)
    idx = np.where(np.abs(t) <= width / 2)
    y[idx] = 1
    return y


def raised_cosine_filter(t, beta):
    """
    Computes the values of a raised cosine filter for a given time array and beta value.

    Args:
    t (array): Array of time values.
    beta (float): Beta value for the raised cosine filter.

    Returns:
    array: The values of the raised cosine filter.
    """
    x = np.abs(t)
    y = np.zeros_like(x)
    idx = np.where(x <= (1 - beta) / 2)
    y[idx] = 1
    idx = np.where((1 - beta) / 2 < x)
    y[idx] = 0.5 * (1 + np.cos((np.pi / beta) * (x[idx] - (1 - beta) / 2)))
    return y


if __name__ == '__main__':
    t = np.linspace(-10, 10, 1000)
    width = 2
    beta = 0.05

    rect_pulse = rectangular_pulse(t, width)
    raised_cosine = raised_cosine_filter(t, beta)

    convolved = np.convolve(rect_pulse, raised_cosine, mode='same')

    plt.subplot(2, 1, 1)
    plt.plot(t, rect_pulse, label='Rectangular Pulse')

    plt.subplot(2, 1, 2)
    plt.plot(t, rect_pulse, label='Rectangular Pulse')
    plt.plot(t, raised_cosine, label='Raised Cosine Filter')
    plt.plot(t, convolved, label='Convolved Signal')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    # plt.title(f'Rectangular signal with raised cosine filter (beta = {beta})')
    plt.legend()
    plt.show()
