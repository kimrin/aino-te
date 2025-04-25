import streamlit as st
import random
import os

st.title("🎤 合いの手ボタン β")
st.write("押すと、合いの手が流れるよ！")

AITE_PATH = "audio/"
aite_files = [f for f in os.listdir(AITE_PATH) if f.endswith(".mp3") or f.endswith(".wav")]

if st.button("合いの手くれ！"):
    selected = random.choice(aite_files)
    st.audio(os.path.join(AITE_PATH, selected))
    st.success(f"🎧 Played: {selected}")
