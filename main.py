import streamlit as st
import random as rd
massage=["すごい！","素晴らしい！","最高！","天才！","完璧！","尊敬する！","感動した！","神！","天才かよ！","やばい！","よしよしヾ(・ω・｀)","えらい！","天才すぎる！","すごすぎる！","やばすぎる！","神かよ！","尊敬するわ！","感動したわ！","完璧すぎる！","最高すぎる！","頑張ってんじゃーん!","明日も君なら頑張れるよー!",]
if "count" not in st.session_state:
    st.session_state.count = 0
st.title("ﾎﾒﾎﾒアプリ")
if st.button("ﾎﾒﾎﾒｰ"):
    st.session_state.count += 1
st.write(f"ﾎﾒﾎﾒｶｳﾝﾄ: {st.session_state.count}")
st.write(rd.choice(massage))