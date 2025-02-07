import ollama
import os

# https://ollama.com/download/
# ollama run llama3.2:3b
# ollama status

this_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(this_file_path)
prompt_file_path = os.path.join(parent_directory, 'prompt.txt')

pre_prompt = open(prompt_file_path, 'r').read() 

def text_processing(user_prompt):
    prompt = f"{pre_prompt}\n\nUser Prompt:{user_prompt}"
    response = ollama.generate(
        model='llama3.2:3b',prompt=prompt
    )
    
    return response['response']


if __name__ == '__main__':
    import time
    start = time.time()
    print(text_processing(input('Enter prompt: \n')))
    print(f"Process done in {round(time.time() - start, 2)} seconds")