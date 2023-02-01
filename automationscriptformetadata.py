import pandas as pd
import os


def extract_features_metadata(filepath):
    # Extract features from file (assume this is done using some external library or method)
    features = extract_features(filepath)

    # Extract metadata from file (assume this is done using some external library or method)
    metadata = extract_metadata(filepath)

    # Create a dictionary with the extracted features and metadata
    data = {"features": features, "metadata": metadata}

    # Return the data
    return data


# Function to inspect the extracted data
def inspect_data(data):
    # Print the extracted features and metadata
    print("Features: ", data["features"])
    print("Metadata: ", data["metadata"])


# Function to automate the process
def automate_process(folderpath):
    # Iterate through all files in the folder
    for filename in os.listdir(folderpath):
        # Create the filepath by joining the folder path and the filename
        filepath = os.path.join(folderpath, filename)

        # Extract the features and metadata
        data = extract_features_metadata(filepath)

        # Inspect the extracted data
        inspect_data(data)


# Example usage:
automate_process("path/to/folder")
