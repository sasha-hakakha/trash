from dataclasses import dataclass, asdict
from typing import List, Dict
import json
import openai

OpenApiModel = "gpt-4-0613" | "gpt-3"

@dataclass
class FunctionParameters:
    name: str
    model_type: str
    description: str
    required: bool


@dataclass
class FunctionDict:
    name: str
    description: str
    parameters: List[FunctionParameters]

@dataClass
class OpenApiArgs:
    prompt: string
    model: OpenApiModel
    functionDicts: FunctionDict[]
    temp: int = 1

def callOpenApi(openApiArgs: OpenApiArgs) -> openai.ChatCompletion:
        system_="You are a helpful project manager, based on a user query select the best people to help conduct further analysis."

        return openai.ChatCompletion.create(
            model=openApiArgs.model,
            messages=[{"role": "system", "content": system_},{"role": "user", "content": openApiArgs.prompt}],
            functions=json.dumps(asdict(openApiArgs.functionDicts))
            temperature=openApiArgs.temp,
        )
