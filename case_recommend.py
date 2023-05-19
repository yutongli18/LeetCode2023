import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    fontDict = {"family": "Times New Roman", "weight": "light"}
    fontProp = {"family": "Times New Roman", "weight": "normal"}
    data = [[19.25, 24.63, 27.55, 31.67],
            [37.14, 48.26, 53.74, 72.88],
            [30.53, 42.14, 56.61, 71.86],
            [45.62, 56.93, 70.24, 81.35]]
    index = ["Description\nMatch", "ES", "Word2Vec Entity\nRepresentation", "eRCA"]
    columns = ["k=1", "k=3", "k=5", "k=10"]
    data = pd.DataFrame(data, columns=columns, index=index)
    fig, ax = plt.subplots()
    data.plot.barh(ax=ax, alpha=0.7)
    # plt.xlabel("p@k", fontdict=fontDict)
    # plt.ylabel("$algorithm$")
    # plt.xticks(range(0, 100, 10), fontdict=fontDict)
    # plt.yticks(range(len(index)), index, fontdict=fontDict)
    ax.set_xlabel("p@k", fontdict=fontDict)
    ax.set_xticks(range(0, 100, 10))
    ax.set_xticklabels(range(0, 100, 10), fontdict=fontDict)
    ax.set_yticklabels(index, fontdict=fontDict)

    for x, y1 in enumerate(data["k=1"]):
        plt.text(y1, x - 0.25, "%s" % y1, fontdict=fontDict)
    for x, y2 in enumerate(data["k=3"]):
        plt.text(y2, x - 0.1, "%s" % y2, fontdict=fontDict)
    for x, y3 in enumerate(data["k=5"]):
        plt.text(y3, x + 0.02, "%s" % y3, fontdict=fontDict)
    for x, y4 in enumerate(data["k=10"]):
        plt.text(y4, x + 0.15, "%s" % y4, fontdict=fontDict)

    lines, labels = ax.get_legend_handles_labels()
    plt.legend(prop=fontProp)

    plt.savefig(r"D:\LeetCode\case_recommend.jpg", bbox_inches="tight")
    # plt.show()
