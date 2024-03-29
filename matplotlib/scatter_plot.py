
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('ggplot')

data = pd.read_csv('data_IV.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes, 
            c=ratio,
            cmap="summer",
            edgecolors="black",
            linewidths=1, alpha=0.75)

cbar = plt.colorbar()
cbar.set_label("Like/Dislike Ratio")

plt.xscale("log")
plt.yscale("log")

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()