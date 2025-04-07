import streamlit as st

from modules import jaspar_api

# ---- STREAMLIT UI ----
st.set_page_config(
    initial_sidebar_state="collapsed"
)

st.title("JASPAR Transcription Factor Binding Site Scanner")

tf_name = st.text_input("Enter Transcription Factor Name (e.g., CTCF)")
selected_tf = None

if "search_clicked" not in st.session_state:
    st.session_state["search_clicked"] = False

if st.button("Search Transcription Factors"):
    st.session_state["search_clicked"] = True
    with st.spinner("Searching for transcription factors..."):
        st.session_state["motifs"] = jaspar_api.search_jaspar(tf_name)

if st.session_state["search_clicked"]:
    motifs = st.session_state.get("motifs", [])
    if motifs and (not tf_name == ""):
        tf_options = {f"{m['name']} ({m['matrix_id']})": m['matrix_id'] for m in motifs}
        selected_tf = st.selectbox("Select a Transcription Factor Binding Profile", list(tf_options.keys()), index=None)
        if not selected_tf == None:
            st.session_state["selected_tf_id"] = tf_options[selected_tf]
            st.write("**You selected:**", selected_tf)
            if st.button("Find Transcription Factor"):
                st.switch_page("pages/binding_site_score.py")
        else:
            st.write("**You selected:**", selected_tf)
    elif (tf_name == ""):
        pass
    else:
        st.error("No transcription factors found. Try another name.")