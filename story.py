import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException


GROQ_API_KEY = os.getenv("STORY_API")

class Story:
    def __init__(self):
        self.llm = ChatGroq(
        model = "llama3-70b-8192",
        groq_api_key = GROQ_API_KEY,
        temperature=0
        )
    
    def generate_story(self, starting_line, selected_genre, story_length):
        prompt_extract = PromptTemplate.from_template(
                """
                ### INSTRUCTIONS
                You are a creative fiction writer.
                Your task is to write a 500-word short story in the **{selected_genre}** genre.
                Here is the starting line provided:
                "{starting_line}"
                If the starting line is appropriate and usable, continue the story directly from it.
                If the starting line is vague, unclear, or inappropriate for storytelling, use it only as inspiration and rewrite it creatively in a way that fits the selected genre.
                The final story should:
                - Be approximately {story_length} words long
                - Match the tone and conventions of the selected genre
                - Include characters, setting, conflict, and resolution or an open ending typical of short stories
                - Flow naturally and feel complete on its own
                Now write the story and generate a appropriate title upto 7-8 words for story.
                Give the title and story in json format
                ### VALID JSON (NO PREAMBLE):
                """
            )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"starting_line":starting_line,"selected_genre":selected_genre,"story_length":story_length})
        
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs")

        return res