# Assignment 1

## Question 1 

To calibrate the camera, I have used a 8x6 checkerboard pattern. The code to take 10 images of the checker board using both the monochrome (left and right) and color cameras can be found in the file q1.ipynb

The images captured can found in the folder 'images'.

The images are then used for calculating the camera matrix, translation and rotational vectors. 

The corrected images are found in the 'images' folder and the corresponding camera values are stored in their respective folders (left, right and color).

<p float="left">
  <img src="./images/left/16648398145492.png" width="200" />
  <img src="./images/left/16648398145492_corners.png" width="200" /> 
  <img src="./images/left/16648398145492_result.png" width="200" /> 
</p>

<hr />

## Question 2

The camera matrix, rotational matrix and translation matrix which were stored in the above step are used to calculate translate the image coordinate to world coordinate.

two pixel coordinates (whose distance we want to measure) are chosen from an image and are converted into world coordinate. The distance between these 3d points then determine the real world distance.

<hr />

## Question 3 

In this question, I was successfully able to simultaneously display the live depth map and the color camera feed while displaying the frame rate in the terminal. I was able to reach frame rates of upto 30 Frames per second on my computer for the rbg camera.

<hr />

## Question 4 

For q4, we have to use the caliberation code provided to us by the depth ai team. Since we are using "Oak D Lite", we need to download the sdk from the "depthai-lite" branch on github.

All the required files and directories can be found in "q4"

Once downloaded, we can run the "install_requirements.py" file to install all the reuired dependancies.

Once this is done, we can run the "caliberate.py" file to begin the calibration process.

The code prompts us to place the checker board in certain angles and orientations. Once the program completes execution, we get the camera matrix. 

We observe that the camera matrices are almost identical.