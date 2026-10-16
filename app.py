import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile

# Page Config
st.set_page_config(
    page_title="Smart Road Damage Detection",
    page_icon="🚧",
    layout="wide"
)

# Header
st.title("🚧 Smart Road Damage Detection System")

st.markdown("""
### AI-Powered Road Monitoring Platform

Upload a road image and our AI will:

- Detect road damage
- Analyze severity
- Generate inspection report
- Support government maintenance decisions
""")

st.divider()

uploaded_file = st.file_uploader(
    "📤 Upload Road Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.image(
            image,
            caption="Uploaded Road Image",
            use_container_width=True
        )

    if st.button("🔍 Detect Damage"):

        # Load YOLO Model
        model = YOLO("../runs/detect/train-3/weights/best.pt")

        # Save uploaded image temporarily
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        )

        image.save(temp_file.name)

        # Run prediction
        results = model(temp_file.name)

        result_img = results[0].plot()

        with col2:
            st.image(
                result_img,
                caption="Detection Result",
                use_container_width=True
            )

        st.success("✅ Road Damage Analysis Completed")

        st.divider()

        # Dashboard
        st.subheader("📈 Dashboard")

        d1, d2, d3, d4 = st.columns(4)

        d1.metric("Total Reports", "1250")
        d2.metric("Pending Repairs", "145")
        d3.metric("Completed Repairs", "1105")
        d4.metric("Critical Roads", "27")

        st.divider()

        # Detection Report
        st.subheader("📊 Detection Report")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Damage Type", "Road Crack")

        with c2:
            st.metric("Severity", "Medium ⚠️")

        with c3:
            st.metric("Confidence", "78%")

        st.warning("Medium Severity Damage Detected")

        st.divider()

        # GPS Location
        st.subheader("📍 GPS Location")

        latitude = "17.3850"
        longitude = "78.4867"
        area = "Hyderabad"

        st.info(f"""
Latitude : {latitude}

Longitude : {longitude}

Area : {area}
""")

        st.divider()

        # Report Generation
        st.subheader("📄 Damage Inspection Report")

        report = f"""
Road Damage Report

Road ID : RD-1025

Location : {area}

Latitude : {latitude}

Longitude : {longitude}

Damage Type : Road Crack

Severity : Medium

Status : Submitted
"""

        st.text_area(
            "Generated Report",
            report,
            height=220
        )

        st.download_button(
            "📥 Download Report",
            data=report,
            file_name="Road_Damage_Report.txt"
        )

        st.divider()

        # Government Notification
        st.subheader("🏛 Government Notification")

        st.success(
            "Report Successfully Sent To GHMC Road Maintenance Department"
        )

        st.divider()

        # Repair Tracking
        st.subheader("🛠 Repair Tracking")

        status = "Under Review"

        st.write("Current Status :", status)

        st.progress(60)

        st.write("Repair Progress : 60%")

        st.divider()

        # Future Workflow
        st.subheader("🚀 Future Workflow")

        st.code("""
Citizen Uploads Image
        ↓
AI Detects Crack
        ↓
Severity Score
        ↓
GPS Location
        ↓
Report Generation
        ↓
Government Notification
        ↓
Repair Tracking
""")

        st.success("🎉 Smart Road Damage Detection Process Completed")