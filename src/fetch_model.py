import requests
import os
import configparser


def download_latest_joblib(org_name, repo_name, file_name, download_dir):
    # Create directory if it doesn't exist
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Construct the URL for the latest release assets
    url = f"https://api.github.com/repos/{org_name}/{repo_name}/releases/latest"

    # Send a GET request to the GitHub API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the download URL of the asset
        download_url = response.json()["assets_url"]

        # Send a GET request to the assets URL
        response = requests.get(download_url)

        # Check if the request was successful
        if response.status_code == 200:
            # Find the .joblib file among the assets
            assets = response.json()
            joblib_url = None
            for asset in assets:
                if file_name in asset["name"]:
                    joblib_url = asset["browser_download_url"]
                    break

            # Download the .joblib file
            if joblib_url:
                response = requests.get(joblib_url)
                if response.status_code == 200:
                    # Save the .joblib file
                    with open(os.path.join(download_dir, file_name), 'wb') as f:
                        f.write(response.content)
                    print(f"File {file_name} downloaded successfully.")
                else:
                    print("Failed to download .joblib file.")
            else:
                print(f"No {file_name} found among the assets.")
        else:
            print("Failed to fetch assets.")
    else:
        print("Failed to fetch latest release.")


# Read parameters from config file
def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    org_name = config.get('GitHub', 'org_name')
    repo_name = config.get('GitHub', 'repo_name')
    file_name = config.get('GitHub', 'file_name')
    download_dir = config.get('Directories', 'download_dir')
    return org_name, repo_name, file_name, download_dir


def main():
    config_file = 'config.ini'
    org_name, repo_name, file_name, download_dir = read_config(config_file)
    download_latest_joblib(org_name, repo_name, file_name, download_dir)


if __name__ == "__main__":
    main()