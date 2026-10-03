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
# print(type_count)

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

#  rating distribution
rating_counts = df['rating'].value_counts()
# print(rating_counts)

plt.figure(figsize=(8,6))
#  pie chart
plt.pie(rating_counts, labels=rating_counts.index , autopct='%1.1f%%' , startangle=90)
plt.title('Percentage of content rating')
plt.tight_layout()
plt.savefig('content_rating.png')
plt.show()


#  movie duration split histogram

movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace(' min', '').astype(int)

plt.figure(figsize=(8, 6))
plt.hist(
    movie_df['duration_int'],
    bins=30,
    color='purple',
    edgecolor='black'
)

plt.title('Distribution of Movie Duration')
plt.xlabel('Duration (minutes)')
plt.ylabel('Number of Movies')

plt.tight_layout()

plt.savefig('movie_duration_histogram.png')

plt.show()