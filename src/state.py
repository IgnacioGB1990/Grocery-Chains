import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

class SessionState(object):
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

def get_session(key):
    session_state = getattr(get_report_ctx().session, "_session_state", None)
    if session_state is None:
        session_state = SessionState(**{key: None})
        setattr(get_report_ctx().session, "_session_state", session_state)
    if not hasattr(session_state, key):
        setattr(session_state, key, None)
    return getattr(session_state, key)

def set_session(key, value):
    session_state = getattr(get_report_ctx().session, "_session_state", None)
    if session_state is None:
        session_state = SessionState(**{key: None})
        setattr(get_report_ctx().session, "_session_state", session_state)
    setattr(session_state, key, value)

# Usage
set_session("name", "John")
name = get_session("name")
st.write("Name:", name)
