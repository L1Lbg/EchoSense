import ollama
import os


# ollama run llama3.2:3b
# ollama status

this_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(this_file_path)
prompt_file_path = os.path.join(parent_directory, 'prompt.txt')

pre_prompt = open(prompt_file_path, 'r').read() 

def text_processing(user_prompt):
    prompt = f"{user_prompt}\n\n{pre_prompt}"

    response = ollama.generate(
        model='llama3.2:3b',prompt=prompt
    )
    
    print(response['response'])


if __name__ == '__main__':
    text_processing(input('Enter prompt: \n'))