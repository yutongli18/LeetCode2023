from pathlib import Path
import matplotlib as mpt
import matplotlib.pyplot as plt
import pandas as pd


fontDict = dict(family='Times New Roman', weight='light')
fontDictProp = dict(family='Times New Roman', weight='normal')


def plotSubgraph(prData, f1Data, ax, xlabel):
    # 画一个子图
    prData = pd.DataFrame(prData, index=["TF-IDF", "TextRank", "YAKE", "Our Model"], columns=["Precision", "Recall"])
    f1Data = pd.Series(f1Data, index=["TF-IDF", "TextRank", "YAKE", "COM-KG"])
    params = {"yticks": range(0, 120, 20),
              "alpha": 0.7}

    prData.plot.bar(ax=ax, **params, label=prData.columns.values)
    f1Data.plot(ax=ax, **params, style="ro--", label="$F_1$")
    ax.set_xlabel(xlabel, fontdict=fontDict)
    ax.set_ylabel(r"P/R(%)", fontdict=fontDict)
    ax.set_xticklabels(prData.index.values, fontdict=fontDict)
    ax.set_yticklabels(range(0, 120, 20), fontdict=fontDict)
    ax.get_legend().remove()

    f1Index = f1Data.index.values
    for i in range(len(f1Index)):
        ax.text(i-0.2, f1Data[f1Index[i]]+0.5, "%s" % f1Data[f1Index[i]], fontdict=fontDict)


if __name__ == '__main__':
    # k=1
    prData_k1 = [[51, 49],
                 [49, 29],
                 [52, 42],
                 [58, 48]]
    f1Data_k1 = [49.98, 36.43, 46.47, 52.52]
    # k=3
    prData_k3 = [[58, 56],
                 [56, 36],
                 [54, 50],
                 [62, 52]]
    f1Data_k3 = [56, 44.21, 51.24, 56.35]
    # k=5
    prData_k5 = [[64, 63],
                 [62, 46],
                 [70, 64],
                 [76, 63]]
    f1Data_k5 = [63.84, 51.93, 66.63, 70.14]
    # k=8
    prData_k8 = [[60, 64],
                 [58, 44],
                 [57, 52],
                 [64, 70]]
    f1Data_k8 = [61.37, 50.27, 55.04, 67.31]
    # 定义子图
    fig, axes = plt.subplots(2, 2)
    # 绘制子图
    plotSubgraph(prData_k1, f1Data_k1, axes[0, 0], r"(a)k=1")
    plotSubgraph(prData_k3, f1Data_k3, axes[0, 1], r"(b)k=3")
    plotSubgraph(prData_k5, f1Data_k5, axes[1, 0], r"(c)k=5")
    plotSubgraph(prData_k8, f1Data_k8, axes[1, 1], r"(d)k=8")
    # 标签放在正中
    lines, labels = fig.axes[0].get_legend_handles_labels()
    fig.legend(lines, labels, loc="upper center", bbox_to_anchor=(0.5, 1.05), ncol=3, prop=fontDictProp)
    # fig.subplots_adjust(top=2.0)
    fig.tight_layout()
    plt.savefig(r"D:\LeetCode\keyword_extraction.jpg", bbox_inches="tight")
    plt.show()
