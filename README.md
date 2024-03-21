# Fine-tuning ViT for classification: video pipeline utilities
This repository contains a complete pipeline as a series of utility scripts for preparing a training set from video data, training of a ViT model, inference, frames engraving for data visualization and frames re-assembling to output annotated videos. 

The pipeline contains scripts for the following tasks: 

| Index | Title | Description | Script |
| :----------  | :----------- | :------------- | :----------- | 
| 1           | <a target="_blank" href="https://github.com/djebel-amila/ViT-for-multiclass-image-classification/tree/main/1_extract_frames_from_video">Frame extraction</a>     | This script lets you extract `.jpg` frames from any local or remote video file at the specified frame rate (it must be below or equal to the video’s actual frame rate). The resulting  `.jpg` sequence is saved with numbered filenames at the video’s native resolution in a newly created folder ( "`$filename`-frames") created at the script’s location (except if it is run on Colab: they will have to be downloaded). | <a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/1_extract_frames_from_video/1_extract_frames_from_video.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>       |
| 2           | Random split | This script lets you select a specified amount of random data from subdirectories in order to create a training or a test set. | Colab |
| 3           | Frame labelling | This is a fork of the sklite sofware that is a convenient way to manually label images with keyboard shortcuts. | Colab |
| 4           | SQLite to csv | This script is a small utility to turn a SQLite database into a `.csv` file. | Colab |
| 5           | Frame resizing | This script resizes a batch of `.jpg` files to the specified resolution | Colab |
| 6           | Training | This notebook hosted on Google Colaboratory for GPU resources lets you load your labelled dataset and use it to fine-tuning a ViT classification model. | <a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/ViT_multiclass_image_classification_training.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a> |
| 7           | Inference | This notebook shows how to run and classify (label) new data on your local or remote fine-tuned ViT model. | Colab |
| 8           | Dir to table | This script will list all files that are located in a specified folder in a `.csv` file. | Colab |
| 9           | Table to dir | This script does the opposite as the previous one: it will move files to folders as specified by a `.csv` table | Colab |
| 10          | Print labels | These scripts engrave labels (text or image) on frames based on the content of a `.csv` table or on the folder they’re in. | Colab |
| 11          | Frames to video | This python script will re-assemble frames into an `.mp4` video file. | Colab |




https://github.com/djebel-amila/ViT-for-multiclass-image-classification/blob/main/ViT_multiclass_image_classification_training.ipynb
