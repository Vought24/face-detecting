-----------------------------------------------------------------------------------------------------
FaceMesh Detector using MediaPipe and OpenCV
This project implements a Face Mesh Detector using MediaPipe and OpenCV. It captures video from a webcam and detects facial landmarks for up to two faces simultaneously, visualizing them on the video stream in real-time.

Features
Detects and visualizes face mesh landmarks on live webcam feed.
Supports up to 2 faces at once.
Displays real-time FPS (frames per second) on the video feed.
Stops the video stream on pressing the q key.
Installation
Clone the repository:


'''
git clone https://github.com/vought24/face-mesh-detector.git
'''
cd face-mesh-detector
Create and activate a virtual environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate  # For Windows, use: venv\Scripts\activate
Install the required dependencies:

bash

pip install opencv-python mediapipe
How to Run
Ensure that a webcam is connected to your machine (for most laptops, the built-in webcam is 0 by default).

Run the main script:

bash

python face_mesh_detector.py
A window will open showing the webcam feed with the detected facial landmarks. The FPS will be displayed in the top left corner.

Press the q key to exit the application.

Code Explanation
FaceMeshDetector Class
Initialization (__init__): Initializes the face mesh detector using MediaPipe, allowing for up to max_faces faces to be detected at once.

findFaceMesh: Processes an image to find facial landmarks. Converts the image from BGR to RGB, detects the landmarks, and draws them on the image.

Main Function
Captures the video feed from the webcam.
Uses FaceMeshDetector to detect face meshes in each frame.
Displays FPS in real-time.
Press q to quit.
Example Output
When the program is running, it will look like this:

(Replace with a screenshot)

Dependencies
Python 3.x
OpenCV
MediaPipe
License
This project is licensed under the MIT License - see the LICENSE file for details.

Contribution
Feel free to open issues or submit pull requests to improve the project.
