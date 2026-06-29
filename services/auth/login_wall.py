import streamlit as st
from services.persistence.exercise_repository import get_or_create_user


def render_login_wall():
    if st.session_state.get("user_id") is not None:
        return True

    st.markdown("""
    <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 0.4rem;">
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#FFFFFF" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
            <path d="M6 5v14"/><path d="M18 5v14"/><path d="M2 9v6"/><path d="M22 9v6"/><path d="M6 12h12"/>
            <rect x="4" y="7" width="2" height="10" rx="1"/><rect x="18" y="7" width="2" height="10" rx="1"/>
            <rect x="1" y="10" width="2" height="4" rx="1"/><rect x="21" y="10" width="2" height="4" rx="1"/>
        </svg>
        <span style="font-size: 2rem; font-weight: 600; letter-spacing: -0.5px; color: #FFFFFF;">AI Real-time GYM Trainer</span>
    </div>
    <p style="font-size: 0.72rem; letter-spacing: 0.12em; text-transform: uppercase; color: rgba(255,255,255,0.35); margin-bottom: 2rem;">Your personal AI-powered fitness coach</p>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        username = st.text_input("Name (unique)", placeholder="e.g. Rohitha Panchamukhi")
        submit_button = st.form_submit_button("Start Session", width="stretch")

    if submit_button:
        if not username:
            st.error("Name cannot be empty.")
            return False
        
        user = get_or_create_user(username)
        st.session_state["user_id"] = user["id"]
        st.session_state["username"] = user["username"]
        st.rerun()

    return False