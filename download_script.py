import os
import requests

def download_file(session, url, local_path):
    if not os.path.exists(local_path):
        with session.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded: {local_path}")
    else:
        print(f"Already exists, skipping: {local_path}")

def download_dataset(base_url, session_id, proxy_dict=None):
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {session_id}'})
    if proxy_dict:
        session.proxies.update(proxy_dict)

    # Fetch directory structure (assuming JSON response with a list of file paths)
    response = session.get(f"{base_url}/directory")
    response.raise_for_status()
    files = response.json()['files']

    for file_info in files:
        file_url = f"{base_url}/{file_info['path']}"
        local_path = os.path.join('path_to_save_files', file_info['name'])
        download_file(session, file_url, local_path)

if __name__ == "__main__":
    # These values should be customized based on your specific situation
    BASE_URL = 'https://example.com/api'
    SESSION_ID = input("Enter session ID: ")
    PROXY_DICT = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080',
    }

    download_dataset(BASE_URL, SESSION_ID, PROXY_DICT)
