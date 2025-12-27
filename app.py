import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Job Recommendation System",
    page_icon="💼",
    layout="centered"
)

st.title("💼 Job Recommendation System")
st.write("Select a job title to get similar job recommendations")

# ---------- LOAD DATA ----------
data_dict = pickle.load(open("Job_recom.pkl", "rb"))
similarity = pickle.load(open("job_similiar.pkl", "rb"))
data = pd.DataFrame(data_dict)

# ---------- CHECK COLUMNS ----------
# Uncomment this if needed for debugging
# st.write(data.columns)

# ---------- JOB SELECTION ----------
job_titles = sorted(data["jobtitle"].unique())

selected_job = st.selectbox("Choose a Job Title", job_titles)

# ---------- RECOMMEND BUTTON ----------
if st.button("🔍 Recommend Jobs"):
    job_index = data[data["jobtitle"] == selected_job].index[0]
    scores = similarity[job_index]

    recommendations = sorted(
        list(enumerate(scores)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    st.success("Recommended Jobs")

    for i in recommendations:
        st.markdown(
            f"""
            ### {data.iloc[i[0]]['jobtitle']}
            📍 **Location:** {data.iloc[i[0]]['joblocation_address']}
            ---
            """
        )
