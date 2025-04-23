import requests

# Replace with your actual values for local use
TOKEN = "YOUR_TIDAL_BEARER_TOKEN"
USER_ID = "YOUR_TIDAL_USER_ID"

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/json"
}

print("Fetching your playlists...")
playlists = []
offset = 0

while True:
    url = f"https://api.tidal.com/v1/users/{USER_ID}/playlists?countryCode=MX&limit=50&offset={offset}"
    r = requests.get(url, headers=HEADERS)

    try:
        data = r.json()
    except Exception as e:
        print(f"❌ JSON conversion error: {e}")
        print("Raw response:", r.text)
        break

    print(f"→ Offset {offset} - Status {r.status_code}")

    if "items" in data and not data["items"]:
        print("🚫 No more playlists, ending.")
        break
    elif "items" not in data:
        print("⚠️ Unexpected format:", data)
        break

    playlists.extend(data["items"])
    offset += 50

print(f"\n✅ Total playlists found: {len(playlists)}")

for playlist in playlists:
    name = playlist["title"]
    playlist_id = playlist["uuid"]
    print(f"\n🎵 Processing playlist: {name}")

    track_ids = []
    offset = 0

    while True:
        url = f"https://api.tidal.com/v1/playlists/{playlist_id}/tracks?countryCode=MX&limit=100&offset={offset}"
        r = requests.get(url, headers=HEADERS)
        data = r.json()

        if "items" in data and not data["items"]:
            break
        elif "items" not in data:
            print(f"⚠️ No valid tracks in {name}")
            break

        track_ids += [item["id"] for item in data["items"]]
        offset += 100

    print(f"  → Tracks found: {len(track_ids)}")

    for track_id in track_ids:
        url = f"https://api.tidal.com/v1/users/{USER_ID}/favorites/tracks?countryCode=MX"
        res = requests.post(
            url,
            headers={**HEADERS,
                     "Content-Type": "application/x-www-form-urlencoded"},
            data={"trackIds": track_id}
        )

        print(f"🔁 Liking track {track_id} → Status: {res.status_code}")
        print("➡️ Response:", res.text)

print("\n🎉 All done! Your playlists' tracks should now be liked on Tidal.")
# Note: This script is for educational purposes only. Use responsibly and ensure compliance with Tidal's API terms of service.
