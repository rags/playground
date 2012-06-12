import sys, os, glob, qllib, shutil

def import_files(ipod_control_music_dir, dest_dir):
    print "Processing... "
    for fname in glob.glob(os.path.join(ipod_control_music_dir,'*','*')):
            import_file(fname, dest_dir)
    
def safe_read_tag(tags,key):
    return tags[key][0].strip().replace('/',' ') if tags[key] and len(tags[key])>0 and len(tags[key][0].strip())>0 else 'Unknown ' + key.title()

def import_file(ipod_file,dest_dir):
    try:
        tags = qllib.AudioFile(ipod_file)
        artist = safe_read_tag(tags,'artist')
        album = safe_read_tag(tags,'album')
        title = safe_read_tag(tags,'title')
        artist_album_dest_dir = os.path.join(dest_dir,artist, album)
        not(os.path.exists(artist_album_dest_dir)) and os.makedirs(artist_album_dest_dir) 
        dest_file = os.path.join(artist_album_dest_dir,title) + os.path.splitext(ipod_file)[1]
        print "{} -> {}".format(ipod_file,dest_file)
        shutil.copyfile(ipod_file,dest_file)
    except Exception as e:
        print "Error processing [{}]\n Error: {}".format(ipod_file,e)

if __name__ == "__main__":
    import_files(sys.argv[1], sys.argv[2])
