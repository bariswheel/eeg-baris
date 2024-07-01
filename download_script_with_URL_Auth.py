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

def list_directory_contents(session, url):
    """Lists the contents of a directory via an API call."""
    print(f"Fetching directory contents from URL: {url}")  # Logging URL access attempt
    response = session.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns a list of items in JSON format
    else:
        print("Failed to fetch directory contents")
        print(f"Status Code: {response.status_code}")  # Log the status code
        print(response.text)  # Log the response body for more context on the error
        return []

def main(session_id, base_url, file_paths, local_storage_path):
    """Main function to handle downloading files directly."""
    session = requests.Session()
    session.headers.update({'Cookie': f'session_id={session_id}'})  # Authentication via session ID

    for file_path in file_paths:
        full_url = f"{base_url}/{file_path}"  # Construct the full URL to the file
        local_file_path = os.path.join(local_storage_path, os.path.basename(file_path))
        os.makedirs(os.path.dirname(local_file_path), exist_ok=True)
        download_file(session, full_url, local_file_path)

if __name__ == "__main__":
    SESSION_ID = 'LPfc9aZz2pTkYtM0t3U2fR1_Yx58V0mH6'
    BASE_URL = 'https://cloud.bcmi.sjtu.edu.cn/sharing/R80Mk1n2v'
    FILE_PATHS = ['SEED_EEG/SEED_EEG.zip', 'SEED_Multimodal/SEED.zip']  # Direct paths to the files
    LOCAL_STORAGE_PATH = '/Users/baris/Downloads/SEED'

    main(SESSION_ID, BASE_URL, FILE_PATHS, LOCAL_STORAGE_PATH)
