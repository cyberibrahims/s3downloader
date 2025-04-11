import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote
import sys

def download_file(url, local_path):
    """Download a single file from S3 URL to local path."""
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(local_path), exist_ok=True)
        
        # Download the file
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Downloaded: {local_path}")
        return True
    except Exception as e:
        print(f"Error downloading {url}: {str(e)}")
        return False

def list_bucket_contents(bucket_url):
    """List all files in the S3 bucket recursively."""
    try:
        response = requests.get(bucket_url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'xml')
        
        # Get all Contents elements (files)
        contents = soup.find_all('Contents')
        
        files = []
        for content in contents:
            key = content.find('Key')
            if key:
                files.append(key.text)
        
        return files
    except Exception as e:
        print(f"Error listing bucket contents: {str(e)}")
        return []

def download_bucket(bucket_url):
    """Download all files from the S3 bucket recursively."""
    # Parse bucket name from URL
    parsed_url = urlparse(bucket_url)
    bucket_name = parsed_url.netloc.split('.')[0]
    
    # Create downloads directory with bucket name
    base_download_dir = os.path.join('downloads', bucket_name)
    os.makedirs(base_download_dir, exist_ok=True)
    
    # List all files in bucket
    files = list_bucket_contents(bucket_url)
    
    # Download each file
    for file_key in files:
        # Decode URL-encoded characters in the file key
        decoded_key = unquote(file_key)
        
        # Construct full URL for the file
        file_url = f"{bucket_url}/{file_key}"
        
        # Construct local path
        local_path = os.path.join(base_download_dir, decoded_key)
        
        # Download the file
        download_file(file_url, local_path)

def main():
    if len(sys.argv) != 2:
        print("Usage: python s3_downloader.py <s3-bucket-url>")
        print("Example: python s3_downloader.py https://my-bucket.s3.amazonaws.com")
        sys.exit(1)
    
    bucket_url = sys.argv[1].rstrip('/')
    download_bucket(bucket_url)

if __name__ == "__main__":
    main()
