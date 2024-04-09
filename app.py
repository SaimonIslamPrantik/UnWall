import requests
import ctypes
import os

# Step 1: Get your Unsplash Access Key and replace 'YOUR_ACCESS_KEY'
UNSPLASH_ACCESS_KEY = 'dcp0uxjGLwwEhincRgASwwdxqLeltfhEsPxKhiq9qiw'
UNSPLASH_URL = f"https://api.unsplash.com/photos/random?client_id={UNSPLASH_ACCESS_KEY}&query=wallpaper&orientation=landscape"

# Step 2: Fetch a random wallpaper from Unsplash
def fetch_wallpaper():
    response = requests.get(UNSPLASH_URL)
    if response.status_code == 200:
        json_response = response.json()
        image_url = json_response['urls']['full']
        return image_url
    else:
        print("Failed to fetch wallpaper")
        return None

# Step 3: Download the wallpaper
def download_wallpaper(image_url):
    if image_url:
        image_bytes = requests.get(image_url).content
        with open('wallpaper.jpg', 'wb') as image_file:
            image_file.write(image_bytes)
        return os.path.abspath('wallpaper.jpg')
    else:
        return None

# Step 4: Set the image as desktop wallpaper
def set_desktop_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

if __name__ == "__main__":
    wallpaper_url = fetch_wallpaper()
    wallpaper_path = download_wallpaper(wallpaper_url)
    if wallpaper_path:
        set_desktop_wallpaper(wallpaper_path)
        print("Wallpaper set successfully.")
    else:
        print("Failed to set wallpaper.")