from pathlib import Path 
import streamlit as st
from PIL import Image

# Define the base path to the images folder
#images = Path("images")


# Function to display each experience with added emojis for flair
def display_experience(company_logo, role, company_and_duration, location, description, skills):
    col1, col2 = st.columns([1, 4])  # Create two columns for layout
    with col1:  # Column for the logo
        st.image(company_logo, width=100)  # Adjust width as needed
    with col2:  # Column for the text
        st.subheader(f"{role} 💼")  # Added rocket emoji for excitement
        st.write(f"{company_and_duration} 🗓️")  # Calendar emoji for duration
        st.write(f"{location} 📍")  # Location pin emoji for location
        st.markdown(description)
      # Light bulb emoji for skills
        st.markdown(f"🛠️{skills}")


# Function to display each study experience
def display_study(logo, degree, university, duration, description):
    col1, col2 = st.columns([1, 4])  # Create two columns for layout
    with col1:  # Column for the logo
        st.image(logo, width=100)  # Adjust width as needed
    with col2:  # Column for the text
        st.subheader(f"{degree} at {university} 🎓")
        st.write(f"{duration} 🗓️")
        st.markdown(description)

def education():
    st.write('\n')
    st.title("Education")
    

    # ENSAI

    with st.expander("Master for Smart Data Science, ENSAI, Rennes"):
        display_study(
            "images/Ensai.png",
            "🎓 Master for Smart Data Science",
            "ENSAI",
            "Sep 2025 - Sep 2026",
            """
            This international Master's program, fully taught in English, combines advanced statistics, 
            applied mathematics, and computer science to analyze massive and heterogeneous data and to 
            develop strong expertise in artificial intelligence.
            Key Areas of Study:
            - Statistical modeling
            - Algorithms
            - Data management
            - Machine learning
            - Modern AI methods.     

            🌍 **The Master for Smart Data Science ranked 5th in Eduniversal's 2025 “Best French Master's in Big Data & Data Science” Ranking.**
               """,
            
        )
    
        # Digisport
    with st.expander("MSc STAPS in Digital and Sport Science (EUR Digisport), Rennes"):
        display_study(
            "images/Digisport.jpg",
            "🎓 Master's in Digital and Sport Science (EUR Digisport), Rennes",
            "University of Rennes 2",
            "Sep 2022 - Jul 2024",
            """
            Master's Program: Digital Sciences and Sport
            The digital revolution in sports has created a demand for interdisciplinary specialists with skills at the intersection of sports science, computer science, data science, electronics, and social sciences.
            This research and innovation-driven masters program aims to train professionals capable of:
            - Understanding the challenges of the digital transformation in sports across all dimensions, including performance, health, and accessibility for all.
            - Developing a comprehensive understanding of the key scientific and technical issues related to the integration of new technologies in sports and physical activity, as well as the structural changes and innovations they bring.
            - Mastering advanced concepts, methods, tools, and technologies driving current developments in the field, with a strong emphasis on data science and its applications in sports.
             """
        )

    # Paris Saclay
    with st.expander("First Year of MSc STAPS in Engineering and Human Movement Sciences, Orsay"):
        display_study(
            "images/Paris saclay.png",
            "🎓 First Year of MSc STAPS in Engineering and Human Movement Sciences",
            "University of Paris Saclay",
            "Sep 2021 - Jun 2022",
            """
            Master's Program: Human Movement Sciences and Engineering
            This program combines expertise in human movement sciences and engineering to design systems where humans are integrated, such as human-machine interfaces, cobotics, and assistive robotics.
            Key Areas of Study:
            - Engineering Sciences: Systems approaches, bio-inspired robotics, assistive robotics.
            - Human Movement Sciences: Perception-action, motor control, musculoskeletal modeling.
            - Technical Skills: Matlab/Simulink programming, OpenSim simulation.
            - Professional Skills: Project management, team leadership, ergonomics, and industry exposure.      
               """,
            
        )

    # Licence STAPS
    with st.expander("BSc STAPS in Sports Ergonomics and Athletic Performance"):
        display_study(
            "images/Rennes 2.jpg",  # Replace with the path to your logo
            "Bachelor's degree, Sports Ergonomics and Athletic Performance",
            "University of Rennes 2",
            "Sep 2019 - Jun 2021",
            """      
            """,
        )

