import requests
import os
from urllib.parse import urlparse

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")
    
    urls = []

    # Get URLs from user
    while True:
        url = input("Enter an image URL (or type 'done' to finish): ")
        if url.lower() == 'done':
            break
        urls.append(url)

    # Tipos de imagens permitidos
    allowed_types = ('image/jpeg', 'image/png', 'image/gif')

    for url in urls:    
        try:
            # Create directory if it doesn't exist
            os.makedirs("Fetched_Images", exist_ok=True)
            
            # Fetch the image
            response = requests.get(url, timeout=10)
            response.raise_for_status()  # Raise exception for bad status codes

            # Verificar o tipo de arquivo
            content_type = response.headers.get("Content-Type", "")
            if content_type not in allowed_types:
                print(f"✗ Type not Allowed: {content_type}")
                continue

            # Verificar tamanho do arquivo (máx. 5 MB)
            content_length = int(response.headers.get("Content-Length", 0))
            if content_length > 5 * 1024 * 1024:  # 5 MB
                print(f"✗ Archive too big ({content_length/1024/1024:.2f} MB).")
                continue
            
            # Extract filename from URL or generate one
            parsed_url = urlparse(url)
            filename = os.path.basename(parsed_url.path)
            
            if not filename:
                filename = "downloaded_image.jpg"
                
            # Save the image
            filepath = os.path.join("Fetched_Images", filename)
            
            with open(filepath, 'wb') as f:
                f.write(response.content)
                
            print(f"✓ Successfully fetched: {filename}")
            print(f"✓ Image saved to {filepath}")
            print("\nConnection strengthened. Community enriched.")
            
        except requests.exceptions.RequestException as e:
            print(f"✗ Connection error: {e}")
        except Exception as e:
            print(f"✗ An error occurred: {e}")

if __name__ == "__main__":
    main()
