from pathlib import Path
import sys
import cv2
import depthai as dai
import numpy as np
import time


pipeline = dai.Pipeline()

# color camera

cam_rgb = pipeline.createColorCamera()
cam_rgb.setPreviewSize(800, 600)
cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
cam_rgb.setInterleaved(False)
cam_rgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.RGB)

xout_rgb = pipeline.createXLinkOut()
xout_rgb.setStreamName("rgb")
cam_rgb.preview.link(xout_rgb.input)


# depth camera

left = pipeline.createMonoCamera()
left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
left.setBoardSocket(dai.CameraBoardSocket.LEFT)

right = pipeline.createMonoCamera()
right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
right.setBoardSocket(dai.CameraBoardSocket.RIGHT)

depth = pipeline.createStereoDepth()
depth.setConfidenceThreshold(200)
# Note: the rectified streams are horizontally mirrored by default
depth.setOutputRectified(True)
depth.setRectifyEdgeFillColor(0) # Black, to better see the cutout
left.out.link(depth.left)
right.out.link(depth.right)

xout_depth = pipeline.createXLinkOut()
xout_depth.setStreamName("depth")
depth.disparity.link(xout_depth.input)


# Pipeline defined, now the device is connected to
with dai.Device(pipeline) as device:
    # Start pipeline
    device.startPipeline()

    r_color = device.getOutputQueue(name="rgb", maxSize=8, blocking=False)
    q_depth = device.getOutputQueue(name="depth", maxSize=8, blocking=False)

    frame_depth = None
    frames = 0

    start_time = time.time()
    while True:
        in_color = r_color.tryGet()
        in_depth = q_depth.tryGet()

        if in_color is not None:
            cv2.imshow("color", in_color.getCvFrame())

        if in_depth is not None:
            frame_depth = in_depth.getData().reshape((in_depth.getHeight(), in_depth.getWidth())).astype(np.uint8)
            frame_depth = np.ascontiguousarray(frame_depth)
            frame_depth = cv2.applyColorMap(frame_depth, cv2.COLORMAP_PINK)
            cv2.imshow("depth", frame_depth)
            
        if cv2.waitKey(1) == ord('q'):
            break

        next_time = time.time()
        frames += 1
        if next_time - start_time >= 1 :
            print("fps", frames)
            frames = 0