def experience():
    st.write('\n')
    st.title("Experience")

    with st.expander("📊⚽ Stade Rennais FC Internship - Data Analyst"):
        display_experience(
            "images/SRFC.jpg",  # Replace with the path to your logo
            "Stade Rennais FC Internship - Data Analyst",
            "Internship Duration : Jan 2024 - Jun 2024",
            "Stade Rennais Training Center, Rennes, · On-site",
            """
            📄 [View Recommendation Letter](https://drive.google.com/file/d/1ogJ5hP-V_mqHkpwu0z1E5LuXkkusTRKd/view?usp=drive_link)
            * Updating Power BI dashboards with data from : 
                - GPS tracking devices
                - Video analysis software
                - Psychological questionnaires
            * Initiating the development of a machine learning model to estimate injury risk.
            * Assisting the sports science team in implementing physical tests.

            """,
            "Rstudio, Power BI, Data Analysis, Machine Learning, GPS data, Sports Science, Physical Testing",
        )


    with st.expander("🏋️📰 M2S Laboratory Internship - Research Sport Scientist"):
        display_experience(
        "images/M2S.jpg",
        "Physiological Researcher",
        "Internship Duration: Feb 2023 - Jun 2023 and Jan 2024 - Jul 2024 (1 year)",
        "M2S (Mouvement Sport Santé) Laboratory,  Bruz · On-site",
        """
        📄 [View Recommendation Letter](https://drive.google.com/file/d/1M7JOEiVB7_ZmWppsesbsVA6GqaDXeGg8/view?usp=drive_link)
        * In my research, I examined the relationship between maximal fat 
          oxidation and match performance using GPS data. My article, 
          "Maximal Fat Oxidation Impacts High-Intensity Running During Soccer Matches: Lessons from a Retrospective Study in Elite Soccer Players," 
          is currently under review for publication in a sports science journal.
        * Master Thesis : [Maximal Fat Oxidation Impacts High-Intensity Running During Soccer Matches: Lessons from a Retrospective Study in Elite Soccer Players](https://drive.google.com/file/d/1yGoOl_K_lRDji14F-EZM5xM375najoPj/preview)
        """,
        "Scientific writing, Rstudio, Data Analysis, Preprocessing, Physiology, Research",
    )


    with st.expander("🏋️📰 iKinesis & CIAMS Laboratory Internship, Research Sport Scientist"):
        display_experience(
        "images/Ciams.jpg" ,
        "Biomechanical Researcher",
        "Internship Duration: April 2021 - June 2021 (3 months)",
        " CIAMS (Complexité, Innovation, Activités Motrices et Sportive) Laboratory, University of Paris-Saclay, Orsay · On-site",
        """
        * Analysis of the Correlation Between Spatio-Temporal and Kinematic Parameters in Running
        * Conducted in-depth research for a university thesis on running mechanics.
        * Collected, processed, and analyzed data to explore the relationship between spatio-temporal and kinematic parameters.
        * Authored a detailed research dissertation, showcasing findings and methodological approaches.
         """,
         "Scientific writing, Matlab, Data Analysis, Preprocessing, Biomechanics, Research", 
    )
        

