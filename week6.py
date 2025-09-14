import os
import requests
import hashlib
from urllib.parse import urlparse
from datetime import datetime

def get_safe_filename(url, content=None):
    """
    Extract a filename from the URL or generate one using a hash of the content.
    """
    parsed_url = urlparse(url)
    base = os.path.basename(parsed_url.path)

    if base and "." in base:
        return base
    # If no name, generate from hash or timestamp
    if content:
        file_hash = hashlib.md5(content).hexdigest()[:12]
        return f"image_{file_hash}.jpg"
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"image_{timestamp}.jpg"


def fetch_images():
    print("Ubuntu Image Fetcher — connecting people through shared images.")
    print("Enter multiple image URLs (one per line). Press Enter on a blank line to finish:\n")

    # Read multiple URLs
    urls = []
    while True:
        url = input("> ").strip()
        if not url:
            break
        urls.append(url)

    if not urls:
        print("No URLs provided. Exiting respectfully.")
        return

    folder = "Fetched_Images"
    os.makedirs(folder, exist_ok=True)

    # Keep track of hashes to avoid duplicates
    downloaded_hashes = set()

    for idx, url in enumerate(urls, start=1):
        print(f"\n🔗 [{idx}/{len(urls)}] Connecting to {url} ...")

        try:
            # Security precaution: allow only http(s)
            if not (url.startswith("http://") or url.startswith("https://")):
                print("Skipping (invalid or unsafe URL). Must start with http:// or https://")
                continue

            # Fetch with headers for safety and proper handling
            headers = {"User-Agent": "UbuntuImageFetcher/1.0"}
            response = requests.get(url, timeout=12, headers=headers)
            response.raise_for_status()

            # Check important HTTP headers
            ctype = response.headers.get("Content-Type", "")
            clen = response.headers.get("Content-Length")

            if not ctype.startswith("image/"):
                print(f"Skipping: content is not an image (Content-Type={ctype})")
                continue

            # Safety: check size limit (e.g., < 10MB)
            if clen and int(clen) > 10 * 1024 * 1024:
                print("Skipping: image is larger than 10MB.")
                continue

            content = response.content
            file_hash = hashlib.md5(content).hexdigest()

            # Prevent duplicates
            if file_hash in downloaded_hashes:
                print("Duplicate detected — already downloaded this image.")
                continue

            downloaded_hashes.add(file_hash)
            filename = get_safe_filename(url, content)
            filepath = os.path.join(folder, filename)

            # Save image safely
            with open(filepath, "wb") as f:
                f.write(content)

            print(f"Saved: {filepath}")

        except requests.exceptions.MissingSchema:
            print("Invalid URL format. Include http:// or https://")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error: {http_err}")
        except requests.exceptions.ConnectionError:
            print("Network issue: could not connect.")
        except requests.exceptions.Timeout:
            print("Timeout: the server took too long to respond.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    print("\n🎉 All done! Images are organized in the 'Fetched_Images' folder.")


if __name__ == "__main__":
    fetch_images()
