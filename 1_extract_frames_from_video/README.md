# Extract frames from video

This notebook allows to extract `.jpg` frames from any local or distant video file at a specified frame rate (must be below or equal to the video’s actual frame rate). The resulting  `.jpg` sequence is saved (with numbered frames) at the video’s native resolution in a new folder ( "`$filename`-frames") created at the script’s location. 

If you are using the jupyter notebook locally, the frames `jpg` files will be saved in a new folder created at the notebook’s location, notwithstanding the video source file’s location. 

<a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/1_extract_frames_from_video/1_extract_frames_from_video.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> You may open and run it in Google’s colab. If doing so, you may want to create a copy of the file on your own drive. Else, the generated folder and files will appear on Colab’s file system (in the left column) but you will have to manually save them. 

If you are running the `Python` script directly, you will require `python 3`, `opencv`, `numpy >= 1.21.3.`. You may open it to specify the desired framerate (currently 10 fps). To run the script, open the terminal and type `python ../path/to/script/1_extract_frames_from_video.py` followed by the path to target video (url or local), i.e.: <br>
`$ python /Users/username/Desktop/myPythonScripts/1_extract_frames_from_video/1_extract_frames_from_video.py http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4`
