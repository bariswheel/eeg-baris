import os
import requests

def download_file(session, url, local_path):
    if not os.path.exists(local_path):
        with session.get(url, stream=True) as response:
            response.raise_for_status()
            with open(local_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
        print(f"Downloaded {local_path} successfully.")
    else:
        print(f"Already exists, skipping: {local_path}")

def list_files(session, api_url):
    response = session.get(api_url)
    response.raise_for_status()
    return response.json()  # Assuming the API returns a JSON list of file paths

def setup_session(session_id, proxy_dict=None):
    session = requests.Session()
    session.headers.update({'Authorization': f'Bearer {session_id}'})
    if proxy_dict:
        session.proxies.update(proxy_dict)
    return session

def main(session_id, base_url, directory_endpoint, local_storage_path, proxy_dict=None):
    session = setup_session(session_id, proxy_dict)
    file_list_url = f"{base_url}{directory_endpoint}"
    file_infos = list_files(session, file_list_url)
    
    for file_info in file_infos:
        file_url = f"{base_url}/{file_info['path']}"
        local_path = os.path.join(local_storage_path, file_info['name'])
        download_file(session, file_url, local_path)

if __name__ == "__main__":
    SESSION_ID = 'LPfc9aZz2pTkYtM0t3U2fR1_Yx58V0mH6'  # Replace with your actual session ID
    BASE_URL = 'https://cloud.bcmi.sjtu.edu.cn/sharing/R80Mk1n2v'
    DIRECTORY_ENDPOINT = '/api/files'  # Adjust as per actual API endpoint that lists files
    LOCAL_STORAGE_PATH = '/path/to/your/local/directory'
    PROXY_DICT = {
        'http': 'http://10.10.1.10:3128',
        'https': 'http://10.10.1.10:1080'
    }

    main(SESSION_ID, BASE_URL, DIRECTORY_ENDPOINT, LOCAL_STORAGE_PATH, PROXY_DICT)
