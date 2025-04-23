# Tidal Playlist Liker Automation 🎶

This Python script allows you to automatically "like" every track from all of your Tidal playlists.

## ✅ Features

- Fetches all your playlists using the Tidal API
- Iterates through every track in each playlist
- Likes each song by adding it to your favorites
- Fully automated with simple Python and `requests`

---

## 🧠 Why I Made This

I had thousands of songs spread across different playlists and wanted to easily shuffle them all from my “Liked” tracks. Tidal didn’t offer a native way to bulk-like songs — so I built my own.

This script helped me get it done instantly.

---

## 🛠️ How to Use

1. Clone this repository and open `like_all_tidal_tracks.py`
2. Replace:
   - `TOKEN` with your Tidal session token
   - `USER_ID` with your Tidal user ID (both explained below)
3. Run the script using:

#python like_all_tidal_tracks.py


4. Open Tidal → **My Collection** → **Tracks** → Enjoy all your playlist songs shuffled in one place 💚

---

## 🔐 How to Get Your Token and User ID

You’ll need two values:  
- Your **Tidal session token**
- Your **Tidal user ID**

### 1. Open the Tidal Web Player  
Go to: https://listen.tidal.com and log in.

### 2. Open DevTools  
- Press `F12` or right-click > **Inspect**
- Go to the **Network** tab

### 3. Find a Playlist Request  
- Click on one of your playlists
- Look in the Network panel for a request that includes `playlists`
- Click it and go to the **Headers** tab

### 4. Get Your Token  
In the **Request Headers**, find a line like this: authorization: Bearer eyJraWQiOiJ2OU1G...


Copy everything **after** `Bearer` → that’s your `TOKEN`.

### 5. Get Your User ID  
In the same or other requests, find a line like: users/203150686/playlists

The number is your `USER_ID`.

---

## ⚠️ Disclaimer

This script uses your private Tidal session token, which acts like a password. **Do not share it** or commit it to a public repo.

This project is for educational and personal use only.

---

Made with ❤️ by [@diegobarocio](https://github.com/diegobarocio)
