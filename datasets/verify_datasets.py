from os import path

import requests

SUSCEPTIBILITY_MATRIX_URL = (
    "https://raw.githubusercontent.com/ama-yash/dataset/main/recovery_matrix.csv"
)
RECOVERY_MATRIX_URL = (
    "https://raw.githubusercontent.com/ama-yash/dataset/main/susceptibility_matrix2.csv"
)

DATASETS = [SUSCEPTIBILITY_MATRIX_URL, RECOVERY_MATRIX_URL]


def dataset_exits(dataset_name):
    if path.exists(dataset_name):
        return True
    elif path.exists("datasets/" + dataset_name):
        return True
    return False


def download_datasets():
    for dataset in DATASETS:
        dataset_name = dataset.split("/")[-1]
        if not dataset_exits(dataset_name):
            response = requests.get(dataset)
            if response.status_code == 200:
                # Open file and write the content
                print("Downloading file: " + dataset_name + "...")
                with open("datasets/" + dataset_name, "wb") as file:
                    # A chunk of 128 bytes
                    for chunk in response:
                        file.write(chunk)
            else:
                print("Error, cannot download " + dataset_name)
                print("Response code: " + response.status_code)
        else:
            print("File " + dataset_name + " exists ✅")
