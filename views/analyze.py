import streamlit as st
import pandas as pd
import altair as alt

# Tựa đề ứng dụng
st.title("File Upload and Data Analysis")

# Thêm chú thích giải thích
st.write(
    """
    **Welcome!** 
    Upload any CSV or Excel file here, and we will analyze the data for you.
    After uploading, you'll be able to view a preview of the data along with some basic statistics and visualizations like histograms and boxplots.
    """
)

# Tải lên file
uploaded_file = st.file_uploader("Upload your Excel or CSV file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Đọc dữ liệu từ file CSV hoặc Excel
    if uploaded_file.name.endswith("csv"):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # Hiển thị bảng dữ liệu
    st.subheader("Data Preview")
    st.dataframe(df)

    # Thống kê mô tả cơ bản
    st.subheader("Basic Data Statistics")
    st.write(df.describe())

    # Lựa chọn cột để phân tích biểu đồ
    columns = df.columns.tolist()
    selected_column = st.selectbox("Select column for analysis", columns)

    # Vẽ biểu đồ
    st.subheader(f"Histogram of {selected_column}")
    chart = alt.Chart(df).mark_bar().encode(
        x=selected_column,
        y='count()',
    ).properties(width=600, height=400)
    st.altair_chart(chart, use_container_width=True)

    # Hoặc vẽ biểu đồ boxplot để phân tích dữ liệu
    if df[selected_column].dtype in ['int64', 'float64']:  # Kiểm tra nếu là dữ liệu số
        st.subheader(f"Boxplot of {selected_column}")
        boxplot = alt.Chart(df).mark_boxplot().encode(
            y=selected_column
        ).properties(width=600, height=400)
        st.altair_chart(boxplot, use_container_width=True)
