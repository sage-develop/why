from typing import Type
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel

# Step 1: Create pydantic model for decision tree attrs

# Step 2: Add attr to decision tree nodes

# Step 3: Extract the decision tree nodes from the file with pydantic model
# (ensures all nodes are traversed and all known attrs are filled and lowers chance of AI hallucination)

# Step 4: Extract information from client text and pdf with client pydantic model using LLM

# Step 5: Combine the decision tree nodes and the client information to get the final result

class Extractor:
    """
    Extract structured attributes from client text using an LLM
    and a Pydantic model schema.
    """

    def __init__(self, openai_api_key: str):
        self.llm = ChatOpenAI(
            api_key=openai_api_key,
            model="gpt-4",
            temperature=0,
        )

    def extract(self, text: str, schema: Type[BaseModel]) -> BaseModel:
        """
        Extract structured data from client text.
        """
        parser = PydanticOutputParser(pydantic_object=schema)

        prompt = f"""
        Extract structured information from the following client statement
        according to the schema. Fill only what you are certain of.

        Client statement:
        \"\"\"{text}\"\"\"

        {parser.get_format_instructions()}
        """

        response = self.llm.invoke(prompt)
        return parser.parse(response.content)
