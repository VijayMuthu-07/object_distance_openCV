dark blue coloured rectangular object will be detected and distance of that object from the webcam will be returned.
it assumes you webcam as a pinhole camera and uses that formula on the countours from openCV to determine the distance.
it has to be caliberated for your webcam once to find the focal length of your webcam,
you can pass a calibration image to the caliberate function in the file.
