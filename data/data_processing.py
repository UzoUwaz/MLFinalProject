import os
import requests
import pandas as pd

# Step 1: Download raw files
city_files = {
    'Asheville': {
        'listings': 'https://data.insideairbnb.com/united-states/nc/asheville/2025-03-13/data/listings.csv.gz',
        'reviews':  'https://data.insideairbnb.com/united-states/nc/asheville/2025-03-13/data/reviews.csv.gz',
    },
    'Boston': {
        'listings': 'https://data.insideairbnb.com/united-states/ma/boston/2025-03-15/data/listings.csv.gz',
        'reviews':  'https://data.insideairbnb.com/united-states/ma/boston/2025-03-15/data/reviews.csv.gz',
    },
    'Chicago': {
        'listings': 'https://data.insideairbnb.com/united-states/il/chicago/2025-03-11/data/listings.csv.gz',
        'reviews':  'https://data.insideairbnb.com/united-states/il/chicago/2025-03-11/data/reviews.csv.gz',
    }
}

print("Downloading files...")
for city, files in city_files.items():
    city_dir = os.path.join("raw", city)
    os.makedirs(city_dir, exist_ok=True)

    for file_type, url in files.items():
        file_name = f"{file_type}.csv.gz"
        file_path = os.path.join(city_dir, file_name)

        print(f"Downloading {file_type} for {city}...")
        response = requests.get(url)
        if response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(response.content)
            print(f"Saved to: {file_path}")
        else:
            print(f"Failed to download {url}")

# Step 2: Clean the downloaded files
print("\nCleaning data...")

raw_dir = "raw"
clean_dir = "clean"
cities = ['Asheville', 'Boston', 'Chicago']

target_columns = [
    'name', 'description', 'property_type', 'price',
    'neighbourhood_cleansed', 'neighbourhood_group_cleansed', 'latitude',
    'longitude', 'host_since', 'host_response_time', 'host_response_rate',
    'host_acceptance_rate', 'host_is_superhost', 'host_listings_count',
    'host_total_listings_count', 'host_verifications',
    'host_has_profile_pic', 'host_identity_verified',
    'calculated_host_listings_count',
    'calculated_host_listings_count_entire_homes',
    'calculated_host_listings_count_private_rooms',
    'calculated_host_listings_count_shared_rooms', 'room_type',
    'accommodates', 'bathrooms', 'bathrooms_text', 'bedrooms', 'beds',
    'amenities', 'has_availability', 'availability_30', 'availability_60',
    'availability_90', 'availability_365', 'instant_bookable',
    'minimum_nights', 'maximum_nights', 'number_of_reviews',
    'number_of_reviews_ltm', 'number_of_reviews_l30d', 'first_review',
    'last_review', 'review_scores_rating', 'review_scores_accuracy',
    'review_scores_cleanliness', 'review_scores_checkin',
    'review_scores_communication', 'review_scores_location',
    'review_scores_value', 'reviews_per_month', 'reviews'
]

os.makedirs(clean_dir, exist_ok=True)

for city in cities:
    input_path = os.path.join(raw_dir, city, "listings.csv.gz")
    review_path = os.path.join(raw_dir, city, "reviews.csv.gz")
    output_path = os.path.join(clean_dir, f"{city}_listings_cleaned.csv")

    try:
        df = pd.read_csv(input_path, compression='gzip')
        available_columns = [col for col in target_columns if col in df.columns]
        df_selected = df[available_columns].copy()

        if 'id' not in df_selected.columns and 'id' in df.columns:
            df_selected['id'] = df['id']

        for col in ['host_is_superhost', 'host_has_profile_pic', 'host_identity_verified', 'has_availability', 'instant_bookable']:
            if col in df_selected.columns:
                df_selected[col] = df_selected[col].replace({'t': 'TRUE', 'f': 'FALSE'})

        if os.path.exists(review_path):
            reviews_df = pd.read_csv(review_path, compression='gzip', usecols=['listing_id', 'comments'])
            reviews_df = reviews_df.dropna(subset=['comments'])
            reviews_df['comments'] = reviews_df['comments'].astype(str).str.replace('\n', ' ').str.replace('\r', ' ').str.replace('<br>', ' ').str.strip()
            grouped_reviews = reviews_df.groupby('listing_id').first().reset_index()[['listing_id', 'comments']]
            grouped_reviews.rename(columns={'comments': 'reviews'}, inplace=True)
            df_selected['id'] = df_selected['id'].astype(int)
            grouped_reviews['listing_id'] = grouped_reviews['listing_id'].astype(int)
            df_selected = df_selected.merge(grouped_reviews, left_on='id', right_on='listing_id', how='left')
            df_selected['reviews'] = df_selected['reviews'].fillna('No reviews')
            if 'listing_id' in df_selected.columns:
                df_selected.drop(columns=['listing_id'], inplace=True)
        else:
            df_selected['reviews'] = "No reviews"

        if 'id' in df_selected.columns:
            df_selected.drop(columns=['id'], inplace=True)

        if 'price' in df_selected.columns:
            df_selected['price'] = (
                df_selected['price']
                .astype(str)
                .str.replace(r'[\$,]', '', regex=True)
                .astype(float)
            )
            price_mean = df_selected['price'].mean()
            df_selected['price'] = df_selected['price'].fillna(price_mean)
            df_selected['price'] = pd.qcut(df_selected['price'], q=6, labels=False, duplicates='drop')

        df_selected.to_csv(output_path, index=False)
        print(f"Cleaned and saved to: {output_path}")

    except Exception as e:
        print(f"Error processing {city}: {e}")