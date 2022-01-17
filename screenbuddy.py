#!/usr/bin/python
import sys
import time
import os
import colorama
from screen_recorder_sdk import screen_recorder 
from colorama import Fore, Back, Style
colorama.init()

def main():
    try:
        if len(sys.argv) == 2 :    
            cwd = os.getcwd()
            print( Fore.GREEN + "Current working directory: {0} ".format(cwd))
            print( Fore.RESET)
            ans = input("Do you want to change the directory:(y/n)?")
            ans = ans.lower()
            if ans == 'y':
                directory = input ("Please specify the path: ")
                isFile = os.path.isfile(directory)
                os.chdir(directory)   
            record_duration = float(input("Enter the record duration in minutes: "))
            file_name = sys.argv[1]
            print(Fore.YELLOW)
            params = screen_recorder.RecorderParams ()
            screen_recorder.init_resources(params)
            screen_recorder.start_video_recording(file_name +'.mp4',30,800000,True)  
            time.sleep(record_duration * 60) 
            screen_recorder.stop_video_recording()
            print(Fore.GREEN)        
            print("Recording stopped. File saved as "+file_name+".mp4")
        elif len(sys.argv) == 1:
            print(Fore.RED + "Oops! please provide a file name")
        else:
            print(Fore.RED + "only one file name at a time is allowed")
    except KeyboardInterrupt:
        print(Fore.RED)
        print("Recording stopped")
        screen_recorder.stop_video_recording()

if __name__ == '__main__':
    main()