# Ubuntu_Requests
Ubuntu-Inspired Image Fetcher Assignment
# Ubuntu Image Fetcher

A Python program inspired by the Ubuntu philosophy — *"A person is a person through other persons"*. This tool connects to the global community of the internet, fetches shared images, and organizes them for later appreciation.

---

## 🌟 Features

* **Fetch Multiple Images**: Enter several URLs, and the script downloads them all.
* **Organized Storage**: Saves images inside a `Fetched_Images` folder.
* **Duplicate Detection**: Uses file hashes to prevent downloading the same image twice.
* **Safety First**: Validates HTTP headers (`Content-Type`, `Content-Length`) and only downloads files that are truly images and under 10MB.
* **Graceful Error Handling**: Respects unreliable connections and invalid inputs without crashing.
* **Community Respect**: Sends a friendly `User-Agent` header and handles errors politely.

---

## 📋 Requirements

* Python 3.7+
* `requests` library

Install `requests` if not already installed:

```bash
pip install requests
```

---

## 🚀 Usage

1. Save the script as `fetch_images_ubuntu.py`.
2. Open a terminal in the script's directory.
3. Run the script:

   ```bash
   python fetch_images_ubuntu.py
   ```
4. Enter one or more image URLs (press **Enter** after each). When finished, press **Enter** on an empty line.
5. The images will be downloaded to the `Fetched_Images` folder.

---

## 🛡️ Precautions When Downloading Files

* Only use **trusted URLs**.
* Verify that the source is legitimate.
* Check the size of the files (script skips >10MB by default).
* Confirm the `Content-Type` header matches the expected file type.

---

## 💡 Example

```
> https://example.com/images/photo1.jpg
> https://picsum.photos/300
> https://www.example.com/sample.png
>
```

Output:

```
🌍 Ubuntu Image Fetcher — connecting people through shared images.

🔗 [1/3] Connecting to https://example.com/images/photo1.jpg ...
✅ Saved: Fetched_Images/photo1.jpg

🔗 [2/3] Connecting to https://picsum.photos/300 ...
✅ Saved: Fetched_Images/image_ab12cd34ef56.jpg

🔗 [3/3] Connecting to https://www.example.com/sample.png ...
✅ Saved: Fetched_Images/sample.png

🎉 All done! Images are organized in the 'Fetched_Images' folder.
```

---

## 🙌 Ubuntu Principles in Action

* **Community**: Connects with shared online resources.
* **Respect**: Treats errors and network issues gracefully.
* **Sharing**: Stores and organizes downloaded images for easy access.
* **Practicality**: Provides a real-world tool for gathering and managing images.

---

## 📜 License

This project is released under the MIT License — free to use, modify, and share in the spirit of Ubuntu.
