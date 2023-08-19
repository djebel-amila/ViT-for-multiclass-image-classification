# Extract frames from video

This notebook allows to extract `.jpg` frames from any local or distant video file at a specified frame rate (must be below or equal to the video’s actual frame rate). The resulting  `.jpg` sequence is saved (with numbered frames) at the video’s native resolution in a new folder ( "`$filename`-frames") created at the script’s location. 

<a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/1_extract_frames_from_video/1_extract_frames_from_video.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a> You may open and run it in Google’s colab. If doing so, you may want to create a copy of the file on your own drive. Else, the generated folder and files will appear on Colab’s file system (in the left column) but you will have to manually save them. 