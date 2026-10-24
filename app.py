
import streamlit as st
from google import genai

st.set_page_config(
    page_title="CreatorFlow AI",
    page_icon="logo.png.png",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- FUTURISTIC DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --bg: #080b18;
    --panel: rgba(21, 26, 49, 0.88);
    --line: rgba(139, 124, 255, 0.24);
    --purple: #9b7bff;
    --blue: #48b8ff;
    --muted: #a5b0ce;
}

.stApp {
    background:
        radial-gradient(ellipse at 12% 5%, rgba(111, 61, 220, .20), transparent 35%),
        radial-gradient(ellipse at 90% 15%, rgba(34, 143, 255, .14), transparent 30%),
        linear-gradient(145deg, #080b18, #0d1024 55%, #090d1c);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #11152a, #0b1020);
    border-right: 1px solid rgba(139, 124, 255, .25);
}

[data-testid="stSidebar"] h2 {
    letter-spacing: -1px;
}

.hero {
    position: relative;
    overflow: hidden;
    padding: 35px;
    border-radius: 25px;
    border: 1px solid rgba(167, 139, 250, .40);
    background:
        radial-gradient(ellipse at 90% 0%, rgba(72, 184, 255, .23), transparent 38%),
        linear-gradient(125deg, rgba(55, 36, 112, .92), rgba(20, 28, 60, .96) 58%, rgba(13, 21, 43, .98));
    box-shadow: 0 18px 55px rgba(65, 43, 155, .19),
                inset 0 1px 0 rgba(255, 255, 255, .10);
    margin-bottom: 28px;
}

.hero:after {
    content: "";
    position: absolute;
    width: 190px;
    height: 190px;
    right: -55px;
    top: -70px;
    border: 1px solid rgba(139, 124, 255, .55);
    border-radius: 50%;
    box-shadow: 0 0 35px rgba(116, 91, 255, .15),
                inset 0 0 30px rgba(72, 184, 255, .12);
}

.hero h1 {
    font-size: clamp(2rem, 4vw, 3rem);
    line-height: 1.15;
    letter-spacing: -1.7px;
    margin: 10px 0;
}

.hero p {
    color: #c5c9e8;
    font-size: 1rem;
    max-width: 650px;
}

.eyebrow {
    color: #9edbff;
    font-size: .76rem;
    font-weight: 800;
    letter-spacing: 2px;
    text-transform: uppercase;
}
