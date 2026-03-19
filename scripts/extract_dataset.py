import os
import zipfile
import pandas as pd
import shutil
from dotenv import load_dotenv

load_dotenv()

def extract_dataset():
    """Extract the dataset if it's a ZIP file and move to proper location."""
    
    file_path = os.getenv("FILE_PATH")

    if not file_path:
        print("Error: FILE_PATH not found in .env file")
        print("Please create a .env file with: FILE_PATH = dataset_path")
        return

    source_file = file_path
    data_folder = "data"
    extract_folder = os.path.join(data_folder, "extracted")
    processed_folder = os.path.join(data_folder, "processed")
    
    # Create necessary folders
    os.makedirs(extract_folder, exist_ok=True)
    os.makedirs(processed_folder, exist_ok=True)
    
    if not os.path.exists(source_file):
        print(f"Source file not found: {source_file}")
        print("Please run download_dataset.py first.")
        return
    
    file_size_gb = os.path.getsize(source_file) / (1024**3)
    print(f"Source file: {source_file}")
    print(f"File size: {file_size_gb:.2f} GB")
    
    # Check if file is ZIP
    with open(source_file, 'rb') as f:
        header = f.read(4)
        
    if header.startswith(b'PK'):
        print("File is a ZIP archive. Extracting...")
        
        # Extract the ZIP file
        with zipfile.ZipFile(source_file, 'r') as zip_ref:
            zip_ref.extractall(extract_folder)
            print(f"Extracted to: {extract_folder}")
            
            # Find and verify CSV files
            csv_files = []
            for root, dirs, files in os.walk(extract_folder):
                for file in files:
                    if file.endswith('.csv'):
                        csv_path = os.path.join(root, file)
                        csv_files.append((file, csv_path))
            
            if csv_files:
                print(f"\nFound {len(csv_files)} CSV file(s):")
                for name, path in csv_files:
                    size_mb = os.path.getsize(path) / (1024**2)
                    print(f"  - {name} ({size_mb:.1f} MB)")
                    
                    # Verify CSV can be read
                    try:
                        df_test = pd.read_csv(path, nrows=5)
                        print(f"    Verified")
                        print(f"    Columns: {list(df_test.columns)}")
                    except Exception as e:
                        print(f"    Error reading: {e}")
            else:
                print("No CSV files found in the archive")
    else:
        print("File is not a ZIP archive. Copying directly...")
        destination = os.path.join(extract_folder, "2019-Nov.csv")
        shutil.copy2(source_file, destination)
        print(f"Copied to: {destination}")

if __name__ == "__main__":
    extract_dataset()