import cv2

#to read image
img=cv2.imread("/Volumes/Dev T7/vscode/projects/Pythonvscode/cameraprojects/projects/tutorial/road.jpeg",cv2.IMREAD_COLOR)

#creating a GUI window to display an image on screen
cv2.imshow("Cute Kittens", img)
cv2.waitKey(0) #to wait screen

#To remove the GUI window
cv2.destroyAllWindows()