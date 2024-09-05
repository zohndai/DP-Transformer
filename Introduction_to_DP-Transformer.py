import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import streamlit.components.v1 as components


<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-6MJ8FDZ7GH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-6MJ8FDZ7GH');
</script>

st.set_page_config(
    page_title="Welcome to DP-Transformer",    
    page_icon="💧",        
    layout="wide",                
    initial_sidebar_state="auto"  
)

TEXT1 = """
        <body style='text-align: justify; color: black;'>
        <p> DP-Transformer platform is backend by advanced machine learning models to service users for predicting the degradation products of aqueous organic pollutants in chemical oxidation processes. 
		DP-Transformer can now predict the degradation products and degradation pathways of organic pollutants. DP-Tramsformer uses SMILES to represent chemicals.   
        </p>DP-Transformer is based on a similar model architecture as the Molecular Transformer but is distinguished by the utilized dataset. The well-trained DP-Transformer accepts pollutant SMILES, oxidative species,
	and reaction conditions (e.g., pH) as inputs and outputs the SMILES of the degradation products. This model is capable of predicting not only the degradation intermediates but also the complete degradation pathways. 
 The prediction of degradation pathways is accomplished through an iterative process, where a predicted degradation product made by DP-Transformer is used as input for subsequent prediction. This process continues until the 
 model predicts CO2 or when the predicted chemicals remain unchanged (i.e., non-degradable), indicating the formation of the final degradation products (Figure 1). 
	  <p> 
	  </p>
        </body>         
        """
if "show_animation" not in st.session_state:
    st.session_state.show_animation = True
st.header('Welcome to DP-Transformer!')
st.markdown(f'{TEXT1}', unsafe_allow_html=True)
#st.image(Image.open('Fig1.jpg'), caption = 'Figure 1. The comparison between binary MF (B-MF) and count-based MF (C-MF) when representing 1-Decanol, 1-Nonanol and 1-Ocatal')
#col1= st.columns([1])
st.image(Image.open('predic.jpg'), width=800, caption = 'Figure 1. The workflow that DP-Transformer makes predictions')
#col2.image(Image.open('Fig2.jpg'), caption = 'Figure 2. The performance enhancment C-MF brings for each dataset')
if "has_snowed" not in st.session_state:
    st.snow()
    st.session_state["has_snowed"] = True

if 'visitor_count' not in st.session_state:
	st.session_state.visitor_count = 0
if 'session_initialized' not in st.session_state:
	st.session_state.visitor_count += 1
	st.session_state.session_initialized = True
st.write(f'Visitor Number: {st.session_state.visitor_count}')
