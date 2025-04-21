import streamlit as st

def about_me():
    
    # Title and subtitle
    st.markdown("""
        <div style='text-align: center'>
            <h1 style='font-size: 3em;'>👋 Hello, I'm Thiago F. Miranda</h1>
            <p style='font-size: 1.2em; color: gray;'>
                Data Scientist | Sports Analytics Enthusiast | Lifelong Learner
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Profile picture
    st.markdown(
    f"""
    <div style='text-align: center; margin-top: 20px;'>
        <img src='./app/static/img/me.jpg' width='200' style='border-radius: 50%; box-shadow: 0 4px 12px rgba(0,0,0,0.1);'>
    </div>
    """,
    unsafe_allow_html=True
)

    # About me section
    st.markdown("""
    ## 🧠 About Me

    I'm a data-driven problem solver passionate about turning raw data into meaningful insights.  
    With experience in **data analysis**, **machine learning**, and **interactive visualizations**, I thrive on building tools and models that make a difference.

    I'm currently working on projects related to **sports analytics**, especially focusing on **football match modeling** and **betting strategies** using Python and R.

    I'm also exploring topics like:
    - Probabilistic modeling
    - Interactive data storytelling
    - Computer adaptive testing

    ## 📫 Let's Connect

    - [LinkedIn](https://www.linkedin.com/in/thiiagofmiranda)
    - [GitHub](https://github.com/thiagofmiranda)
    - 📧 thiagofm.pa@gmail.com
    """)

    # Footer
    st.markdown("""
    <hr>
    <p style='text-align: center; font-size: 0.9em; color: gray;'>
        Built with ❤️ using Streamlit
    </p>
    """, unsafe_allow_html=True)
