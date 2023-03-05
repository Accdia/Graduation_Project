import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':

    # Set the filter parameters
    alpha = 0.5 # Roll-off factor
    sps = 8 # Samples per symbol
    span = 8 # Filter span in symbols

    # Generate the impulse response
    t = np.arange(-4*span, 4*span+1)
    h = np.sinc(t/sps)*np.sqrt(np.cos(np.pi*alpha*t/sps)/(1-4*alpha*alpha*t*t/sps/sps))

    # Plot the impulse response
    plt.plot(t, h)
    plt.xlabel('Time (symbols)')
    plt.ylabel('Amplitude')
    plt.title('Square Root Raised Cosine Impulse Response')
    plt.show()