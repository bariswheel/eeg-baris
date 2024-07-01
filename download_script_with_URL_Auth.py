import requests
import os

def download_file(session, url, save_path):
    """Downloads a file from a URL into the specified local path."""
    response = session.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded: {save_path}")
    else:
        print(f"Failed to download {url}, Status Code: {response.status_code}")

def list_directory_contents(session, url):
    """Lists the contents of a directory via an API call."""
    response = session.get(url)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns a list of items in JSON format
    else:
        print("Failed to fetch directory contents")
        return []

def main(session_id, base_url, directories, local_storage_path):
    """Main function to handle downloading directories."""
    session = requests.Session()
    session.headers.update({'Cookie': f'session_id={session_id}'})  # Authentication via session ID

    for directory in directories:
        directory_url = f"{base_url}/{directory}"  # Adjust this URL based on actual API structure
        contents = list_directory_contents(session, directory_url)
        directory_path = os.path.join(local_storage_path, directory)
        os.makedirs(directory_path, exist_ok=True)

        for item in contents:
            if item['type'] == 'file':  # Assuming the API response includes a type attribute
                file_url = f"{base_url}/{item['path']}"
                local_file_path = os.path.join(directory_path, item['name'])
                download_file(session, file_url, local_file_path)

if __name__ == "__main__":
    SESSION_ID = 'LPfc9aZz2pTkYtM0t3U2fR1_Yx58V0mH6'
    BASE_URL = 'https://cloud.bcmi.sjtu.edu.cn/sharing/R80Mk1n2v'
    DIRECTORIES = ['SEED_EEG', 'SEED_Multimodal']
    LOCAL_STORAGE_PATH = '/Users/baris/Downloads/SEED'

    main(SESSION_ID, BASE_URL, DIRECTORIES, LOCAL_STORAGE_PATH)
