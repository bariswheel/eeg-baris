import requests
import os

def download_file(session, url, save_path):
    """Downloads a file from a URL into the specified local path."""
    print(f"Attempting to download from URL: {url}")  # Logging URL attempt
    response = session.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download {url}, Status Code: {response.status_code}")
        print(response.text)  # Logging the response body for more context on the error

def main(session_id, file_urls, local_storage_path):
    """Main function to handle downloading files directly."""
    session = requests.Session()
    session.headers.update({
        'Cookie': f'session_id={session_id}',  # Ensure this is the correct way to authenticate
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    })

    for url in file_urls:
        local_file_path = os.path.join(local_storage_path, os.path.basename(url))
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        download_file(session, url, local_file_path)

if __name__ == "__main__":
    SESSION_ID = 'LPfc9aZz2pTkYtM0t3U2fR1_Yx58V0mH6'
    FILE_URLS = [
        'https://cloud.bcmi.sjtu.edu.cn/fsdownload/webapi/file_download.cgi/SEED_EEG.zip',
        'https://cloud.bcmi.sjtu.edu.cn/fsdownload/webapi/file_download.cgi/SEED.zip'
    ]
    LOCAL_STORAGE_PATH = '/Users/baris/Downloads/SEED'

    main(SESSION_ID, FILE_URLS, LOCAL_STORAGE_PATH)
