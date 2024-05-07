# final_exam

Sources Used: Github copilot was not used, various internet searches of errors such as str.object is not an iterator, specifics of the pandas dataframe syntax ,  AttributeError: Object has no attribute?, looking up randint(), list reorder syntax etc. were used.

Level 1:

    Goals:
        Import Music
        Add a song
        Display Music Library

So I began by separating my two factors, songs and song compilations (or the music library) into 2 different classes so as to address them more specifically in the future. We have first our classic def init that contains all the specifics of defining each song first by its ID number fallowed by it's title, artist, album, duration (always in seconds), and the amount of tiems it has been played, which I thought would be useful for later when I attempt to do a shuffle if I have enough time (fingers crossed)

Next, I added the new def's to import, add music, and display the library, whose titles were given int the exam description. I read in the songs.csv file using pandas because that's all I know after taking Data in the Cosmos, and defined the row so that it understood that each row included the title.etc. Initially I just tried to do df.title..etc. and have it read one by one but then I realized that was stupid and I should just define the row and have it search through them, so I did that instead. This, however, led to dataframe error, which according to the internet, might have happened when I tried to use pandas and then mesh it, so I had to think of another way to do this.

it worked! my I had to adjust some of the syntax because I still kept mixing up pandas and not pandas, and reading in the dataframe wrong, but my first official output in the terminal is this! 

26, Dance Monkey, Tones and I, The Kids Are Coming, 207, 0
27, Señorita, Shawn Mendes with Camila Cabello, Shawn Mendes, 191, 0
28, Sunflower (Spiderman: Into the Spider-Verse), Post Malone & Swae Lee, Spider-Man: Into the Spider-Verse Soundtrack, 159, 0
29, The Box, Roddy Ricch, Please Excuse Me for Being Antisocial, 210, 0
30, Rockstar, Post Malone, Beerbongs & Bentleys, 217, 0
31, Old Town Road (Remix), Lil Nas X (feat. Billy Ray Cyrus), Old Town Road EP, 157, 0

I probably simultanesouly made it easier and also a lot more complicated by using pandas but oh well.

I'm glad I'm making progress, since I'm so behind and have so much make up work in this class I was worried that I would get to the final exam and not even get a C since I've been struggling to follow along, but I'm actually really enjoying this exam and though it's been quite time consuming and a lot of trial and error thus far, I don't feel like I"m too far behind. I definitely could be faster and I've had to look up a lot of simple syntax errors, but I'm making good progress and that's what matters.

Finished level 1 at 2:59pm


Level 2:

    Goals:
        Create a playlist:
        Add songs to playlist:
        Play Songs:

Level 2!! I appreciate the very straightforward both grading method and sort of step-by-step guide this assignment has in its concept. Now I need to work on creating a playlist, adding songs, and playing them, so naturally, we're going to introduce a new def, that I'm just plopping into the music library class as well as adding a playlist class so it can reference itself which may not be the most organized thing in the world but it makes sense in my head, just so that I can refer to itself easier and all that. Now I'll admit this step felt a lot more daunting than the first because I was trying to think of how someone would naturally make a playlist and I thought of the whole user interface that I obviously do not have time to make and suddenly the project seems a lot bigger, but I figured one only makes a playlist if they already know what songs they want to play, so I went from there, using a typical list (haha.. play..list) and appending as songs are added. I had to make sure that the playlist class had its own init and naming function and I spent a lot of time with typos in the code defining dictionaries as playlist instead of playlists or vise versa before adding in the given methods from the exam of create playlist and add a song to a playlist. Initially started by searching through the lists of existing songs with song id but then I realized that made no sense and who adds songs using their id and not their title so I changed it back. I realize this does make it so that currently there could be errors if someone doesn't spell a song right or there's case sensitivity, but I'm sure with more time I would be able to figure out how do fix that but right now I'm not going to worry about it too much and focus on getting everything out there since I'm starting to run out of time. 

I'm now moving on the the play songs feature at 3:49 (yikes)

-- after a very stupid error (sorry professor for making you come over for that, I'm deciding to move on to make the play songs and the shuffle play at the same time becuase I think that will be convenient)

Finished level 2 at 4:10pm (ahhh an hour left I'm getting a little nervous)

Level 3:

    Goals:
        Shuffle Play:
        Search:

For the shuffle play and regular play, since we're not utilizing the ability to pauase, rewind etc, the defs are essentially a repeat of the display playlist but in specific orders, either the original order or a shuffled order. So I basically just copied the display playlist code and tweaked it as needed, which was a bit of a relief because I thought this part would be a lot more compicated than it ended up being.... 

I spoke too fast. It never occured to me how I would actually get the playlist to shuffle, but luckily we're here at 4:26 so I still have a bit of time to figure it out, and for now am going to move to complete the search method before coming back to it. Completed the search aspect! It is now 4:34 and the rest of the time I have is to figure out how to shuffle things and also how to possibly shuffle things.

I've decided to try and conceive a list with a random order before doing anything else, and trying to use that order to apply it to the playlist, and return essentially a new playlist with the same name but a different order. We've gotten to the point where I'm starting to get really tired and I"m not quite sure if this is going to work as intended, but I hope the idea is communicated. There's definitely a problem with the nested for loops and how the actual shuffle design itself is very costly and not super effective, there's probably a simpler and more efficient way to do it, but at this time I'm struggling to search for my thoughts and need food lol and I'm not sure if I'm going to be able to implement it correctly and as intended in the time (it is now 4:54) so I'm just going to work on submitting what I have.