from ultralytics import YOLO
import cv2

model = YOLO("yolov8n-seg.pt")

cap = cv2.VideoCapture("testt.mp4")

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter("result_tracking.mp4", fourcc,fps,(width,height))

object_counts = {}

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.track(frame, persist = True)

    for r in results:
        annotated_frame = r.plot()

        if r.boxes is not None:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                class_name = model.names[cls_id]

                obj_id = int(box.id[0]) if box.id is not None else None
                if obj_id is not None:
                    if class_name not in object_counts:
                        object_counts[class_name] = set()
                    object_counts[class_name].add(obj_id)

    
    print("Current Counts: ", {cls: len(ids) for cls, ids in object_counts.items()})


    cv2.imshow("Tracking + Counting", annotated_frame)
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



cap.release()
out.release()
cv2.destroyAllWindows()

print("\nFinal Counts: ", {cls: len(ids) for cls, ids in object_counts.items()})



