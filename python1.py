import depthai as dai
import cv2
import numpy as np

# Load YOLOv4
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

# Load class names
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Setup OAK pipeline
pipeline = dai.Pipeline()
cam = pipeline.createColorCamera()
cam.setPreviewSize(416, 416)
cam.setInterleaved(False)
cam.setBoardSocket(dai.CameraBoardSocket.RGB)

xout = pipeline.createXLinkOut()
xout.setStreamName("video")
cam.preview.link(xout.input)

# Run device
with dai.Device(pipeline) as device:
    queue = device.getOutputQueue("video", maxSize=1, blocking=False)
    while True:
        in_frame = queue.get()
        frame = in_frame.getCvFrame()

        # YOLOv4 detection
        blob = cv2.dnn.blobFromImage(frame, 1/255.0, (416, 416), swapRB=True, crop=False)
        net.setInput(blob)
        detections = net.forward(output_layers)

        h, w = frame.shape[:2]
        boxes, confidences, class_ids = [], [], []

        for detection in detections:
            for obj in detection:
                scores = obj[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]

                if confidence > 0.5:
                    center_x = int(obj[0] * w)
                    center_y = int(obj[1] * h)
                    bw = int(obj[2] * w)
                    bh = int(obj[3] * h)
                    x = int(center_x - bw / 2)
                    y = int(center_y - bh / 2)

                    boxes.append([x, y, bw, bh])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        # Non-max suppression
        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        # Draw bounding boxes and labels
        for i in indexes:
            i = i[0] if isinstance(i, (list, tuple, np.ndarray)) else i
            x, y, w_box, h_box = boxes[i]
            label = f"{classes[class_ids[i]]} {int(confidences[i]*100)}%"
            cv2.rectangle(frame, (x, y), (x + w_box, y + h_box), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

        # Display the result
        cv2.imshow("OAK-D + YOLOv4", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

cv2.destroyAllWindows()
