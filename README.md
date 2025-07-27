# 📝 Short Story Generator using GROQ LLM

This project is a simple Streamlit-based application that allows users to generate short stories using the **GROQ Large Language Model (LLM)**. Users can select a **genre**, choose a **word count**, and provide a **starting line** — the model then generates a creative story based on their inputs.

---

## 🚀 Features

- Generate creative stories using GROQ LLM
- Choose from 25+ popular short story genres
- Set desired word length (500–1200 words)
- Provide a custom or sample starting line
- Intuitive web UI using **Streamlit**

---

## 📚 Sample Starting Lines by Genre

You can use any of these 10 pre-defined starting lines, or write your own:

| Genre              | Starting Line                                         |
|--------------------|--------------------------------------------------------|
| Science Fiction    | *"The stars blinked out, one by one."*                |
| Fantasy            | *"She woke with dragon scales across her arms."*      |
| Horror             | *"Someone was breathing under my bed last night."*    |
| Mystery            | *"The letter arrived fifty years after it was sent."* |
| Romance            | *"Their hands brushed, and time seemed to pause."*    |
| Historical Fiction | *"He marched into 1914 with hope and a rifle."*       |
| Dystopian          | *"Curfews meant survival after the second blackout."* |
| Magical Realism    | *"Every mirror lied, except the one in grandma’s attic."* |
| Coming-of-Age      | *"Summer ended the day we found that hidden cave."*   |
| Adventure          | *"Maps don’t show the island we crashed on."*         |

---

## 🌐 Deployment

The app is live and can be accessed here:  
👉 [**Launch App**](https://story-generator-aditya-naranje.streamlit.app/)  


---

## 🛠️ Technologies Used

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [GROQ LLM API](https://console.groq.com/)

---

## 📦 Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/story-generator-groq.git
   cd story-generator-groq

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Set your GROQ API Key (use environment variable or .env file):

   ```bash
    export GROQ_API_KEY=your_api_key_here

4. Run the app:

   ```bash
   streamlit run app.py

## 🙌 Acknowledgments
- Thanks to GROQ for providing powerful LLM capabilities, and Streamlit for making UI development effortless.
