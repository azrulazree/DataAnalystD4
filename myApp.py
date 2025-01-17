import streamlit as st

st.write('shrdc')
st.write('Hellow again')
st.write('shrdc')

st.write("Hello friends")
st.header("Hello friends")
st.subheader("Hello friends")
st.caption("Hello friends")

st.success("good")
st.warning("bad")
st.info("info")
st.error("Error!")

st.markdown("*Streamlit* is **really** ***cool***.")

st.markdown(''' :red[Streamlit] :orange[is] :green[fun] ''')

st.markdown("Here's a bouquet &mdash;\:tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

#UI Component
st.selectbox("Kuala Lumpur is located at",
['Malaysia', 'Thailand', 'UK'])
st.multiselect("Select 2 states",
['Selangor','Johor','Kedah'])

st.button("Click Here to Proceed")

st.slider("Select the length of stay", 1,10, value=3)

number = st.number_input("Insert a number",
value=None, placeholder="Type a number...")

st.write("The current number is ", number)

#SHRDC will be in the middle
col1, col2, col3 = st.columns(3) 
with col2:
    from PIL import Image
    im = Image.open('shrdc_logo.png')
    st.image(im, width=600) 


#Dataframe
import pandas as pd
df = pd.read_excel('sampledata.xlsx')
st.dataframe(df)

#Bar chart
st.bar_chart(df, x="Location", y="Income")

#Line chart
st.line_chart(df, x="Household", y="Income")

#Scatter chart
st.scatter_chart(df, x="Household", y="Income")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", width=200)
with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)
with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)


col1, col2, col3 = st.columns(3)

#with col1:
    #st.header("A cat")
    #st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

#with col3:
    #st.header("An owl")
    #st.image("https://static.streamlit.io/examples/owl.jpg")