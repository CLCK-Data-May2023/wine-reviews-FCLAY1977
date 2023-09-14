import pandas as pd

# Read the CSV data
data = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Group data by 'country' and calculate the number of reviews and average points for each country
summary = data.groupby('country').agg({'points': 'mean', 'title': 'count'}).reset_index()

# Rename columns for clarity
summary.rename(columns={'title': 'number_of_reviews', 'points': 'average_points'}, inplace=True)

# Write the summary data to a new CSV file
summary.to_csv('data/reviews-per-country.csv', index=False)

print("Summary data written to 'reviews-per-country.csv'")




