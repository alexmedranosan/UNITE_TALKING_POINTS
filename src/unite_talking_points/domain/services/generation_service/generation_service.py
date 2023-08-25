from typing import List

from langchain import OpenAI, PromptTemplate, LLMChain

from src.unite_talking_points.domain.services.service import Service


class GenerationService(Service):
    """
    A service that generates talking points based on other documents using LangChain and OpenAI models.
    """

    def __init__(self, summaries: List[str], generation_parameters: dict, openai_api_key: str):
        """
        A service that generates talking points based on other documents using LangChain and OpenAI models.
        :param summaries: List[str] List summarized texts
        :param generation_parameters: dict The parameters for the generation.
        :param openai_api_key: str The OpenAI API key.
        """
        super().__init__()
        self.generation_parameters = generation_parameters
        self.generation_parameters['summaries'] = summaries

        self.openai_api_key = openai_api_key

    def _pre_process(self):
        """
        Initialize the Langchain prompt with the given parameters.

        This includes initializing the model connection and defining the Prompt Template.
        """
        # Initialize the model connection
        self.llm = OpenAI(temperature=self.generation_parameters['temperature'], openai_api_key=self.openai_api_key)

        # TODO: Define the prompt template and chain as a singleton
        generation_template = """
        given this summaries about a group of relevant documents {summaries}.
        
        I want you to write a talking point:
            1. Attending this user prompt: {user_prompt}.
            2. {length} in length.
            3. {tone} in tone.
        """

        self.generation_prompt_template = PromptTemplate(
            input_variables=['summaries', 'user_prompt', 'length', 'tone'],
            template=generation_template
        )

        self.chain = LLMChain(llm=self.llm, prompt=self.generation_prompt_template)

    def _process(self):
        self.output = self.chain.run(**self.generation_parameters)

    def _post_process(self):
        return self.output
