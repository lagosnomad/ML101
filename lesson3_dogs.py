import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random(greyhounds)
lab_height = 28 + 4 * np.random(labs)

plt.hist(
    [
        grey_height,
        lab_height,
    ],
    stacked = True,
    color = ['r', 'b']
)
plt.show()
