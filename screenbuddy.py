#!/usr/bin/python
import sys
import time
from screen_recorder_sdk import screen_recorder 

def main():
    try:
        if len(sys.argv) == 2 :     
            file_name = sys.argv[1]
            params = screen_recorder.RecorderParams ()
            screen_recorder.init_resources(params)
            screen_recorder.start_video_recording(file_name +'.mp4',30,800000,True)   
            time.sleep(6000)         
        elif len(sys.argv) == 1:
            print("Oops! please provide a file name")
        else:
            print("only one file name at a time is allowed")
    except KeyboardInterrupt:
            print("Recording stopped. File saved as "+file_name+".mp4")
            screen_recorder.stop_video_recording()

if __name__ == '__main__':
    main()