def set_sidbar():
    with st.sidebar:
        # Ajout de la photo en haut de la barre latérale
        profile_pic = Image.open("images/Me.jpg")  # Remplacez "images/Me.jpg" par le chemin réel de votre photo
        st.image(profile_pic, caption="Pierre Hernot")#, use_container_width=True)
        st.title("SUMMARY")
        st.subheader("""
Currently enrolled in the Master for Smart Data Science at ENSAI (Rennes), I am seeking a 4- to 6-month internship starting in March 2026. My background includes a Master’s degree in Digital Sciences and Sport (EUR Digisport), where I specialized in data science. Initially focused on sports applications, I am now eager to apply my skills more broadly, particularly in areas such as healthcare, the environment, where data-driven approaches can generate meaningful contributions to society.
        """)

        st.write("\n \n ")
        st.title("LANGUAGES")
        st.progress(70 , "🇬🇧 English")
        st.progress(100 , "🇫🇷 French")
  

        st.write("\n \n ")
        st.title("extracurricular activities")
        st.markdown("""
                * ⚽ Regional-Level Soccer Player (SC Morlaix).
                * 🍿 Thought-provoking dramas and psychological stories.
                * 🌍 Strong interest in geopolitics and global conflicts.
                    """)



def skills():
    # --- SKILLS ---
    st.write('\n')
    
    # Adding a title for the skills section with an emoji
    st.title('Skills')

    # Embedding badges in Markdown
    badges = """
    [![Python](https://img.shields.io/badge/-Python-3776AB?style=for-the-badge&logo=python&logoColor=white&logoSize=2)](#)
    [![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)](#)
    [![TensorFlow](https://img.shields.io/badge/-TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white&logoSize=2)](#)
    [![scikit-learn](https://img.shields.io/badge/-scikit%20learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white&logoSize=2)](#)
    [![Keras](https://img.shields.io/badge/-Keras-D00000?style=for-the-badge&logo=keras&logoColor=white&logoSize=2)](#)
    [![NumPy](https://img.shields.io/badge/-NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white&logoSize=2)](#)
    [![Pandas](https://img.shields.io/badge/-Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white&logoSize=2)](#)
    [![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white&logoSize=2)](#)
    [![Seaborn](https://img.shields.io/badge/-Seaborn-4E5180?style=for-the-badge&logo=python&logoColor=white&logoSize=2)](#)
    [![json](https://img.shields.io/badge/-json-000000?style=for-the-badge&logo=json&logoColor=white&logoSize=2)](#)
    [![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=for-the-badge&logo=Jupyter&logoColor=white&logoSize=2)](#)
    [![Github](https://img.shields.io/badge/-GitHub-181717?style=for-the-badge&logo=github&logoColor=white&logoSize=2)](#)
    [![React](https://img.shields.io/badge/-React-61DAFB?style=for-the-badge&logo=react&logoColor=white&logoSize=2)](#)
    [![R](https://img.shields.io/badge/-Rstudio-276DC3?style=for-the-badge&logo=R&logoColor=white&logoSize=2)](#)
    [![Shiny](https://img.shields.io/badge/-Shiny-276DC3?style=for-the-badge&logo=R&logoColor=white&logoSize=2)](#)
    [![Matlab](https://img.shields.io/badge/-Matlab-0076A8?style=for-the-badge&logo=mathworks&logoColor=white&logoSize=2)](#)
    [![SQL/Mysql](https://img.shields.io/badge/-SQL/Mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white&logoSize=2)](#)
    """


    # Adding badges to the Streamlit app
    st.markdown(badges)


