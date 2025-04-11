# S3 Public Bucket Downloader

A Python script that recursively downloads all files from a public S3 bucket while maintaining the original directory structure.

## Features

- Downloads all files from a public S3 bucket recursively
- Maintains original folder structure
- Creates organized downloads directory with bucket name
- Handles URL-encoded file names
- Provides download progress feedback
- Error handling and reporting

## Requirements

- Python 3.x
- Required packages (automatically installed via requirements.txt):
  - requests>=2.31.0
  - beautifulsoup4>=4.12.2
  - lxml>=4.9.3

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cyberibrahims/s3downloader.git
cd s3-downloader
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script with a public S3 bucket URL as an argument:

```bash
python s3_downloader.py <s3-bucket-url>
```

Example:
```bash
python s3_downloader.py https://my-bucket.s3.amazonaws.com
```

The script will:
1. Create a `downloads/my-bucket` directory
2. Download all files from the bucket
3. Preserve the original folder structure
4. Show progress for each downloaded file

## Output Structure

```
downloads/
└── my-bucket/
    ├── file1.txt
    ├── folder1/
    │   ├── file2.txt
    │   └── file3.txt
    └── folder2/
        └── file4.txt
```

## Error Handling

The script includes error handling for:
- Invalid URLs
- Network connection issues
- File system errors
- Permission issues

Errors are reported to the console with detailed messages.

## Limitations

- Only works with public S3 buckets
- Requires proper read permissions on the bucket
- Network bandwidth and storage space dependent

## License

MIT License - feel free to use and modify as needed.
