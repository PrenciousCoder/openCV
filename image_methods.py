import cv2 # opening the opencv library]

#reading the image using imread() function
image=cv2.imread("/Volumes/Dev T7/vscode/projects/Pythonvscode/cameraprojects/projects/tutorial/road.jpeg")

#extracting height and width
h,w=image.shape[:2]

#display

print("height={},width={}".format(h,w))

#to extract RGB value =select a random picel by entering a height and width
(B,G,R)=image[100,100]
print("R={},G={},B={}".format(R,G,B))

#pass the channel to extract
B=image[100,100,0]
print("B={}".format(B))

#A region of interest (ROI) is a portion
#  of an image that you want to filter or perform some other operation on.

#calculating region of interest
roi=image[100:500,200:700]

#resizing the image
resize=cv2.resize(image,(800,800)) #aspect ratio is not maintained by this method

#To maintain aspect ratio

ratio=800/w
dim=(800,int(h*ratio))
#resizing the image
resize_aspect=cv2.resize(image,dim)


"""rotating the image"""

#finding the centre of the image
center=(w//2,h//2)
#generating a rotation matrix
matrix=cv2.getRotationMatrix2D(center,-45,1.0)
#performaing the affine transformation
rotated=cv2.warpAffine(image,matrix,(w,h))

"""Drawing a reactangel"""
#we are copying the original image
#as it is an in place operation
output=image.copy()
#using the reactangle() function to create a reactangle.
cv2.rectangle=cv2.rectangle(output,(1500,900),(600,400),(255,0,0),2)

"""Displaying text"""
#copy the original image
output=image.copy()

#adding the text using putText() function
text=cv2.putText(output,'OpenCV Demo',(500,500),cv2.FONT_HERSHEY_SIMPLEX,4,(255,0,0),2)