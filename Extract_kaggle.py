import os
import kaggle
from kaggle.api.kaggle_api_extended import KaggleApi

def download_dataset(dataset_name, output_path='.'):
    """
    Download a dataset from Kaggle and save it to the specified output path.
    
    Args:
        dataset_name (str): The dataset identifier in the format 'username/dataset-name'
        output_path (str): The directory where the dataset will be saved
    """
    try:
        # Initialize the Kaggle API
        api = KaggleApi()
        api.authenticate()
        
        # Create output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)
        
        # Download the dataset
        print(f"Downloading dataset: {dataset_name}")
        api.dataset_download_files(dataset_name, path=output_path, unzip=True)
        print(f"Dataset downloaded successfully to {output_path}")
        
    except Exception as e:
        print(f"Error downloading dataset: {str(e)}")

if __name__ == "__main__":
    # Example usage
    dataset_name = "tsr564/goldpriceindianmarket"  # Replace with your desired dataset
    download_dataset(dataset_name)
