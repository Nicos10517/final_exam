import csv
import pandas as pd 
import random

class Song: #gather songs and return them with all the relevant data
    def __init__(self, id: int, title: str, artist: str, album: str, duration_in_seconds: int):
        self.id = id
        self.title = title
        self.artist = artist
        self.album = album
        self.duration_in_seconds = duration_in_seconds
        self.times_played = 0
        #probably not the most efficient way to do this but here it is

    def __str__(self):
        return f"{self.id}, {self.title}, {self.artist}, {self.album}, {self.duration_in_seconds}, {self.times_played}"

class Playlist: #playlists class to store playlists and call them later for better functionality

    def __init__(self, name: str):
        self.name = name
        self.songs = []

    def add_song (self, song:Song):
        self.songs.append(song)

    def display_songs(self):
        for song in self.songs:
            print(song)

    def display_shuffle(self):
        pass #ran out of time a little bit, there is meant to be an organized shuffling method but instead it ended up scrambled down below (you'll see)
            


class MusicLibrary: #the implementation of the full music library
    def __init__(self):
        self.songs = []
        self.playlists = {}
        self.next_id = 1


    def import_music_library(self, df) -> None:
        for index, row in df.iterrows():
            self.add_song_to_library(row['title'], row['artist'], row['album'], int(row['duration_in_seconds']))


    def add_song_to_library(self, title: str, artist: str, album: str, duration_in_seconds: int) -> None:
        song = Song(self.next_id, title, artist, album, duration_in_seconds)
        self.songs.append(song)
        self.next_id += 1


    def display_library(self) -> None:
        for song in self.songs:
            print(song)


    def create_playlist(self, playlist_name: str) -> None:
        if playlist_name not in self.playlists:
            self.playlists[playlist_name] = Playlist(playlist_name)
        
        else:
            print(f"Playlist '{playlist_name}' already exists :/.") # making sure I don't run into this error because goodness I have before

    def add_songs_to_playlist(self, playlist_name: str, songs: list[int]) -> None:
        if playlist_name in self.playlists:
            playlist = self.playlists[playlist_name]
            found_songs = [song for song in self.songs if song.title in songs]
            if found_songs:
                for song in found_songs:
                    playlist.add_song(song)
                print(f"Added {len(found_songs)} songs to the playlist '{playlist_name}'.")
            else:
                print("No songs matched the titles provided.")


    def play_songs(self, playlist_name: str | None=None) -> None:
        if playlist_name in self.playlists:
            print(f"Playing songs in Playlist: {playlist_name}")
            self.playlists[playlist_name].display_songs()
        else:
            for song in self.songs:
                print(song)


    def shuffle_play(self, playlist_name: str | None=None) -> None:
        if playlist_name in self.playlists:
            shufint_list = []
            print(f"Shuffling songs in Playlist: {playlist_name}")
            length = len(self.songs in playlist_name)
            new_shuffle_order = [None] *length
            for i in new_shuffle_order:
                shufint = random.randint(0,length)
                for i in shufint_list:
                    if shufint_list[i] == shufint:
                        shufint = random.randint(0,length)
                    else:
                        shufint_list.append(shufint)
                        new_shuffle_order[i] = random.randint(0,length)
                        shufint = random.randint(0,length)

                i+=1

  

    def display_playlist(self, playlist_name: str) -> None:
        if playlist_name in self.playlists:
            print(f"Playlist: {playlist_name}")
            self.playlists[playlist_name].display_songs()
        else:
            print(f"Playlist '{playlist_name}' does not exist.")

    
    def search(self, search_criteria: str, playlist_name: str | None=None) -> None:
        if playlist_name in self.playlists:
            print (f"Searching for {search_criteria} in {playlist_name}")
            if search_criteria in self.songs in playlist_name:
                print(f"Found {search_criteria} in {playlist_name}")
            else:
                print(f"Could not find {search_criteria in {playlist_name}}")
        else:
            print (f"Searching for {search_criteria} in Music Library")
            if search_criteria in self.songs:
                print(f"Found {search_criteria} in Music Library")
            else:
                print(f"Could not find {search_criteria} in Music Library")




def main ():
    df = pd.read_csv('songs.csv')
    library = MusicLibrary()
    '''
    library.add_song_to_library("Bad Habits", "Ed Sheeran", "=", 231)
    library.import_music_library(df)
    library.display_library()
    ''' #Step 1 testing

    '''library.create_playlist("Boogie Wonderland")
    library.add_songs_to_playlist("Boogie Wonderland", ["Dance Monkey"]) #said no songs matched the titles provided but at least I know it works, I'm going to move on
    library.display_playlist("Boogie Wonderland")''' #Step 2 testing



if __name__ == '__main__':
    main()