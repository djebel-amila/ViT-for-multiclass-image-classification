# tkteach
A Super Fast Image Categorization Tool Written in Python
-------------------------------------------------------------

tkteach is a graphical tool that lets you quickly flip through datasets of images to categorize them.

Original features
----------

- Easily customizable categories and keyboard shortcuts
- Categorization can be done with arrow keys and keyboard shortcuts for improved speed, OR can be done with the mouse
- Category labels saved to sqLite database for easy retrieval
- Operates on one or more user-collected datasets of images
- Images can be zoomed in or out
- Allows multiple categorizations per image
- Category labels can be reviewed from within the application

![Screenshot](screenshot.PNG)

Fixes and improvements
----------

- Added resizing of images to fit the maximum size
- Fixed window size jumping
- Made zoom in/zoom out more gentle
- Zoom in by '+' **OR '='** (no need to hold the Shift button)
- Datasets moved to /ds folder and added preselecting the dataset if it's the only one available

![Screenshot](screenshot.PNG)

About
-----------

- Tested in both Python 2.7 and 3.6
- Requires PIL, sqlite3, and tkiner or Tkinter
