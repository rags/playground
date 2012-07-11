import sys, os, glob, qllib, shutil, formic


def safe_read_tag(tags,key):
    return tags[key][0].strip().replace('/',' ') if tags[key] and len(tags[key])>0 and len(tags[key][0].strip())>0 else 'Unknown ' + key.title()

for fname in formic.FileSet(directory="/home/rags/Downloads/Carnatic/Carnatic",include="*.mp3"):
    tags = qllib.AudioFile(fname)
    artist = safe_read_tag(tags,'artist')
    if(artist != "Unknown Artist"):        
        title = safe_read_tag(tags,'title')
        tags['artist'] = 'Unknown Artist'
        tags['title'] = artist + " - " + title
        tags.write()
        print "-------------"
        print tags['title'] 
        print ['artist']
        
        
