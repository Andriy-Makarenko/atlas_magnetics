import numpy as np
from scipy import stats as st

data_set = [
    364, 373, 358, 394, 378, 379, 357, 364, 350,
    363, 392, 368, 359, 375, 399, 365, 379, 357, 380
]


print(
    f"mean - {np.mean(data_set)}",
    f"median - {np.median(data_set)}",
    # returns only one value-repetition occurrence for multiple occurrences
    f"mode - {st.mode(data_set, keepdims=True)}",
    f"standard deviation - {np.std(data_set)}",
    sep="\n",
)
