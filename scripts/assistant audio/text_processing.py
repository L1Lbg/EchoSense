import ollama
import os


this_file_path = os.path.abspath(__file__)
parent_directory = os.path.dirname(this_file_path)
prompt_file_path = os.path.join(parent_directory, 'prompt.txt')

pre_prompt = open(prompt_file_path, 'r').read() 

def text_processing(user_prompt):
    prompt = f"{pre_prompt}\n User prompt: {user_prompt}"

    response = ollama.chat(
        model='llama3.2:3b', messages=[{'role': 'user', 'content': prompt}]
    )

    print(response['message']['content'])

# stream = ollama.chat(
#     model='llama3.2:3b',
#     messages=[{'role': 'user', 'content': prompt}],
#     stream=True,
# )

# for chunk in stream:
#     print(chunk['message']['content'], end='', flush=True)rue)