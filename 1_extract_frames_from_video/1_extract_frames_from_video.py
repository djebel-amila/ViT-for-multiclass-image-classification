# This Python script leverages openCV (cv2) and numpy to extract the frames of a given video file at a desired framerate (10 fps by default) and saves them (with frame numbering) in a new folder as jpg images, keeping their native resolution. 
# requires python 3, opencv, numpy >= 1.21.3. 
# use: In terminal, run program followed by the path to video (filename), i.e.: 
# python 1_extract_frames_from_video.py http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4

from datetime import timedelta
import cv2
import numpy as np
import os
import math

# i.e if video of duration 30 seconds, saves 10 frame per second = 300 frames saved in total
SAVING_FRAMES_PER_SECOND = 10.0

def get_saving_frames_durations(cap, saving_fps):
    """A function that returns the list of durations where to save the frames"""
    s = []
    # get the clip duration by dividing number of frames by the number of frames per second
    clip_duration = cap.get(cv2.CAP_PROP_FRAME_COUNT) / cap.get(cv2.CAP_PROP_FPS)
    # use np.arange() to make floating-point steps
    print("current frames in video:", math.floor(cap.get(cv2.CAP_PROP_FRAME_COUNT)))
    print("duration of the video in seconds:", clip_duration)
    print("extracting frames:", saving_fps, "FPS")
    frame_count_prediction = saving_fps * clip_duration
    print("total frames expected:", math.floor(frame_count_prediction-1))
    for i in np.arange(0, clip_duration, 1 / saving_fps):
        s.append(i)
    return s
    print(s)


def main(video_file):
    filename, _ = os.path.splitext(video_file)
    #filename += "-frames"
    newdir = filename + "-frames"
    folder = newdir.split("/")
    # if there isn't already one, create a folder named after filename + "-frames"
    if not os.path.isdir(folder[len(folder)-1]):
        os.mkdir(folder[len(folder)-1])
    # read the video file
    cap = cv2.VideoCapture(video_file)
    # get the FPS of the video
    fps = cap.get(cv2.CAP_PROP_FPS)
    print("source video fps:", fps, "FPS")
    # if the SAVING_FRAMES_PER_SECOND is above video FPS, then set it to FPS (as maximum)
    saving_frames_per_second = min(fps, SAVING_FRAMES_PER_SECOND)
    # get the list of duration spots to save
    saving_frames_durations = get_saving_frames_durations(cap, saving_frames_per_second)
    # start the loop
    count = 0
    index = 0
    while True:
        is_read, frame = cap.read()
        if not is_read:
            # break out of the loop if there are no frames to read
            break
        # get the duration by dividing the frame count by the FPS
        frame_duration = count / fps
        try:
            # get the earliest duration to save
            closest_duration = saving_frames_durations[0]
        except IndexError:
            # the list is empty, all duration frames were saved
            break
        	
        if frame_duration >= closest_duration:
            # if closest duration is less than or equals the frame duration, 
            # then save the frame
            #frame_duration_formatted = format_timedelta(timedelta(seconds=frame_duration))
#            cv2.imwrite(os.path.join(filename, str(video_file) + "-" + str(index) + ".jpg"), frame)
            videoname = filename.split("/")
            videoname = videoname[len(videoname)-1]
            newfile = os.path.join(folder[len(folder)-1], videoname + "-" + str(index) + ".jpg")
            cv2.imwrite(newfile, frame) 
            index += 1

            # drop the duration spot from the list, since this duration spot is already saved
            try:
                saving_frames_durations.pop(0)
            except IndexError:
                pass
        # increment the frame count
        count += 1

if __name__ == "__main__":
    import sys
    video_file = sys.argv[1]
    main(video_file)
