import matplotlib as mpt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


if __name__ == '__main__':
    """
    x = np.linspace(0, 10, 100)
    fig, axes = plt.subplots(1, 2)
    y1 = pd.Series(np.sin(x))
    y2 = pd.Series(np.cos(x))
    y1.plot(ax=axes[0], label=r"$sin\left(x\right)$")
    y2.plot(ax=axes[1], label=r"$cos\left(x\right)$")
    lines, labels = fig.axes[-1].get_legend_handles_labels()
    plt.legend(lines, labels, loc="upper left", bbox_to_anchor=(1.05, 1.0))
    plt.tight_layout()
    plt.show()
    nums = [1, 2, 3]
    print(nums[-1])
    """
    dict = {"Jan": 1, "Feb": 2}
