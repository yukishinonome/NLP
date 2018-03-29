import time
import numpy as np


a = time.time()
w_list = ["りんご", "ぶどう", "なし", "いちご", "れもん", "みかん"]
w_list = np.sort(w_list)
print(w_list)
print(time.time() - a)


b = time.time()
s_list = ["りんご", "ぶどう", "なし", "いちご", "れもん", "みかん"]
s_list.sort()
print(s_list)
print(time.time() - b)


c = time.time()
s2_list = ["りんご", "ぶどう", "なし", "いちご", "れもん", "みかん"]
s2_list = sorted(s2_list)
print(s2_list)
print(time.time() - c)


# ３種類のソートをした時の実行時間