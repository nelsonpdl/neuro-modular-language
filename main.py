# main.py

from parser import parse_prompt
from action import execute_actions

def load_prompt(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def main():
    prompt_path = './agentic_test/prompt.nml'
    prompt_text = load_prompt(prompt_path)

    print("📥 Loading NMEP prompt...\n")
    parsed_data = parse_prompt(prompt_text)

    print("🧠 Parsing complete. Executing agent...\n")
    execute_actions(parsed_data)

if __name__ == '__main__':
    main()
