from pydantic import BaseModel
from google import genai
from google.genai import types
from config.config import settings

client = genai.Client(api_key=settings.GOOGLE_API_KEY)


class Recipe(BaseModel):
    recipe_name: str
    recipe_description: str
    recipe_ingredients: list[str]


class TestGem:
    def _try(self):
        # structured_llm = llm.with_structured_output(Joke)
        response = client.models.generate_content(
            model=settings.MODEL_ID,
            contents="Provide a popular cookie recipe and its ingredients.",
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=Recipe,
            ),
        )
        
        # return structured_llm.invoke("Tell me a joke about cats")
        return response.text