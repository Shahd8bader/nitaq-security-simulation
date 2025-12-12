# Nitaq Absher System
## نظام نطاق ابشر


**Nitaq** is an AI-powered security system designed to support real-time border monitoring using **YOLOv4 object detection**, **Drones** and **DepthAI cameras**.  
The system integrates digital-twin concepts with live object detection to help identify potential threats across desert, mountainous, and remote areas in Saudi Arabia.

نظام **نطاق** هو نظام أمني يعمل بالذكاء الاصطناعي، يعتمد على **YOLOv4**, **طائرات مسيرة** و **كاميرات الذكاء الاصطناعي** لرصد الأجسام في الوقت الحقيقي، مع دمج تقنيات **الديجيتال توين** لدعم مراقبة الحدود في المناطق الصحراوية والجبلية داخل المملكة العربية السعودية.

---

## Features | المميزات

- **YOLOv4 Real-Time Detection**  
  Fast and accurate detection of people, vehicles, and objects using your uploaded model files.
  
  رصد فوري ودقيق للأشخاص والمركبات باستخدام YOLOv4.

- **OAK-D DepthAI Integration**  
  High-quality depth + RGB video stream using DepthAI pipelines.

  دمج كاميرا OAK-D للحصول على فيديو وعمق بدقة عالية.

- **Digital Twin Connectivity**  
  The detections can be streamed into a digital-twin dashboard.

  إمكانية ربط نتائج الكشف بلوحة تحكم للتوأم الرقمي.

- **Secure Architecture**  
  Can run through government VPNs for safe field deployment.

  يمكن ربطه عبر VPN حكومي لضمان أعلى درجات الأمان.

---

## Project Files | ملفات المشروع

The repository expects the following files (already provided):

| File | Description |
|------|-------------|
| `yolov4.weights` | YOLOv4 pretrained weights |
| `yolov4.cfg` | YOLOv4 configuration file |
| `coco.names` | Object class labels |
| `python1.py` | Main script integrating YOLO + OAK-D DepthAI |

الملفات المطلوبة تم رفعها مسبقاً:  
- ملف الوزنات  
- ملف الإعدادات  
- أسماء الأصناف  
- سكربت بايثون الرئيسي

---

## Installation | التثبيت
bash
# Clone repo
git clone https://github.com/yourusername/nitaq-ai-security.git
cd nitaq-ai-security

# Install dependencies
pip install -r requirements.txt
`

> **Note:** OAK-D requires `depthai` installed.

> **ملاحظة:** كاميرا OAK-D تتطلب تثبيت مكتبة depthai.

---

## Running the System | تشغيل النظام

bash
python python1.py


This will:

1. Start the OAK-D RGB preview
2. Run YOLOv4 inference
3. Draw bounding boxes + labels
4. Display real-time detection

يقوم النظام بـ:

1. تشغيل كاميرا OAK-D
2. تنفيذ الكشف باستخدام YOLOv4
3. رسم الصناديق حول الأجسام
4. عرض الفيديو في الوقت الحقيقي

---

## Folder Structure | هيكل المشروع


Nitaq/
│
├─ python1.py          # Main AI pipeline
├─ yolov4.weights      # Model weights
├─ yolov4.cfg          # Model config
├─ coco.names          # Label names
├─ README.md           # Project documentation
└─ data/               # (Optional) maps, twin files, sensor logs


---

## Next Steps | الخطوات القادمة

* Integrate detections into a **Digital Twin dashboard**
  ربط نتائج الرصد بمنصة **توأم رقمي**

* Add **GPS + Telemetry** for field deployment
  إضافة بيانات الـ GPS لربط الكاميرا بالموقع الحدودي

* Use **thermal cameras / PTZ / drones** in future phases
  ربط النظام بكاميرات حرارية ودرونز في المراحل القادمة


```
