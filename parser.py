# parser.py

def parse_prompt(prompt_text):
    sections = {}
    current_section = None

    for line in prompt_text.splitlines():
        line = line.strip()
        if line.startswith("::"):
            current_section = line[2:].strip().rstrip(":")
            sections[current_section] = []
        elif current_section:
            sections[current_section].append(line)

    # Join multi-line values into a single string or process lists
    for key, lines in sections.items():
        joined = "\n".join(lines)
        if joined.startswith("[") and joined.endswith("]"):
            try:
                sections[key] = eval(joined)
            except:
                sections[key] = joined
        else:
            sections[key] = joined

    return sections
