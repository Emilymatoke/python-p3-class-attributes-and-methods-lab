class Song:
    count = 0 
    genres = []
    artists =[]
    genre_count = {}

    def __init__(self, name, artist, genre) :
        Song.count += 1
        self.add_song_to_count ()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.name = name
        self.artist = artist
        self.genre = genre

    @classmethod
    def add_song_to_count(cls, increment=1) :
        cls.count += increment

    @classmethod
    def add_to_genres(cls, genre) :
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist) :
        if artist not in cls.artists:
            cls.artists.append(artist)
 
    @classmethod
    def add_to_genre_count(cls,genre) :
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1


    



