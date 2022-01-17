# Note: <mark> The tool is designed specifically for windows hosts<mark>

# Screenbuddy
A simple screen recorder program written in python. Screenbuddy takes the file name as argument and start recording the screen for the specified time. User can specify the recording time and directory to which the recording has to be saved. If not specified explicitly after the specified time the recording will get automatically saved in the current working directory. The recording can be adjusted as per the demand and has to be specifed in minutes.

# Requirement
- [Python 3.x(64-bit)](python.org)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [screen-recorder-sdk](https://pypi.org/project/screen-recorder-sdk/)
- [colorama](https://pypi.org/project/colorama/)

Make sure you have the latest version of 64-bit python and pip installed in your system. Once python and pip are properly confirgured run
```
pip install screen-recorder-sdk
```

# How to Use

```
 screenbuddy.py file_name 
```
