import requests
import os
from bs4 import BeautifulSoup

def process_svg_elements(svgs, titles, folder_path):
    # Loop through each svg and title
    for i in range(len(svgs)):
        current_svg = svgs[i]

        # Your code to process each SVG element goes here
        print(f"Processing SVG {i + 1}...")

        # Create SVG file in the specified folder
        title = titles[i]
        file_name = f"{title.text}.svg"
        file_path = os.path.join(folder_path, file_name)

        try:
            with open(file_path, 'w', encoding='utf-8') as svg_file:
                svg_file.write(str(current_svg))
            print(f"SVG {i + 1} saved to {file_path}")

        except FileNotFoundError as e:
            print(f"Error: {e}")
            print(f"Make sure the path {file_path} is correct and the folder exists.")

def main():
    base_url = 'https://heroicons.com/'
    folder_paths = ["outline", "solid", "mini", "micro"]

    for folder_path in folder_paths:
        # Create the folder if it doesn't exist
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Set the URL based on the current folder_path
        url = f'{base_url}{folder_path}'
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Grab all svgs and their respective titles
        svgs = soup.find_all('svg', {'data-slot': 'icon'})
        titles = soup.find_all('div', {'class': 'truncate'})

        # Process SVG elements for the current folder path
        process_svg_elements(svgs, titles, folder_path)

if __name__ == "__main__":
    # Check if the script is being run directly
    main()
