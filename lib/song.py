class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist.lower()
        self.genre = genre
        Song.count += 1
        self.add_to_genres()
        self.add_to_artists()

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    def add_to_genres(self):
        if self.genre not in Song.genres:
            Song.genres.append(self.genre)
            Song.add_to_genre_count()

    def add_to_artists(self):
        if self.artist not in Song.artists:
            Song.artists.append(self.artist)
            Song.add_to_artist_count()

    @classmethod
    def add_to_genre_count(cls):
        genre_histogram = {}
        for song in cls.genres:
            if song in genre_histogram:
                genre_histogram[song] += 1
            else:
                genre_histogram[song] = 1
        cls.genre_count = genre_histogram

    @classmethod
    def add_to_artist_count(cls):
        artist_histogram = {}
        for artist in cls.artists:
            if artist in artist_histogram:
                artist_histogram[artist] += 1
            else:
                artist_histogram[artist] = 1
        cls.artist_count = artist_histogram

