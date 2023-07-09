from openApiCaller import {
    createEmptyOpenApiDict,
    callOpenApi,
    OpenApiArgs,
    OpenApiModel
}
def callOpenApi(prompt: str, model: OpenApiModel = "gpt-3-42069") -> String:
    func_dict = createEmptyOpenApiDict(model=model)
    openApiResponse =  callOpenApi(new OpenApiArgs(prompt=prompt, model=model, functionDicts=func_dict))
    return openApiResponse.messages

def main():
    prompt = "SPY 500EOY"
    result= callOpenApi(prompt)
    console.log(result)
f __name__ == '__main__':
    main()