def projects():
    # --- Projects & Accomplishments ---

    Data_Viz = {
        "🏅 R Shiny App": "https://github.com/PierreHernt/Application-Shiny-Visualisation-des-Jeux-Olympiques",
        "⚛ React App": "https://github.com/PierreHernt/my-map-app",

    }
    Data_Viz_descreption = {
        "🏅 R Shiny App": "Create an R Shiny application focused on sports science to visualize specific data.",
        "⚛ React App": "Develop a React application to visualize and assess the accessibility of healthcare services in French communes.",
    } 

    ML = {
        "🎾 Classification of Tennis Stroke Types": "https://github.com/PierreHernt/MachineLearning-Classification-de-types-de-coups-au-Tennis",
        
    }
    ML_descreption = {
        "🎾 Classification of Tennis Stroke Types" : "Classification of Tennis Stroke Types (Time-Series Data from Accelerometer and Gyroscope) with Machine Learning (Rstudio). ",
    }

    DL = {
        "🔗 Classification of Tennis Stroke Types": "https://github.com/PierreHernt/DeeplLearning-Classification-de-types-de-coups-au-Tennis",
    }

    DL_descreption = {
        "🔗 Classification of Tennis Stroke Types" : "Classification of Tennis Stroke Types (Time-Series Data from Accelerometer and Gyroscope) with Deep Learning (Python).",
    }
    
     
    st.write('\n')
    st.title("Projects")
    st.write("---")
    
    
    tab1 , tab2 , tab3= st.tabs(["Data Visualisation" , "Machine learning" , "Deep Learning"])

    with tab1:
        for project, link in Data_Viz.items():
            with st.expander(project):
                st.subheader(project)
                st.markdown(Data_Viz_descreption[project])
                st.link_button("visite in GitHub 🌐" , link)

    
    with tab2:
        for project, link in ML.items():
            with st.expander(project):
                st.subheader(project)
                st.markdown(ML_descreption[project])
                st.link_button("visite in GitHub 🌐" , link)

    with tab3:
        for project, link in DL.items():
            with st.expander(project):
                st.subheader(project)
                st.markdown(DL_descreption[project])
                st.link_button("visite in GitHub 🌐" , link)




def certaficate():
    def display_certificate(image_path, name, issuer, date ):
        col1 , col2 = st.columns(2)
        with col1:
            st.image(image_path, caption=name)#, use_container_width=True)
        with col2:
            st.subheader(name)
            st.write(f"**Issuer:** {issuer}")
            st.write(f"**Date Earned:** {date}")
  

    # Replace these with your actual certificate data
    certificates_data = [
        {"image_path": "images/Toeic.jpg", "name": "Toeic Listening and Reading comprehension", "issuer": "ETS", "date": "Nov 2024"},        
        # Add more certificates as needed
    ]

    st.title("My Certificate")

    for certificate in certificates_data:
        display_certificate(certificate["image_path"], certificate["name"], certificate["issuer"], certificate["date"])





def main():

    # --- PATH SETTINGS ---
    current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
    css_file = current_dir / "styles" / "main.css"
    resume_file = current_dir / "pdf" / "Pierre_Hernot__Data_Scientist.pdf"
    profile_pic = current_dir / "images" / "Me.jpg"

    # --- GENERAL SETTINGS ---
    PAGE_TITLE = "Digital CV | Pierre Hernot"
    PAGE_ICON = "assets/Icone.png"
    NAME = "Pierre Hernot"
    DESCRIPTION = """
    Digital and Sport Science MS Graduate | EUR Digisport 
    """
    EMAIL = "pierhernot@gmail.com"
    
    st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON , layout="wide")
    
    # --- set the bar side ---
    set_sidbar()
    

    # --- LOAD PDF & PROFIL PIC ---
    with open(resume_file, "rb") as pdf_file:
        PDFbyte = pdf_file.read()


    # --- Hero section ---

    col1,col2 = st.columns([3,1])
    
    with col1:
        st.title(NAME)
        st.subheader(DESCRIPTION)
    
    with col2:
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.write('\n')
        st.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )  # Bouton de téléchargement du CV

    
    # Ajouter les éléments côte à côte (email, LinkedIn, GitHub) sur la même ligne
    st.markdown(
        f"""
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="font-size: 16px;">
                📫 <a href="mailto:pierhernot@gmail.com" style="text-decoration: none; color: #1a73e8;">pierhernot@gmail.com</a>
            </div>
            <div>
                <a href="https://www.linkedin.com/in/pierrehernot" target="_blank">
                    <img src="https://img.shields.io/badge/-LinkedIn-blue?logo=linkedin&style=flat-square" alt="LinkedIn">
                </a>
            </div>
            <div>
                <a href="https://github.com/PierreHernt" target="_blank">
                    <img src="https://img.shields.io/badge/-GitHub-black?logo=github&style=flat-square" alt="GitHub">
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


    
    # --- Experience section---
    experience()

    # --- Education section---
    education()

    # ---skills section ---
    skills()

    # ---Project section ---
    projects()

    certaficate()



if __name__ == "__main__":
    main()

