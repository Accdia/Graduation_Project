import numpy as np


def raised_root_cosine(upsample, num_positive_lobes, alpha):
    """
    Root raised cosine (RRC) filter (FIR) impulse response.

    upsample: number of samples per symbol

    num_positive_lobes: number of positive overlaping symbols
    length of filter is 2 * num_positive_lobes + 1 samples

    alpha: roll-off factor
    """

    N = upsample * (num_positive_lobes * 2 + 1)
    t = (np.arange(N) - N / 2) / upsample

    # result vector
    h_rrc = np.zeros(t.size, dtype=np.float)

    # index for special cases
    sample_i = np.zeros(t.size, dtype=np.bool)

    # deal with special cases
    subi = t == 0
    sample_i = np.bitwise_or(sample_i, subi)
    h_rrc[subi] = 1.0 - alpha + (4 * alpha / np.pi)

    subi = np.abs(t) == 1 / (4 * alpha)
    sample_i = np.bitwise_or(sample_i, subi)
    h_rrc[subi] = (alpha / np.sqrt(2)) \
                  * (((1 + 2 / np.pi) * (np.sin(np.pi / (4 * alpha))))
                     + ((1 - 2 / np.pi) * (np.cos(np.pi / (4 * alpha)))))

    # base case
    sample_i = np.bitwise_not(sample_i)
    ti = t[sample_i]
    h_rrc[sample_i] = np.sin(np.pi * ti * (1 - alpha)) \
                      + 4 * alpha * ti * np.cos(np.pi * ti * (1 + alpha))
    h_rrc[sample_i] /= (np.pi * ti * (1 - (4 * alpha * ti) ** 2))

    return h_rrc
