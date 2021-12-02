# Emotifier
### Note Emotifier use the Python 3.9 and the most recent versions of scipy, cv2, skimage, and PyQt5 if the build does not work it is likely a result of missing one of these packages.


# How to use each feature of the Emotifier:

## **Select Image:**
To first select an image click on the upload button and then the you will be prompted to select an image from the file explorer the image can be a .jpg, .png, or .bmp

After an image is selected the user can now perform any of the other functions on the image.


## **Pixelize:**
Pixelizing an image will result in the image having colors averaged and be displayed in larger pixels than the image. This function can be modified by using the window size feature. 

### Window size:
Window size takes in an integer for window size for the size of the resulting pixels in pixelize. By default this is 3.

## **Cartoonize:**
Cartoonizing an image will result in the image having colors averaged will add addtional lines to the image in an attempt to cartoonify the image. 

## **Abstractify:**
Abstractifying an image will result in the image having going through superpixeling and color averaging over each superpixel.

### Superpixels:
Superpixels takes in an integer for the number of superpixels that Abstracify will use to create an image. By default this is 1000

## Extract Foreground:
When the user checks the foreground detection box. They will then be able to input Row Column order coordinates on the image. These coordinates are then used to extract the foreground from the image in an attempt to only display the selected foreground.

Example of coordinate input 100,650;300,200
This gives two coordinates with the x and y coordinate seperated by a comma and the coordinate pairs seperated by a semicolon.

Fill Iterations takes in an integer and will iteratively fill the image to close holes within the foreground. This tends to be a number between 1 - 10
