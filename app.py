import streamlit as st
from story import Story

story_genres = [
    "Drama",
    "Literary Fiction",
    "Science Fiction",
    "Fantasy",
    "Horror",
    "Mystery",
    "Thriller",
    "Romance",
    "Historical Fiction",
    "Speculative Fiction",
    "Magical Realism",
    "Dystopian",
    "Cyberpunk",
    "Paranormal",
    "Crime",
    "Adventure",
    "Satire",
    "Coming-of-Age",
    "Love Story",
    "Fairy Tale",
    "Mythology",
    "Gothic",
    "Noir",
    "Absurdist",
    "Slice of Life",
    "Post-Apocalyptic"
]

story_length = [500, 750, 1000, 1200]

def streamlit_app(model, story_genres, story_length):
    st.title("STORY GENERATOR")
    starting_line = st.text_input("Enter Starting Line",max_chars=80)
    col1, col2  = st.columns(2)

    with col1:
        selected_genre = st.selectbox("Select Genre",story_genres)
    with col2:
        selected_length = st.selectbox("Select Length", story_length)

    if st.button("Generate"):
        response = model.generate_story(starting_line, selected_genre, selected_length)
        story_title = response['title']
        story_content = response['story']
        c = st.container()

        c.subheader(story_title)
        c.markdown(story_content)
    

if __name__ == "__main__":
    stories = Story()
    st.set_page_config(layout="centered", page_title="STORY GENERATOR", page_icon="📖")
    streamlit_app(stories,story_genres ,story_length)