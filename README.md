# YOLOv8 Tracking + Counting (Video)

## 📌 Overview
This project demonstrates **object tracking and counting** using YOLOv8 segmentation model.  
The model assigns unique IDs to each detected object and counts how many unique instances appear across the video.

## 🚀 Features
- Tracks objects across frames with unique IDs  
- Counts unique instances of each class (e.g., number of people, cars)  
- Displays **real-time annotated video**  
- Saves processed video with annotations  

## 🛠️ Installation
```bash
git clone https://github.com/Suhail-Mahaboob/yolo-video-detection-tracking.git
cd yolo-video-detection-tracking
pip install -r requirements.txt
```

▶️ Usage
Run the script:

```bash
python track_count.py
```

* Replace "testt.mp4" with your own video path.
* Press Q to quit.

💾 Output
Annotated video is saved as result_tracking.mp4

Console logs:
- Current counts (updated per frame)
- Final counts after video ends

📂 Project Structure
```bash
Copy code
tracking_counting/
│── track_count.py         # Main script
│── requirements.txt       # Dependencies
│── README.md              # Documentation
│── testt.mp4              # Sample input video
```
📊 Example Console Output
> Current Counts: {'person': 1}
> Current Counts: {'person': 2}
> ...
> Final Counts: {'person': 3, 'car': 1}
