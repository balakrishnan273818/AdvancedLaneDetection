Height,Width = UndistortedImage.shape[:2]

# define source and destination points for transform
LeftTop = [(570,460)]
RightTop = [(710,460)]
LeftBottom = [(250,680)]
RightBottom = [(1050,680)]
ROI = 460
SourcePoints = np.float32([LeftTop,
                  RightTop, 
                  LeftBottom, 
                  RightBottom])
DestinationPoints = np.float32([(ROI,0),
                  (Width-ROI,0),
                  (ROI,Height),
                  (Width-ROI,Height)])

UnwarpedImage, TransformationMatrix, InverseTransformationMatrix = \
								unwarp(UndistortedImage,
								SourcePoints,
								DestinationPoints)

# Visualize unwarp
Figure, (Axis_1, Axis_2) = plt.subplots(1, 2, figsize=(20,10))
Figure.subplots_adjust(hspace = .2, wspace=.05)
Axis_1.imshow(UndistortedImage)
x_axis = [SourcePoints[0][0],SourcePoints[2][0],SourcePoints[3][0],SourcePoints[1][0],SourcePoints[0][0]]
y_axis = [SourcePoints[0][1],SourcePoints[2][1],SourcePoints[3][1],SourcePoints[1][1],SourcePoints[0][1]]
Axis_1.plot(x_axis, y_axis, color='#33cc99', alpha=0.4, linewidth=3, solid_capstyle='round', zorder=2)
Axis_1.set_ylim([Height,0])
Axis_1.set_xlim([0,Width])
Axis_1.set_title('Undistorted Image', fontsize=30)
Axis_2.imshow(UnwarpedImage)
Axis_2.set_title('Unwarped Image', fontsize=30)

print('Undistorted Successfully...!')