import streamlit as st

# Page configuration
st.set_page_config(page_title="Dhruv Ahuja's Resume", layout="wide")

# Header
st.title("Dhruv Ahuja")
st.write("dhruv_ahuja@berkeley.edu | 925-639-7319 | [Github](Your-Github-URL) | [LinkedIn](Your-LinkedIn-URL) | Berkeley, CA")

# Education
st.header("Education")
st.write("""
UC Berkeley — Computer Science, Math — 3.9/4.0 (2021-2025)  
Relevant Coursework: Machine Learning, Artificial Intelligence, Optimization Models and Convex Optimization, Computer Architecture, Efficient Algorithms, Stochastic and Random Processes, Discrete Mathematics and Probability, Data Structures and Algorithms, Computer Programming, Quant Finance, Game Theory, Blockchain Development
""")
# Image for education - Place a path to an image or URL
st.image("path_to_your_education_image.jpg", caption="UC Berkeley")

# Organizations
st.header("Organizations")
st.write("""
- Computer Science Mentors
- Nova Consulting
- Men’s Club Soccer
- Phi Kappa Sigma Fraternity
""")
# Insert images for extracurricular activities
st.image("2242.jepg", caption="Men's Club Soccer at Cal")
st.image("f2684.jpeg", caption="Phi Kappa Sigma")
st.image("3771.png", caption="Nova Consulting")

# Experience
st.header("Experience")
st.subheader("Thrrive — Machine Learning, Software Engineering Intern (May 2023 - October 2023)")
st.write("""
- Deployed an application for yoga pose identification and form correction.
- Utilized TensorFlow, OpenCV, Numpy, and Pandas for development.
- Employed Google Compute Engine for performance optimization.
""")
# Image for experience
st.image("path_to_your_work_image.jpg", caption="Thrrive Internship")

# Personal Projects
st.header("Personal Project Highlights")
st.write("""
- **Handwritten Digit Machine Learning Classifier (RISC-V)**
- **Discrete Optimal Binary Decision Rule Calculator (Python)**
- **Scalar Kalman Filter (Python)**
- **Gitlet — Version Control System (Java)**
- **PCA, Low-Rank Approximation, Regression on Senate Data (Python)**
- **Wordle Bot (Python)**
- **Snake Game (C)**
""")
# Image for projects
st.image("path_to_your_project_image.jpg", caption="Project Highlights")

# Skills
st.header("Languages/Tools")
st.write("Python, Java, C, SQL, RISC-V(Assembly), C++, TensorFlow, Numpy, Pandas, Seaborn, Sklearn, Docker, REST")

# Interests
st.header("Interests")
st.write("Soccer, Weight Lifting, Poker, Chess, Comedy, Fifa, International Travel, Fusion Cuisine, Formula 1 Racing")

# Footer
st.write("© 2023 Dhruv Ahuja")
