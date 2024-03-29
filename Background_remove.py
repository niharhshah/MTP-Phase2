import profile
import pyrealsense2 as rs
import numpy as np
import cv2
import os
pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.depth,1280,720,rs.format.z16,30)
config.enable_stream(rs.stream.color,1280,720,rs.format.bgr8,30)

profile = pipeline.start(config)

depth_sensor = profile.get_device().first_depth_sensor()
depth_scale = depth_sensor.get_depth_scale()
print("Depth Scale is: " , depth_scale)

clipping_distance_in_meters = 1 #1 meter
clipping_distance = clipping_distance_in_meters / depth_scale

align_to = rs.stream.color
align = rs.align(align_to)

filename = 0
pname = ""
while True:
    # Get frameset of color and depth
    frames = pipeline.wait_for_frames()
    # frames.get_depth_frame() is a 640x360 depth image
    # Align the depth frame to color frame
    aligned_frames = align.process(frames)
    # Get aligned frames
    aligned_depth_frame = aligned_frames.get_depth_frame() # aligned_depth_frame is a 640x480 depth image
    color_frame = aligned_frames.get_color_frame()
    # Validate that both frames are valid
    if not aligned_depth_frame or not color_frame:
        continue
    depth_image = np.asanyarray(aligned_depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    # Remove background - Set pixels further than clipping_distance to grey
    grey_color = 153
    depth_image_3d = np.dstack((depth_image,depth_image,depth_image)) #depth image is 1 channel, color is 3 channels
    bg_removed = np.where((depth_image_3d > clipping_distance) | (depth_image_3d <= 0), grey_color, color_image)
    # Render images:
    #   depth align to color on left
    #   depth on right
    depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
    images = np.vstack((bg_removed, depth_colormap))
    cv2.namedWindow('Align Example', cv2.WINDOW_NORMAL)
    cv2.imshow('Align Example', images)
    key = cv2.waitKey(1)
    # Press esc or 'q' to close the image window
    if key & 0xFF == ord('q') or key == 27:
        cv2.destroyAllWindows()
        break
    if key & 0xFF == ord('s'):
        os.chdir("Images")
        pname = "SavedImage" + str(filename) + ".png"
        cv2.imwrite(pname,bg_removed)
        filename+=1
        print("Saved",pname)
        os.chdir("..")