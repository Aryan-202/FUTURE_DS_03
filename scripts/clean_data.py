import pandas as pd
import os

# Paths
INPUT_PATH = "data/extracted/2019-Nov.csv"
OUTPUT_PATH = "data/cleaned_data.csv"
CHUNK_SIZE = 500000

def clean_data():
    if not os.path.exists(INPUT_PATH):
        print(f"Error: Input file not found at {INPUT_PATH}")
        return

    print(f"Cleaning dataset: {INPUT_PATH}")
    print(f"Output will be saved to: {OUTPUT_PATH}")

    # To write the header for the first chunk only
    first_chunk = True

    chunk_count = 0
    total_cleaned_rows = 0

    # Ensure data folder exists
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    for chunk in pd.read_csv(INPUT_PATH, chunksize=CHUNK_SIZE):
        chunk_count += 1
        
        # 1. Drop rows with missing essential identifiers
        # In behavior data, user_id and user_session are critical for funnel.
        chunk = chunk.dropna(subset=['user_id', 'user_session'])
        
        # 2. Clean price: Filter out obvious errors (negative prices)
        chunk = chunk[chunk['price'] >= 0]
        
        # 3. Handle missing values for brand and category_code
        chunk['brand'] = chunk['brand'].fillna('unknown')
        chunk['category_code'] = chunk['category_code'].fillna('unknown')
        
        # 4. Remove duplicate events occurring at the exact same second for the same user-product interaction
        # This can happen if a page refreshes or double clicks.
        before_dedup = len(chunk)
        chunk = chunk.drop_duplicates(subset=['event_time', 'event_type', 'product_id', 'user_id', 'user_session'])
        
        # 5. Convert event_time to datetime formatting consistency
        try:
            chunk['event_time'] = pd.to_datetime(chunk['event_time']).dt.strftime('%Y-%m-%d %H:%M:%S UTC')
        except Exception as e:
            # If conversion fails, keep original or handle errors
            pass

        # Write chunk to CSV
        mode = 'w' if first_chunk else 'a'
        header = True if first_chunk else False
        chunk.to_csv(OUTPUT_PATH, index=False, mode=mode, header=header)
        
        total_cleaned_rows += len(chunk)
        first_chunk = False
        
        print(f"  Processed Chunk {chunk_count}... Total cleaned rows: {total_cleaned_rows:,}", end='\r')

    print(f"\nCleaning complete. Total rows preserved: {total_cleaned_rows:,}")
    print(f"Saved to {OUTPUT_PATH}")

if __name__ == "__main__":
    clean_data()
