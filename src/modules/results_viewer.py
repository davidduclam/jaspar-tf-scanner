import streamlit as st
import pandas as pd

# ---- DISPLAY RESULTS ----
def display_results(results):
    """Display binding site scores and plot the results."""
    st.subheader("Binding Site Scores")
    for pos, score in results:
        if score > 0: 
            st.write(f"Position **{pos}**: Score **{score:.2f}**")

    try:
        positions, scores = zip(*results)
        data = pd.DataFrame({
            'Position': positions,
            'Score': scores
        })
        #data['Positive'] = data['Score'] > 0  # Add a column to indicate scores above 0

        #st.scatter_chart(data, x='Position', y='Score', color='Positive')  # Use 'Highlight' for color
        
        st.scatter_chart(data, x='Position', y='Score')
        
    except ValueError:
        st.error("Not enough values to unpack!")
        
    except:
        st.error("Something went wrong!")