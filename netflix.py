import pandas as pd
import matplotlib.pyplot as plt

# load the data
df = pd.read_csv(r'D:\MACHINE LEARNING\matplotlib\netflix project\netflix_titles.csv')
# print(df.head())


# clean the data
df = df.dropna(
    subset=['type', 'release_year', 'rating', 'country', 'duration']
)


#  movies vs tv shows
type_count = df['type'].value_counts()
print(type_count)

#  creates the area for figure
plt.figure(figsize=(6, 4))

# bar chart
plt.bar(type_count.index , type_count.values , color=['skyblue', 'orange'])
plt.title('Number of Movies VS TV Shows on Netflix')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('movies_vs_tvshows.png')
plt.show()



