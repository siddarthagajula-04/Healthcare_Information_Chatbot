def initialize_memory():
    return [{"role": "system", "content": "You are a healthcare information assistant."}]


def update_memory(memory, role, content):
    memory.append({"role": role, "content": content})
    return memory