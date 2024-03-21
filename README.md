# ViT-classification-on-video-data-pipeline
This repository contains a complete pipeline for the classification of individual frames extracted from video data with custom labels. It contains various utilities in the form of Python script and/or Jupyter Notebooks for the convenient processing of data, the training of a Vision Transformer (ViT) model, the inference of additional data, the engraving of labels and other data on frames, and the re-assembling of the frames into new videos as final outputs. 

| Index       | Title       | Description   | Colab       |
| :----------  | :----------- | :------------- | :----------- | 
| 1           | <a target="_blank" href="https://github.com/djebel-amila/ViT-for-multiclass-image-classification/tree/main/1_extract_frames_from_video">Extract frames from video</a>     | This script extracts `.jpg` frames from any local or remote video file at the specified frame rate (must be below or equal to the video’s actual frame rate). The resulting  `.jpg` sequence is saved with numbered filenames at the video’s native resolution in a new folder ( "`$filename`-frames") created at the script’s location (except if it is run on Colab, they will have to be downloaded). | <a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/1_extract_frames_from_video/1_extract_frames_from_video.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>       |
| 2           | Title 2     | description 2 | Colab       |
| 3           | Title 3     | description 2 | Colab       |
| 4           | Title 4     | description 2 | Colab       |
| 5           | Title 5     | description 2 | Colab       |
| 6           | Title 6     | description 2 | Colab       |
| 7           | Title 7     | description 2 | Colab       |
| 8           | Title 8     | description 2 | Colab       |
| 9           | Title 9     | description 2 | Colab       |
| 10          | Title 10    | description 2 | Colab       |
| 11          | Title 11    | description 2 | Colab       |
| 12          | Title 12    | description 2 | Colab       |
| 13          | Title 13    | description 2 | Colab       |


The pipeline contains scripts for the following tasks: 
***
1. <a target="_blank" href="https://github.com/djebel-amila/ViT-for-multiclass-image-classification/tree/main/1_extract_frames_from_video">Extract frames from video</a>
<a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/1_extract_frames_from_video/1_extract_frames_from_video.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
   - This script extracts `.jpg` frames from any local or remote video file at the specified frame rate (must be below or equal to the video’s actual frame rate). The resulting  `.jpg` sequence is saved with numbered filenames at the video’s native resolution in a new folder ( "`$filename`-frames") created at the script’s location (except if it is run on Colab, they will have to be downloaded).
***
2. Random split training/test data
   - This python script … 
***
3. Frames labelling
   - This python script …
***
4. SQLite to csv
   - This python script is a small utility to turn a SQLite database into a `.csv` file.
5. Frames resizing
   - This python script resizes `.jpg` files to the specified resolution
6. ViT model training <a target="_blank" href="https://colab.research.google.com/github/djebel-amila/ViT-for-multiclass-image-classification/blob/main/ViT_multiclass_image_classification_training.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>
   - This jupyter notebook hosted on Google Colaboratory shows how to load the labelled dataset for the fine-tuning of a ViT classification model 
7. ViT model inferring
   - This jupyter notebook shows how to run and classify (label) new data on your fine-tuned ViT model.
8. Create table from directory
   - This python script will list in a `.csv` file all files that are located in a specified subfolder
9. Sort data from table to directory
   - This python script does the opposite as the previous one: it will move files listed in a `.csv` table into specified subfolder(s)
10. Sort data from table to directory
   - This python script does the opposite as the previous one: it will move files listed in a `.csv` table into specified subfolder(s)
11. Print label (text, watermark) on frames
   - This python script engraves labels on frames based on the content of a `.csv` table
12. Print label (image, watermark) on frames
   - This python script engraves a specified image on frames based on the directory they are located in
13. Create video from frames
   - This python script will re-assemble frames into an `.mp4` video file   

https://github.com/djebel-amila/ViT-for-multiclass-image-classification/blob/main/ViT_multiclass_image_classification_training.ipynb
