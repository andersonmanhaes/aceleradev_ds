import streamlit as st

def main():
    st.title('Hello World')
    st.header('This is header')
    st.subheader('This is subheader')
    st.text('This is text')
    st.subheader('Imagens')
    st.image('0.jpeg')
    st.image('logo.png')
    st.subheader('Audio')
    st.audio('record.mov')
    st.subheader('Video')
    st.video('formaturaNicolas.mp4')


if __name__ == '__main__':
    main()