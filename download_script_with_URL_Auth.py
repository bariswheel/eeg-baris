import requests
from requests.auth import HTTPBasicAuth
from urllib.parse import urljoin

def download_file(url, username, password, save_path):
    with requests.Session() as session:
        session.auth = HTTPBasicAuth(username, password)
        response = session.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"Downloaded {save_path} successfully.")
        else:
            print(f"Failed to download {url}. Status code: {response.status_code}")

if __name__ == "__main__":
    url = "https://cloud.bcmi.sjtu.edu.cn/sharing/R80Mk1n2v"
    username = ""  # Not needed for basic authentication
    password = "sjtubcmi"
    save_path = "/path/to/save/files/"

    # Replace with actual file names or iterate over a list of files to download
    file_names = ["file1.txt", "file2.txt"]

    for file_name in file_names:
        file_url = urljoin(url, file_name)
        local_path = os.path.join(save_path, file_name)
        download_file(file_url, username, password, local_path)
