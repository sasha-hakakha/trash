from openApiFunctionCaller import OpenApiFunctionCaller

def main():
    caller = OpenApiFunctionCaller(api_key_path = 'key.txt')
    func_dict = caller.create_function_dict({})
    answer = caller.call_functions("prompt here", func_dict)
    console.log(answer)
if __name__ == '__main__':
    main()
