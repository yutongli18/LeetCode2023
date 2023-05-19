from pathlib import Path
import matplotlib as mpt
import matplotlib.pyplot as plt
import pandas as pd


data = [[0.47, 0.09],
        [0.61, 0.21],
        [0.76, 0.22],
        [0.79, 0.3]]
index = ["1", "3", "5", "8"]
data = pd.DataFrame(data, columns=["$Acc$", r"$P_\varepsilon$"], index=index)
params = {"style": "o--", "xlabel": "$k$", "ylabel": r"$Acc$/$P_\varepsilon$",
          "xticks": range(len(index))}

# fig, ax = plt.subplots()
# fontPath = Path(mpt.get_data_path(), r"D:\LeetCode\times.ttf")
# ax.set_xticklabels(index, font=fontPath)
# ax.set_yticklabels()
data.plot(**params)

acc_rate = data["$Acc$"]
err_rate = data[r"$P_\varepsilon$"]
for i in range(len(index)):
        plt.text(i - 0.05, acc_rate[index[i]] + 0.01, "%s" % acc_rate[index[i]], font=fontPath)
        plt.text(i - 0.05, err_rate[index[i]] + 0.01, "%s" % err_rate[index[i]], font=fontPath)
plt.savefig(r"D:\LeetCode\root_cause_analysis.jpg")
