import streamlit as st
from utils import calculate_rot, brain_rot_tip

# Custom CSS for improved UI
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
        transition: background-color 0.5s;
    }
    h1 {
        color: #4f8bf9;
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        margin-top: 40px;
        letter-spacing: 2px;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    .stButton>button {
        background-color: #4f8bf9;
        color: white;
        border-radius: 8px;
        font-size: 18px;
        padding: 10px 24px;
        margin-top: 20px;
    }
    .stMetric {
        font-size: 24px;
        font-weight: bold;
        color: #333;
    }
    .rot-bar {
        height: 20px;
        background-color: #e0e0e0;
        border-radius: 8px;
    }
    .rot-fill {
        height: 100%;
        border-radius: 8px;
    }
    .brain-icon {
        font-size: 100px;
        text-align: center;
        animation: brain-animation 2s infinite alternate;
    }
    @keyframes brain-animation {
        0% {
            transform: scale(1);
            color: #4f8bf9;
        }
        100% {
            transform: scale(1.2);
            color: #f44336;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 **Brain Rot Meter: Are You on the Verge of Becoming a Meme Zombie?**")
st.write("👾 **Track your screen time and meme consumption today to see how much 'Brain Rot' you've accumulated!**\n\n"
         "⚡️ Find out if you’re still in control or if you’ve crossed the line into meme addiction territory. "
         "Let’s see if your brain needs a recovery boost or a well-deserved break! 🚀")

col1, col2 = st.columns(2)
with col1:
    hours = st.slider("🕒 Hours scrolled today:", 0, 10, 0)
with col2:
    memes = st.slider("📱 Memes watched today:", 0, 20, 0)

if st.button("🎮 Calculate Brain Rot"):
    rot_score = calculate_rot(hours, memes)
    
    # Change background color based on rot score
    if rot_score < 30:
        st.markdown('<style>.main { background-color: #a5d6a7; }</style>', unsafe_allow_html=True)
    elif rot_score < 70:
        st.markdown('<style>.main { background-color: #fff176; }</style>', unsafe_allow_html=True)
    else:
        st.markdown('<style>.main { background-color: #ef5350; }</style>', unsafe_allow_html=True)

    # Display animated brain icon based on the score
    if rot_score < 30:
        st.markdown('<div class="brain-icon">🧠</div>', unsafe_allow_html=True)
        st.success("🧠 Your brain is in good shape!")
    elif rot_score < 70:
        st.markdown('<div class="brain-icon">🤯</div>', unsafe_allow_html=True)
        st.warning("🤯 Careful! Your brain is getting moldy!")
    else:
        st.markdown('<div class="brain-icon">🧟</div>', unsafe_allow_html=True)
        st.error("🧟 Your brain is officially rotten!")

    # Display the rot percentage with a progress bar
    st.subheader("Brain Rot Level")
    rot_percentage_color = 'green' if rot_score < 30 else 'yellow' if rot_score < 70 else 'red'
    st.markdown(f'<div class="rot-bar"><div class="rot-fill" style="width:{rot_score}%; background-color:{rot_percentage_color};"></div></div>', unsafe_allow_html=True)
    st.write(f"Your brain rot is at **{rot_score}%**")

    st.subheader("Today's Tip 📝")
    st.info(brain_rot_tip(rot_score))

    st.subheader("Today's Challenge 🎯")
    challenge = (
    "📚 Keep your screen time low tomorrow — perhaps dive into a short story, sketch something fun, or try a new hobby for 30 minutes!" if rot_score < 30 else
    "⏱ Reduce meme-watching by 3 memes and create your own hilarious meme, doodle a comic, or even write a quirky short story — let your creativity shine while giving your brain a break!" if rot_score < 70 else
    "🧠 Take a 20-minute brain-boosting break with something unique — solve a mystery puzzle, learn a magic trick, or even freestyle a fun rap about your day!"
    )
    st.warning(challenge)
