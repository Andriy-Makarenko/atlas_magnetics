import statistics as st


data_set = [364, 373, 358, 394, 378, 379, 357, 364, 350, 363, 392, 368, 359, 375, 399, 365, 379, 357, 380]


print(
    f"mean - {st.mean(data_set)}",
    f"median - {st.median(data_set)}",
    # returns all occurrences without repetitions
    f"mode - {st.multimode(data_set)}",
    f"standard deviation - {st.stdev(data_set)}",
    sep="\n",
)
