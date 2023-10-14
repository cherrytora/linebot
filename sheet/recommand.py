import pandas as pd
import numpy as np


dis = pd.read_excel("data/醫療路線距離.xlsx")


def recommand(txt):
    r_stores = dis.loc[(dis["商店1"] == txt) & (dis["距離(公尺)"] <= 300)]
    if len(r_stores) >= 3:
        idx = np.random.choice(r_stores.index, 3, False)
        recommand_list = r_stores.loc[idx, "商店2"].values
    else:
        l = len(r_stores)
        idx = np.random.choice(r_stores.index, l, False)
        recommand_list = r_stores.loc[idx, "商店2"].values

    return recommand_list
