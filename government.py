import streamlit as st
import pandas as pd



st.set_page_config(
    page_title="Government Dashboard",
    page_icon="🏛️",
    layout="wide"
)
-----------------------------------------------

st.title("🏛️ SmartRoad AI - Government Dashboard")
st.caption("Road Damage Monitoring & Maintenance Management System")

st.divider()


# --------------------------------------------------

c1,c2,c3,c4,c5 = st.columns(5)

c1.metric("📨 Total Complaints","1250","+25")
c2.metric("🚨 Critical","27","+3")
c3.metric("🟠 Pending","145")
c4.metric("👷 Assigned","89")
c5.metric("✅ Completed","1016")

st.divider()

----------------------------------------------

col1,col2,col3=st.columns(3)

with col1:
    area=st.selectbox(
        "Select Area",
        ["All","Hyderabad","Kukatpally","Gachibowli"]
    )

with col2:
    severity=st.selectbox(
        "Severity",
        ["All","High","Medium","Low"]
    )

with col3:
    status=st.selectbox(
        "Status",
        ["All","Pending","Assigned","Completed"]
    )

st.divider()

-----------------------------------------------

st.subheader("🚧 Road Damage Complaints")

data=pd.DataFrame({

"Complaint ID":[
"RD1001",
"RD1002",
"RD1003",
"RD1004",
"RD1005"
],

"Location":[
"Hyderabad",
"Kukatpally",
"Gachibowli",
"Ameerpet",
"Miyapur"
],

"Damage":[
"Road Crack",
"Pothole",
"Road Crack",
"Edge Crack",
"Pothole"
],

"Severity":[
"Medium",
"High",
"Low",
"High",
"Medium"
],

"Status":[
"Pending",
"Assigned",
"Completed",
"Pending",
"Assigned"
]

})

st.dataframe(
    data,
    use_container_width=True
)

st.divider()

-----------------------------------------------

st.subheader("📄 Selected Complaint")

left,right=st.columns([1,2])

with left:

    st.image(
        "https://images.unsplash.com/photo-1541888946425-d81bb19240f5",
        use_container_width=True
    )

with right:

    st.write("### Complaint Information")

    st.write("Complaint ID : RD1002")
    st.write("Citizen Name : Rahul")
    st.write("Location : Kukatpally")
    st.write("Latitude : 17.494")
    st.write("Longitude : 78.399")
    st.write("Damage : Pothole")
    st.write("Severity : High")
    st.write("Date : 25 June 2026")

    st.progress(60)

    st.info("Current Status : Engineer Assigned")

st.divider()

# --------------------------------------------------
# EN
# --------------------------------------------------

st.subheader("👷 Engineer Assignment")

col1,col2,col3=st.columns(3)

col1.write("Engineer : Ravi Kumar")
col2.write("Department : GHMC")
col3.write("Vehicle : TS09AB1025")

st.success("Engineer Assigned Successfully")

st.divider()

# --------------------------------------------------

# --------------------------------------------------

st.subheader("🔔 Recent Notifications")

st.success("✔ Complaint RD1005 received")
st.info("✔ Engineer Assigned to RD1002")
st.warning("✔ High Severity Road Detected")
st.success("✔ Complaint RD0998 Completed")

st.divider()

# --------------------------------------------------

# --------------------------------------------------

st.subheader("📥 Generate Reports")

report="""
SMART ROAD AI REPORT

Complaint ID : RD1002

Location : Kukatpally

Damage : Pothole

Severity : High

Status : Assigned

Department : GHMC
"""

st.download_button(
    "📄 Download Report",
    report,
    file_name="Road_Report.txt"
)

st.divider()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.success("✅ Smart Road AI Government Dashboard Ready")