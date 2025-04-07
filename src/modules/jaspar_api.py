import streamlit as st
import requests
from constants import JASPAR_BASE_URL

# ---- JASPAR API FUNCTIONS ----
def search_jaspar(tf_name):
    """Search for transcription factor motifs by name."""
    try:
        response = requests.get(f"{JASPAR_BASE_URL}/?name={tf_name}&format=json")
        response.raise_for_status()
        motifs = response.json()
        return motifs["results"]
    except requests.RequestException as e:
        st.error(f"Error fetching data from JASPAR: {e}")
        return None

def fetch_jaspar_motif(jaspar_id):
    """Fetches motif matrix from JASPAR."""
    try:
        response = requests.get(f"{JASPAR_BASE_URL}/{jaspar_id}/?format=json")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Error fetching motif data from JASPAR: {e}")
        return None
