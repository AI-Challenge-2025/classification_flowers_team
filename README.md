# classification_flowers
# โครงการทำนายดอกไม้ 3 ชนิดจากภาพ

โปรเจคนี้มีวัตถุประสงค์เพื่อสร้างโมเดลทำนายชนิดของดอกไม้จากรูปภาพ โดยมี 3 คลาสของดอกไม้ และสร้าง UI สำหรับให้ผู้ใช้สามารถอัปโหลดภาพเพื่อดูผลการทำนายได้

ภาพรวมโปรเจค
โปรเจคนี้เป็นระบบจำแนกประเภทของดอกไม้จากภาพถ่าย โดยใช้โมเดล Deep Learning ที่เทรนด้วย TensorFlow Keras เพื่อทำนายว่าในภาพเป็นดอกไม้ชนิดใด ระบบประกอบด้วย

FastAPI สำหรับทำ Backend API เพื่อรับภาพจากผู้ใช้ ทำนายผล และส่งผลลัพธ์กลับ

Streamlit สำหรับทำหน้าเว็บอินเทอร์เฟซที่ใช้งานง่าย เพื่อให้ผู้ใช้สามารถอัปโหลดภาพและดูผลทำนายได้ทันที



---

## ขั้นตอนการทำงานของโปรเจค

### 1. เตรียม Dataset
โหลดข้อมูลได้จากที่นี่
https://drive.google.com/drive/folders/19u11SVFik1lIB5f0tR2LZwg_bg_tYbJ7?usp=sharing

- ใช้ชุดข้อมูลภาพดอกไม้ 3 ชนิด (เช่น ดอกกุหลาบ,ดอกเดซี่, ดอกทานตะวัน)
- แบ่งข้อมูลเป็น 3 ชุด คือ
  - ชุดฝึกสอน (Training set) 70%
  - ชุดทดสอบ (Testing set) 20%
  - ชุดวาลิเดชัน (validation) 10%

### 2. การสร้างและเทรนโมเดล

- เลือก Dataset รูปภาพที่เป็นแบบให้นำมาใช้ได้ https://www.kaggle.com/datasets/imsparsh/flowers-dataset
- นำชุดข้อมูลฝึกสอนเข้าเทรนโมเดล เพื่อให้โมเดลเรียนรู้การจำแนกภาพแต่ละชนิดของดอกไม้
- ประเมินผลโมเดลด้วยชุดทดสอบ (Testing set) เพื่อวัดความแม่นยำ

### 3. บันทึกโมเดล

- เมื่อเทรนเสร็จ บันทึกโมเดลไว้ในไฟล์  `flowers_model.keras`

### 4. สร้าง User Interface (UI)

- สร้างหน้าเว็บหรือแอปที่ให้ผู้ใช้สามารถอัปโหลดภาพดอกไม้ได้
- เมื่อผู้ใช้ส่งภาพเข้ามา ระบบจะโหลดโมเดลที่บันทึกไว้มาใช้ทำนาย
- แสดงผลลัพธ์การทำนายว่าภาพนั้นเป็นดอกไม้ชนิดใด พร้อมแสดงความมั่นใจของโมเดล (เช่น ความน่าจะเป็น)
  
### 5. การติดตั้งและใช้งาน
การ download dataset ให้ download จาก lilk ที่ได้ทำการแปะไว้ จากนั้นทำการเทรนให้ได้โมเดลที่ต้องการ นำไปทำต่อที่ VS code 
ทำการ git clone https://github.com/AI-Challenge-2025/classification_flowers_team.git เปิดใน VS code แล้วนำเข้าโมเดลที่เราเทรนเสร็จแล้วมารัน

1. สร้าง virtual environment 
python
def hello():
    print("python -m venv venv")

**Windows**
python
def hello():
    print("venv\Scripts\activate")


**Linux/macOS**
python
def hello():
    print("source venv/bin/activate")

2. ติดตั้ง dependencies
python
def hello():
    print("pip install -r requirements.txt")

3. การรันโปรเจค
รัน FastAPI backend
python
def hello():
    print("uvicorn app:app --host 0.0.0.0 --port 8000 --reload")

ระบบจะรันที่ http://localhost:8000

Endpoint สำหรับทำนายคือ POST /predict

รัน Streamlit frontend
def hello():
    print("streamlit run streamlit_app.py")

หน้าเว็บจะเปิดในเบราว์เซอร์
ผู้ใช้สามารถอัปโหลดภาพดอกไม้และดูผลการทำนายได้ทันที
