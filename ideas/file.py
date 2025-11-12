test: "username"

PSCOST: "5:00" 

"login": 'STOLENHAHA"



def get_playlist(mood):
    # Define mood-to-music mappings
    playlists = {
        "happy": [
            "Happy - Pharrell Williams",
            "Walking on Sunshine - Katrina & The Waves",
            "Good as Hell - Lizzo"
        ],
        "sad": [
            "Someone Like You - Adele",
            "Fix You - Coldplay",
            "Let Her Go - Passenger"
        ],
        "energetic": [
            "Eye of the Tiger - Survivor",
            "Can't Hold Us - Macklemore",
            "Stronger - Kanye West"
        ],
        "chill": [
            "Sunflower - Post Malone",
            "Lo-Fi Beats - Chillhop Music",
            "Weightless - Marconi Union"
        ]
    }

    # Return playlist or fallback message
    return playlists.get(mood.lower(), ["No playlist found for that mood. Try happy, sad, energetic, or chill."])

# Main interaction
if __name__ == "__main__":
    print("🎶 Welcome to Gab's Mood-Based Music Recommender!")
    user_mood = input("How are you feeling today? (happy, sad, energetic, chill): ")
    recommendations = get_playlist(user_mood)

    print("\n🎵 Recommended Playlist:")
    for song in recommendations:
        print(f"- {song}")
