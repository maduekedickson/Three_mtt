import streamlit as st

def run():
    # Home Page Section
    st.title("🖱️Team Rite Click🖱️")
    st.subheader("Nigeria Hospital Data Visualization on Map")
    st.markdown("## And Grid Code App")
    
    st.markdown("""
        ### Instructions:
        * Click on the "View Digital Map" button above to open the map.
        * Once the map loads, click the layer control at the top right corner.
        * Uncheck the layers to view the impact of each layer individually.
        * Check multiple layers at once to compare different data points together.
        * Double-click on the markers on each layer for pop-ups.
        * Explore the map to see how different layers interact with one another.
        * For best results, zoom in and out of the map to explore data at different scales.
        * Click on any radio button on the sidebar to switch to any section.
    """)

if __name__ == "__main__":
    run()
