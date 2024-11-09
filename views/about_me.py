import streamlit as st
from forms.contact import contact_form  # Đảm bảo form được định nghĩa trong module 'forms.contact'

# --- HERO SECTION ---
# col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
col1, col2 = st.columns([1, 2], gap="small", vertical_alignment="center")
from forms.contact import contact_form


@st.dialog("Contact Me")
def show_contact_form():
    contact_form()
with col1:
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXJA32WU4rBpx7maglqeEtt3ot1tPIRWptxA&s", width=230)

with col2:
    st.title("Fun Software", anchor=False)
    st.markdown("**Your trusted partner for software solutions**")
    st.write("🚀 We specialize in building interactive, scalable, and efficient applications.")
    if st.button("✉️ Contact Us"):
        show_contact_form()

# Giới thiệu công ty
st.header("About Us")
st.write("""
    💼 **Fun Software** is a leading software development company specializing in building high-quality, user-centered software solutions. 
    We design and develop websites, mobile applications, enterprise tools, automation systems, and provide data analysis services using machine learning.
    🌟 We are passionate about creating innovative solutions that help businesses achieve their goals and enhance user experiences.
""")

# Dịch vụ của công ty
st.header("Our Services")
st.write("""
    - 💻 **Custom Software Development**: Tailor-made software solutions to meet your business needs.
    - 🌐 **Website and Web App Development**: Design and development of modern, responsive websites and web applications.
    - 📱 **Mobile App Development**: Creation of mobile applications for both Android and iOS platforms.
    - 🛠️ **Automation Tools**: Development of tools that automate manual processes to increase efficiency and productivity.
    - 🤖 **Machine Learning & Data Analysis**: Leveraging data and machine learning to provide insights and predictive models.
""")

# Kỹ năng của đội ngũ
st.header("Our Skills & Technologies")
st.write("""
    - 💻 **Programming Languages**: JavaScript, Python, HTML, CSS, TypeScript
    - 🌐 **Frontend**: React, Vue.js, Angular
    - 🛠️ **Backend**: Node.js, Express, Django, Flask, PHP
    - 🗄️ **Databases**: MySQL, MongoDB, PostgreSQL, SQLite
    - ⚙️ **Tools & Technologies**: Docker, Kubernetes, AWS, Azure, Git
    - 📊 **Data Science**: Machine Learning, Data Visualization, Pandas, Scikit-learn, TensorFlow
""")

# Kinh nghiệm làm việc
st.header("Our Experience")
st.subheader("Senior Web Developers | Fun Software")
 
st.markdown('<strong class="large-text">2022 - Present</strong>', unsafe_allow_html=True)
st.write("🔹 Led the development of automation tools and web applications as a team, focusing on streamlining workflows and improving efficiency.")
st.write("🔹 Worked collaboratively on architecting scalable web apps and utilizing containerization technologies (Docker, Kubernetes).")
 
st.markdown("""
    <style>
        .large-text {
            font-size: 1.6rem;  # Thay đổi giá trị này để tăng/giảm kích thước chữ
            font-weight: 800;  
        }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<strong class="large-text">2020 - 2022</strong>', unsafe_allow_html=True)
st.write("🔹 Lead the development of enterprise-grade applications and tools, ensuring scalability and performance.")
st.write("🔹 Architecting cloud-native applications and utilizing containerization technologies (Docker, Kubernetes).")
 
st.markdown('<strong class="large-text">2018 - 2020</strong>', unsafe_allow_html=True)
st.write("🔹 Contributed to web application development using React and Node.js.")
st.write("🔹 Collaborated in building automated systems to improve business workflows.")

st.markdown('<strong class="large-text">2016 - 2018</strong>', unsafe_allow_html=True)
st.write("🔹 Designed and developed CMS solutions using PHP, WordPress, Laravel, and other frameworks, ensuring flexibility and scalability for clients.")
st.write("🔹 Implemented custom features and optimized CMS platforms to meet business requirements and improve user experience.")
# Dự án nổi bật
st.header("Highlighted Projects")
st.write("""
    - 🌐 **E-commerce Web Application**: Developed a full-stack e-commerce platform with real-time inventory management.
    - 📈 **Analytics Dashboard**: Created a dashboard for data analysis and visualization, helping businesses make data-driven decisions.
    - 📱 **Mobile App for Fitness Tracking**: Designed and built a cross-platform mobile app for health and fitness tracking, integrated with APIs and wearable devices.
    - 🤖 **Automated Data Processing System**: Developed a machine learning-powered system for analyzing large datasets and making predictive models.
""")

# Thông tin thêm
st.header("Let's Connect!")
st.write("LinkedIn: [Fun Software](https://linkedin.com/company/fun-software)")
st.write("GitHub: [fun-software](https://github.com/fun-software)")
st.write("Website: [www.funsoftware.com](https://www.funsoftware.com)")

# --- Contact Form Function ---
@st.dialog("Contact Us")
def show_contact_form():
    contact_form()  # Giả sử form đã được định nghĩa trong module 'forms.contact'
