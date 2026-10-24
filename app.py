
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

.glass-card {
    padding: 20px;
    border-radius: 18px;
    background: linear-gradient(145deg, rgba(31, 37, 69, .84), rgba(15, 20, 41, .92));
    border: 1px solid var(--line);
    box-shadow: 0 12px 30px rgba(0, 0, 0, .16),
                inset 0 1px 0 rgba(255, 255, 255, .045);
}

.metric {
    font-size: 1.35rem;
    font-weight: 800;
    letter-spacing: -.5px;
    margin-top: 5px;
}

.muted {
    color: var(--muted);
    font-size: .87rem;
}

.stTextInput input, .stTextArea textarea {
    background: rgba(9, 13, 30, .82) !important;
    border: 1px solid #30385d !important;
    border-radius: 12px !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #9b7bff !important;
    box-shadow: 0 0 0 1px #9b7bff !important;
}

.stSelectbox [data-baseweb="select"] > div {
    background: #11172c;
    border-color: #343c62;
    border-radius: 10px;
}

.stButton > button, .stDownloadButton > button {
    border-radius: 11px;
    font-weight: 700;
    min-height: 45px;
    border: 1px solid rgba(161, 135, 255, .5);
    transition: all .2s ease;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #7753e8, #426cf5, #329de8);
    color: white;
    box-shadow: 0 5px 22px rgba(93, 88, 255, .23);
}

.stButton > button:hover, .stDownloadButton > button:hover {
    border-color: #8ad9ff;
    box-shadow: 0 0 22px rgba(91, 142, 255, .24);
    transform: translateY(-1px);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
    background: rgba(15, 20, 40, .8);
    padding: 8px;
    border: 1px solid #282f51;
    border-radius: 14px;
}

