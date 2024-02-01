import textwrap
import os
from dotenv import dotenv_values
from IPython.display import Markdown, display
import google.generativeai as genai
import platform
class GenerativeAI:
    CONST_COMMAND = "Show command for the given query. Show only command not any other description with it. Only provide output if the user asks for a specific operating system command.If the user asks anything else or requests a list of commands, respond with 'invalid input is given.'. Also the os is "
    CONST_OS = platform.system()
    # CONST_CONFIG="Also connect to database before the execution of any command using given username and password"
    def __init__(self):
        env_vars = dotenv_values(".env")
        self.GOOGLE_API_KEY = env_vars.get('GOOGLE_API_KEY')
        # self.GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
        self.model = genai.GenerativeModel('gemini-pro')
        genai.configure(api_key=self.GOOGLE_API_KEY)

    def to_markdown(self, text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
    
    def generate_response(self, user_input):
        response = self.model.generate_content(self.CONST_COMMAND + self.CONST_OS + user_input)
    
        return response.text