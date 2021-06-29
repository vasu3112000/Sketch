# Sketch
This Project allows you to convert your boring pictures to an interesting picture sketch.
# Installation
Download the complete folder and save it anywhere on your desktop. Open the file named test.py in a any python IDE such as pycharm, anaconda etc.

Install Open-CV library in your interpreter if it is not present. Once installed, you're ready to use the software.

Copy the image you want to convert to the pencil sketch and paste it in the project folder and write the name of the picture in the code test.py.

# Working of the Project
Once you run the code multiple windows will open up.

Firstly the original image you copied in the folder will be displayed on the screen.
Further running the code the image will be converted to a gray image and the output will be displayed on the screen.
Now the displayed image that is the semi finale step is the image converted to an inverted image
Finally we get our desired output which is the pencil sketch on the screen.

In the end there will be two windows one will be the original image and the other the pencil sketch showing the transformation that has occured in the image.

# Code Explanation
We have used the open cv library of python for this project.

First I read the image file using inbuilt function of opencv library.

Then I converted the image to diffent colours using the inbuilt "cvtColor" function. I also blurred the image using the "cv2.GaussianBlur" function and finally to give it a pencil sketch look I used "cv2.divide" function. Also to get all the outputs on screen I used the "cv2.imshow" function.

To know more about these function you can refer to the documentation of open-cv library.

# Summary
As you might have understood till now, I've made a software that will help you covert your standard images to a pencil sketch just by copying the image to the project folder. The code is written in a very easy manner so as to make it feasible for an unknown purpose to understand easily.
