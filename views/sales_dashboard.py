import streamlit as st
import pandas as pd
import altair as alt

# Dữ liệu kỹ năng và công cụ cá nhân hoặc team
skills_data = {
    "Skill": [
        "HTML", "CSS", "JavaScript", "Vue.js", "React",    # Frontend
        "Python", "Node.js", "Django", "PHP", "SQL",       # Backend & Database
        "Docker", "AWS",                                    # DevOps
        "VBA",                     # Tool
        "Figma", "Canva", "Photoshop",                      # Design Tool
        "WordPress", "OctoberCMS", "Shopify"                # CMS
    ],
    "Proficiency (%)": [
        90, 85, 80, 75, 80,  # Frontend
        80, 75, 80, 80, 80,  # Backend & Database
        50, 60,              # DevOps
        80,      # Tool
        80, 85, 80,          # Design Tool
        80, 75, 85           # CMS
    ],
    "Category": [
        "Frontend", "Frontend", "Frontend", "Frontend", "Frontend",
        "Backend", "Backend", "Backend", "Backend", "Database",
        "DevOps", "DevOps",
        "Tool",
        "Design Tool", "Design Tool", "Design Tool",
        "CMS", "CMS", "CMS"
    ]
}

# Dự án và hình ảnh cho mỗi category với link đúng ngôn ngữ hoặc công nghệ
projects_data = {
    "Frontend": [
        {"name": "HTML Official", "image": "https://via.placeholder.com/150", "link": "https://html.spec.whatwg.org/", "description": "Official homepage for HTML."},
        {"name": "CSS Official", "image": "https://via.placeholder.com/150", "link": "https://www.w3.org/Style/CSS/", "description": "Official homepage for CSS."},
        {"name": "Vue.js", "image": "https://via.placeholder.com/150", "link": "https://vuejs.org/", "description": "Official Vue.js framework homepage."},
        {"name": "React", "image": "https://via.placeholder.com/150", "link": "https://reactjs.org/", "description": "Official React framework homepage."}
    ],
    "Backend": [
        {"name": "Python Official", "image": "https://via.placeholder.com/150", "link": "https://www.python.org/", "description": "Official Python homepage."},
        {"name": "Node.js", "image": "https://via.placeholder.com/150", "link": "https://nodejs.org/", "description": "Official Node.js homepage."},
        {"name": "Django", "image": "https://via.placeholder.com/150", "link": "https://www.djangoproject.com/", "description": "Official Django framework homepage."},
        {"name": "PHP", "image": "https://via.placeholder.com/150", "link": "https://www.php.net/", "description": "Official PHP homepage."}
    ],
    "Database": [
        {"name": "SQL Official", "image": "https://via.placeholder.com/150", "link": "https://www.mysql.com/", "description": "Official MySQL homepage."},
    ],
    "DevOps": [
        {"name": "Docker", "image": "https://via.placeholder.com/150", "link": "https://www.docker.com/", "description": "Official Docker homepage."},
        {"name": "AWS", "image": "https://via.placeholder.com/150", "link": "https://aws.amazon.com/", "description": "Official AWS homepage."}
    ],
    "Tool": [
        {"name": "VBA", "image": "https://via.placeholder.com/150", "link": "https://www.microsoft.com/en-us/microsoft-365/visual-basic-for-applications", "description": "VBA official page."}
    ],
    "Design Tool": [
        {"name": "Figma", "image": "https://via.placeholder.com/150", "link": "https://www.figma.com/", "description": "Official Figma homepage."},
        {"name": "Canva", "image": "https://via.placeholder.com/150", "link": "https://www.canva.com/", "description": "Official Canva homepage."},
        {"name": "Photoshop", "image": "https://via.placeholder.com/150", "link": "https://www.adobe.com/products/photoshop.html", "description": "Official Photoshop homepage."}
    ],
    "CMS": [
        {"name": "WordPress", "image": "https://via.placeholder.com/150", "link": "https://wordpress.org/", "description": "Official WordPress homepage."},
        {"name": "OctoberCMS", "image": "https://via.placeholder.com/150", "link": "https://octobercms.com/", "description": "Official OctoberCMS homepage."},
        {"name": "Shopify", "image": "https://via.placeholder.com/150", "link": "https://www.shopify.com/", "description": "Official Shopify homepage."}
    ]
}

# Tạo DataFrame từ dữ liệu kỹ năng
df = pd.DataFrame(skills_data)

# Tiêu đề và mô tả
st.title("Our Team's Skills and Toolset")

st.write("This dashboard provides an overview of the technical skills and tools expertise of our team.")

# Lựa chọn để hiển thị kỹ năng và công cụ theo từng nhóm
category_selected = st.selectbox("Filter by Category", options=["All", "Frontend", "Backend", "Database", "DevOps", "Tool", "Design Tool", "CMS"])

# Lọc dữ liệu theo category đã chọn
filtered_df = df if category_selected == "All" else df[df["Category"] == category_selected]

# Tạo biểu đồ thanh để hiển thị mức độ thành thạo từng kỹ năng và công cụ
chart = alt.Chart(filtered_df).mark_bar().encode(
    x=alt.X("Proficiency (%)", title="Proficiency Level"),
    y=alt.Y("Skill", sort="-x"),
    color="Category"
).properties(
    title="Skills and Tool Proficiency Level",
    width=600,
    height=400
)

# Hiển thị biểu đồ
st.altair_chart(chart, use_container_width=True)

# Hiển thị các dự án và hình ảnh của category đã chọn
if category_selected != "All":
    st.subheader(f"Projects and Examples for {category_selected}")
    
    # Tạo hai cột cho dự án
    columns = st.columns(2)
    
    # Duyệt qua các dự án trong category đã chọn và phân chia vào hai cột
    for i, project in enumerate(projects_data[category_selected]):
        col = columns[i % 2]  # Dự án sẽ được chia cho hai cột, sử dụng mod để luân phiên
        with col:
            st.markdown(f"[![{project['name']}]({project['image']})]({project['link']})")
            st.write(project["description"])

# Mô tả thêm để làm rõ kỹ năng và công cụ
st.write("**Skill and Tool Proficiency Levels**:")
for index, row in filtered_df.iterrows():
    st.write(f"{row['Skill']}: {row['Proficiency (%)']}% - {row['Category']}")
