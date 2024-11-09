import streamlit as st

# --- PAGE SETUP ---
about_page = st.Page(
    "views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",  # Thay đổi icon ở đây
    default=True,
)
project_1_page = st.Page(
    "views/sales_dashboard.py",
    title="Skill",
    icon=":material/bar_chart:",  # Thay đổi icon ở đây
)
project_2_page = st.Page(
    "views/chatbot.py",
    title="Chat Bot",
    icon=":material/smart_toy:",  # Thay đổi icon ở đây
)

# project_32_page = st.Page(
#     "views/analyze.py",
#     title="Data Science",
#     icon=":material.analytics:",  # Thay đổi icon ở đây
# )

# project_33_page = st.Page(
#     "views/insight.py",
#     title="Analytics ",
#     icon=":material.insights:",  # Thay đổi icon ở đây
# )

project_32_page = st.Page(
    "views/analyze.py",
    title="Data Science",
    icon=":material/analytics:",  # Thay đổi icon ở đây
)

project_33_page = st.Page(
    "views/insight.py",
    title="Analytics ",
    icon=":material/insights:",  # Thay đổi icon ở đây
)

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page, project_32_page, project_33_page],
    }
)
 
# --- SHARED ON ALL PAGES ---
 
st.sidebar.markdown("Made with ❤️ by [Fun Software]()")

# --- RUN NAVIGATION ---
pg.run()
