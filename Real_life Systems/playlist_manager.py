class Playlist:
  def __init__(self):
     self.playlist=[]
     
  def addSong(self,song):
    self.playlist.append(song)
    
  def removeSong(self,song):
    if song in self.playlist:
      self.playlist.remove(song)
      return True
    else:
      return False
      
  def playNext(self):
    return self.playlist.pop(0)
    
  def getPlaylist(self):
    return self.playlist
    
play=Playlist()
play.addSong("Song 1")
play.addSong("Song 2")
play.addSong("Song 3")

print(play.getPlaylist())
print(play.playNext())
print(play.removeSong("Song D"))
print(play.removeSong("Song B"))
print(play.getPlaylist())
    
    