.stTabs [data-baseweb="tab"] {
    border-radius: 9px;
    padding: 10px 17px;
    background: transparent;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(100deg, #50349b, #244e94) !important;
}

div[data-testid="stExpander"] {
    background: rgba(18, 23, 45, .7);
    border: 1px solid #30365a;
    border-radius: 12px;
}

hr {
    border-color: rgba(139, 124, 255, .20);
}

footer {visibility: hidden;}

@media (max-width: 700px) {
    .hero {padding: 23px;}
    .hero h1 {font-size: 2rem;}
}
</style>
""", unsafe_allow_html=True)


# ---------- API KEY ----------
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    api_key = ""


# ---------- SIDEBAR ----------
with st.sidebar:
   
    st.image("logo.png.png", width=150)
    st.markdown("## CreatorFlow AI")

    st.markdown(
        '<p style="color:#9eabce;margin-top:-12px;">AI CONTENT STUDIO · V1.0</p>',
        unsafe_allow_html=True
    )
    st.divider()

    st.markdown("### ⚙️ Studio settings")

    mode = st.selectbox(
        "Content type",
        [
            "Full Content Pack",
            "Reel / Shorts Script",
            "Hooks & Titles",
            "Caption & Hashtags",
            "YouTube SEO Pack"
        ]
    )

    platform = st.selectbox(
        "Platform",
        ["YouTube", "YouTube Shorts", "Instagram Reels"]
    )

    language = st.selectbox(
        "Language",
        ["Hindi / Hinglish", "English"]
    )

    tone = st.selectbox(
        "Content style",
        [
            "Catchy and engaging",
            "Funny and relatable",
            "Educational and clear",
            "Storytelling",
            "Professional"
        ]
    )

    duration = st.selectbox(
        "Video duration",
        ["30 seconds", "60 seconds", "90 seconds", "3 minutes"]
    )

    st.divider()
    st.markdown("**✨ Built for creators**")
    st.caption("Ideas in. Content out.")


# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ YOUR CREATIVE ADVANTAGE</div>
    <h1>Ideas into content.<br>Creativity into momentum.</h1>
    <p>
        Your AI-powered workspace for scripts, hooks, captions and SEO.
        Built for creators who want to spend less time staring at a blank page.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------- DASHBOARD METRICS ----------
m1, m2, m3 = st.columns(3)

with m1:
    st.markdown("""
    <div class="glass-card">
        <div class="muted">✦ CONTENT STUDIO</div>
        <div class="metric">5 tools</div>
        <div class="muted">From ideas to SEO</div>
    </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
    <div class="glass-card">
        <div class="muted">◎ CREATOR LANGUAGES</div>
        <div class="metric">Hindi + English</div>
        <div class="muted">Made for your audience</div>
    </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
    <div class="glass-card">
        <div class="muted">⚡ YOUR WORKFLOW</div>
        <div class="metric">Idea → Content</div>
        <div class="muted">Generate and download</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")
st.markdown("### ✦ Create your next piece")
st.markdown(
    '<p class="muted">Start with a topic. Your AI studio will handle the first draft.</p>',
    unsafe_allow_html=True
)

# ---------- INPUT WORKSPACE ----------
with st.container(border=True):
    topic = st.text_input(
        "💡 Video topic",
        placeholder="e.g. 5 Python mistakes beginners make"
    )

    audience = st.selectbox(
        "🎯 Target audience",
        [
            "General audience",
            "Students",
            "Python beginners",
            "Content creators",
            "Gamers",
            "Working professionals"
        ]
    )

    script = st.text_area(
        "📝 Existing script or extra details (optional)",
        placeholder="Add your script, target audience, or extra instructions...",
        height=130
    )

    generate = st.button(
        "✨ Generate my content",
        type="primary",
        use_container_width=True
    )

# ---------- GENERATION ----------
if generate:
    if not topic.strip() and not script.strip():
        st.warning("Please enter a topic or paste a script first.")

    elif not api_key:
        st.error(
            "API key not found. Check your .streamlit/secrets.toml file."
        )

else:
    prompt = f"""
You are CreatorFlow AI, an expert content strategist for Hindi, Hinglish, and English creators.

Create useful, original content tailored to the selected platform, language, style, duration, topic, audience, and content type.

SCRIPT QUALITY:
- Start with a strong, truthful hook that grabs attention without misleading clickbait.
- Write natural spoken dialogue that sounds human, clear, and easy to say aloud.
- Match the selected duration realistically. For 30 seconds, target 60–75 spoken words; scale sensibly for other durations.
- Count only spoken dialogue, excluding titles, visuals, captions, and metadata.
- Use a clear hook, well-explained main points, and a relevant CTA when appropriate.
- Prefer 2–3 useful points explained properly over many rushed points.
- Keep spoken dialogue, visual directions, on-screen text, captions, and hashtags separate.

ACCURACY:
- Never invent facts, APIs, code behaviour, errors, or guarantees.
- For Python topics, explain concepts correctly and give simple, working examples when useful.
- Distinguish value comparison (==) from object identity (is).
- Explain indexing, assignment versus copying, shallow copies, and list modification accurately when relevant.
- If information is uncertain or context is missing, be transparent rather than guessing.

OUTPUT:
- Follow the selected content type and include only relevant sections.
- Make titles specific, descriptions useful, and hashtags relevant.
- If alternative hooks are useful, provide 3 short options: curiosity-driven, problem-focused, and relatable. Keep them separate from the main script.
- Use timestamps only when requested or helpful, with realistic pacing.
- Before responding, check factual accuracy, clarity, consistency, natural language, and duration.
- Never claim the script fits the duration unless the spoken word count supports that estimate.

CONTENT SETTINGS:
Target audience: {audience}
Content type: {mode}
Platform: {platform}
Language: {language}
Style: {tone}
Duration: {duration}
Topic: {topic}
Additional context or source script: {script}
"""

try:
    client = genai.Client(api_key=api_key)

    with st.spinner("✨ Creating your content..."):
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

            if response.text:
                st.session_state["creatorflow_result"] = response.text
                st.session_state["creatorflow_topic"] = (
                    topic.strip() or "Content from existing script"
                )
                st.session_state["creatorflow_mode"] = mode
                st.success("Your content is ready!")
            else:
                st.error("The AI returned no text. Please try again.")

        except Exception as e:
            st.error("Content generation failed.")
            st.caption(str(e))


# ---------- RESULTS ----------
if st.session_state.get("creatorflow_result"):
    result = st.session_state["creatorflow_result"]

    st.write("")
    st.markdown("### ✨ Your creation")
    st.markdown(
        f'<p class="muted">Topic: {st.session_state.get("creatorflow_topic", "")} '
        f'· {st.session_state.get("creatorflow_mode", "")}</p>',
        unsafe_allow_html=True
    )

    tab_output, tab_preview, tab_export = st.tabs(
        ["📝 Full output", "🔎 Review", "📥 Download"]
    )

    with tab_output:
        with st.container(border=True):
            st.markdown(result)

    with tab_preview:
        st.markdown("#### Review your content")
        st.caption(
            "Check the hooks, titles, script, captions and hashtags before publishing."
        )
        st.markdown(result)

    with tab_export:
                st.download_button(
            "📥 Download content (.txt)",
            data=result,
            file_name="creatorflow_content.txt",
            mime="text/plain",
            use_container_width=True
        )


    # ---------- REWRITE TOOL ----------


    st.write("")
    st.markdown("### ✨ Improve your content")

    rewrite_style = st.selectbox(
        "Choose an improvement",
        [
            "Make it more engaging",
            "Make it shorter",
            "Simplify the language",
            "Convert to natural Hinglish",
            "Add storytelling",
            "Improve the hook"
        ],
        key="rewrite_style"
    )

    if st.button("✨ Rewrite my content"):
        st.info("Rewrite Tool is ready for the next step!")
st.write("")
st.divider()
st.markdown(
    '<p style="text-align:center;color:#8793b5;font-size:.82rem;">'
    'CREATORFLOW AI · CREATE WITH INTENTION ✦</p>',
    unsafe_allow_html=True
)
