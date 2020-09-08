import pandas as pd
import os
import matplotlib.pyplot as plt

phone_list = []
root_dir = r"C:\Users\xilig\Desktop"
for parent, dir_names, file_names in os.walk(root_dir):
    for filename in file_names:
        phone_list.append(os.path.basename(parent))
pd.Series(list(set(phone_list))).to_csv('3.txt', index=None)
print(pd.datetime(2016, 12, 12))
plt.plot([1, 2, 3, 4, 5])
plt.show()
