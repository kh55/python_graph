import numpy as np
import matplotlib.pyplot as plt

data_set = np.loadtxt(
    fname="./import/application_h.csv", #読み込むファイルのパスと名前
    dtype="int", #floatで読み込む
    delimiter=",", #csvなのでカンマで区切る
)

for data in data_set:
    plt.scatter(data[1], data[0])

plt.savefig("./output/sin.png", format="png", dpi=300)