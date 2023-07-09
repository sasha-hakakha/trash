import json
import openai

class OpenApiFunctionCaller:
    def __init__(self, model="gpt-4-0613", api_key_path="key.txt"):
        openai_api_key ="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"  # Replace with your OpenAI API key

        openai.api_key = openai_api_key
        self.model = model

    def create_function_dict(self, function_dict):
        """
        Create a function schema from a dictionary.
        The dictionary should have the following structure:
        {
            "name": "function_name",
            "description": "function_description",
            "parameters": [
                {
                    "name": "param_name",
                    "type": "param_type",
                    "description": "param_description",
                    "required": True or False
                },
                ...
            ]
        }
        """
        params = {param["name"]: {"type": param["type"]} for param in function_dict["parameters"]}
        required_params = [param["name"] for param in function_dict["parameters"] if param.get("required", False)]

        return {
            "name": function_dict["name"],
            "description": function_dict["description"],
            "parameters": {
                "type": "object",
                "properties": params,
                "required": required_params,
            },
        }

    def call_functions(self, prompt, function_dicts, temp=1):
        """
        Calls multiple functions defined in function_dicts.
        """
        function_schemas = [self.create_function_dict(fn_dict) for fn_dict in function_dicts]
        system_="You are a helpful project manager, based on a user query select the best people to help conduct further analysis."

        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=[{"role": "system", "content": system_},{"role": "user", "content": prompt}],
            functions=function_schemas,
            temperature=temp,
        )
        return completion
