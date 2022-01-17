# Screenbuddy
Sreenbuddy is a simple recording program written in python. It takes the file name as argument and start recording the screen for the specified time. User can specify the recording time and directory to which the recording has to be saved. If not specified explicitly after the specified time the recording will get automatically saved in the current working directory. The recording can be adjusted as per the demand and has to be specifed in minutes.

## Requirement
- [Python 3.x(64-bit)](python.org)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [screen-recorder-sdk](https://pypi.org/project/screen-recorder-sdk/)
- [colorama](https://pypi.org/project/colorama/)
```
 pip install screen-recorder-sdk
```
```
 pip install colorama
```
## Install Screenbuddy
Screenbuddy is designed specifically for windows hosts, it requires latest vaersion of 64-bit python and pip installed in your system.
Run the following command to install the latest version -

```
 https://github.com/SCR1P7K1DD13/screenbuddy.git
```
### Usage

``` 
python screenbuddy.py <file_name>
```
## How it works
1. Once installed run the command:
```
 python screenbuddy.py myrecording
 ```
2. Specify the directory to which the recording has to be saved
3. Specify the record duration in minutes. Click on enter.
<img width="524"  alt="image" src="https://user-images.githubusercontent.com/56312786/149762709-5ba148f2-1852-4772-9165-0aeed6ce5a76.png">
4. Once completed the recording will be saved in the specified directory. 
