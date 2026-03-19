import os
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd

def download_dataset():
    """Download the ecommerce dataset using kagglehub."""
    
    # Define paths
    data_folder = "data"
    os.makedirs(data_folder, exist_ok=True)
    
    # Dataset configuration
    dataset_name = "mkechinov/ecommerce-behavior-data-from-multi-category-store"
    file_name = "2019-Nov.csv"
    output_path = os.path.join(data_folder, file_name)
    
    print(f"Downloading {file_name} from {dataset_name}...")
    
    try:
        # Download dataset
        df: pd.DataFrame = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            dataset_name,
            file_name
        )
        
        print(f"Dataset loaded successfully with {len(df):,} rows and {len(df.columns)} columns")
        print(f"Columns: {list(df.columns)}")
        
        # Save to CSV
        df.to_csv(output_path, index=False)
        print(f"Dataset saved to {output_path}")
        
        # Save dataset information
        info_path = os.path.join(data_folder, "dataset_info.txt")
        with open(info_path, "w") as f:
            f.write(f"Dataset: {dataset_name}\n")
            f.write(f"File: {file_name}\n")
            f.write(f"Rows: {len(df):,}\n")
            f.write(f"Columns: {len(df.columns)}\n")
            f.write(f"Column names: {', '.join(df.columns.tolist())}\n")
            f.write(f"\nData types:\n{df.dtypes.to_string()}\n")
        
        print(f"Dataset information saved to {info_path}")
        
    except Exception as e:
        print(f"Error downloading dataset: {e}")

if __name__ == "__main__":
    download_dataset()