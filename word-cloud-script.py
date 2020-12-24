import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt



def cloud(text, max_word, max_font):
    stopwords = (['us', 'one', 'will', 'said', 'now', 'well', 'man', 'may',
                      'little', 'say', 'must', 'way', 'long', 'yet', 'mean',
                      'put', 'seem', 'asked', 'made', 'half', 'much',
                      'certainly', 'might', 'came', 'be', 'you'])

    wc = WordCloud(background_color="black", colormap="hot", max_words=max_word,
                   stopwords=stopwords, max_font_size=max_font)
    # generate word cloud
    wc.generate(text)

    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    st.pyplot()


def main():
    text = st.text_area("Add text ..")
    max_word = st.sidebar.slider("Max words", 200, 3000, 200)
    max_font = st.sidebar.slider("Max Font Size", 50, 350, 60)
    if text is not None:
        if st.button("Plot"):
            st.write("### Word cloud")
            st.write(cloud(text, max_word, max_font), use_column_width=True)





if __name__ == '__main__':
    main()
