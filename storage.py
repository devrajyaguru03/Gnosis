import json
from pathlib import Path


DATA_FILE = Path("/Users/devrajyaguru/Desktop/Gnosis/data/knowledge.json")


def load_knowledge():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_knowledge(knowledge):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(knowledge, file, indent=4)


def add_knowledge(knowledge):
    current_knowledge = load_knowledge()

    current_knowledge.append(knowledge)

    save_knowledge(current_knowledge)


def get_all_knowledge():
    return load_knowledge()