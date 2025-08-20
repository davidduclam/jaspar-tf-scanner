import streamlit as st
from modules import binding_site_finder, jaspar_api, pfm_pwm_converter
from constants import SVG_BASE_URL
from pages import results_viewer

st.set_page_config(
    layout="wide"
)

if "selected_tf_id" in st.session_state:
    
    motifs = st.session_state.get("motifs", [])
    jaspar_id = st.session_state["selected_tf_id"]
    motif_data = jaspar_api.fetch_jaspar_motif(jaspar_id)
    
    SVG_URL = f"{SVG_BASE_URL}/{jaspar_id}.svg"
    
    st.header("Information profile on " + motif_data['matrix_id'])
    st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
    col = st.columns((2, 3.5), gap='medium')
    
    with st.container():
        with col[0].container(border=True):
            st.subheader("Profile Summary")
            st.markdown("<hr style='margin-top: 2px; margin-bottom: 2px;'>", unsafe_allow_html=True)
            profile_col1, profil_col2 = st.columns((0.3, 0.7))
            with profile_col1:
                st.markdown("**Name:**")
                st.markdown("**Matrix ID:** ")
                st.markdown("**Class:**")
                st.markdown("**Family:**")
                st.markdown("**Collection:**")
                st.markdown("**Taxon**")
                st.markdown("**Species**")        
                    
            with profil_col2:
                st.text(motif_data['name'])
                st.text(motif_data['matrix_id'])
                st.text(motif_data['class'][0])
                st.text(motif_data['family'][0])
                st.text(motif_data['collection'])
                s = str(motif_data['tax_group'])
                st.text(s.capitalize())
                st.text(motif_data['species'][0]['name'])
            
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            st.markdown(f'<img src="{SVG_URL}"/>', unsafe_allow_html=True)
            st.markdown("<div style='margin-top: 20px;'></div>", unsafe_allow_html=True)
            if st.button("Retry", use_container_width=True, icon="🔁"):
                st.switch_page("app.py")
                    
        if motifs and motif_data:
            pwm = pfm_pwm_converter.pfm_to_pwm(motif_data["pfm"])

            with col[1].container(border=True):
                st.subheader("Binding Site")
                st.markdown("<hr style='margin-top: 2px; margin-bottom: 2px;'>", unsafe_allow_html=True)
                dna_sequence = st.text_area("Enter DNA Sequence (A, C, G, T)", "ATCGGCTAGCTAGCTGATCG")

                if st.button("Find Binding Sites", icon="🔎"):
                    results = binding_site_finder.scan_sequence(dna_sequence, pwm)
                    results_viewer.display_results(results)
