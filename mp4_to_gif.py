import os
from datetime import datetime
from art import tprint
from moviepy.video.compositing.concatenate import concatenate_videoclips
from moviepy.editor import VideoFileClip, clips_array, concatenate_videoclips

def convert(dir, height = 400, second = 10, step = 2):
    if os.path.isfile(dir):
        
        # return name files for *.gif
        file_name = os.path.basename(dir)
        f_name = os.path.splitext(file_name)[0]
        
        print(f'[+] Original file: {file_name}')
        print(f'[+] Processing...')

        # open video and resize to height
        # clip1 = VideoFileClip(dir).subclip(0,2).resize(height=height)
        # clip2 = VideoFileClip(dir).subclip(2,4).resize(height=height)
        # ...
        # clip5 = VideoFileClip(dir).subclip(10,12).resize(height=height)
        clip_list = []
        for i in range(second+step):
            if i%step == 0:
                print(f"{i} {i+step}")
                clip_list.append(VideoFileClip(dir).subclip(i,i+step).resize(height=height))

        # final clip_list = [clip1, clip2, ..., clip5]
        final_clip = concatenate_videoclips(clip_list)
        final_clip.write_gif(f"{f_name}.gif")
        
        print(f'[+] {f_name}.gif saved successfully!\n---Have a good day---')
    
    else:
        print('File not exists, check the file in path')
    

if __name__ == "__main__":
    # return header
    tprint('mp4>>to>>gif', font='bulbhead')
    
    start = datetime.now()
    #-------
    file_path = input("\nEnter a file's path: ")
    height = input("Choose height, for resize video: ")

    convert(dir=str(file_path), height=int(height))
    #------
    end = datetime.now()
    print(f'[+] lead time {str(end-start)}')