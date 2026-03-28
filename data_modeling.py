# playlist

_position = 1

title_card = {
    "playlist_name": "Super Likes",
    "created_by": "Jared Truscott",
    "number_of_songs": 275,
    "length": "19hr 10min",
}

first_five_songs = [
    {
        "position": _position,
        "title": "Season of the Shark",
        "artist": ["Say Sue Me"],
        "album": 10,
        "play_length": "4:39",
    },
    {
        "position": (_position := _position + 1),
        "title": "Trusty Chords",
        "artist": ["Hot Water Music", "Chuck Ragan"],
        "album": "Caution",
        "play_length": "2:50",
    },
    {
        "position": (_position := _position + 1),
        "title": "Promised Land",
        "artist": ["Skeletal Family"],
        "album": "Killed By Deathrock",
        "play_length": "4:50",
    },
    {
        "position": (_position := _position + 1),
        "title": "Melodie",
        "artist": ["IDIOTAPE"],
        "album": 1111101,
        "play_length": "5:01",
    },
    {
        "position": (_position := _position + 1),
        "title": "Somebody Else",
        "artist": ["Pynch"],
        "album": "Somebody Else",
        "play_length": "5:32",
    },
]

playlist = [title_card, first_five_songs]
formatted_playlist = f"\n{playlist[0]['playlist_name']} by {playlist[0]['created_by']} has {playlist[0]['number_of_songs']} songs and is {playlist[0]['length']} long.\n"

formatted_first_five_songs = [
    f"{song['position']}. {song['title']} by {', '.join(song['artist'])} from the album {song['album']} is {song['play_length']} long."
    for song in playlist[1]
]

print(formatted_playlist)
print("The first " + str(len(playlist[1])) + " songs in this playlist are:")
print("\n".join(formatted_first_five_songs))
