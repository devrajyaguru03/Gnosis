from storage import add_knowledge, get_all_knowledge

MIN_RELEVANCE = 0.5

def create_knowledge(content, knowledge):
    return {
        "id": len(knowledge) + 1,
        "content": content
    }


def add_new_knowledge(content):
    knowledge = get_all_knowledge()
    new_knowledge = create_knowledge(content, knowledge)

    add_knowledge(new_knowledge)


def list_knowladge():
    knowledge = get_all_knowledge()

    print("\nKnowledge:\n")

    if not knowledge:
        print("No knowledge available.")
        return

    for item in knowledge:
        print(f"[{item['id']}] {item['content']}")
        print()

    print(f"Total: {len(knowledge)}")


def tokenize(text):
    return text.lower().split()


def search_knowledge(query):
    knowledge = get_all_knowledge()
    query_words = tokenize(query)

    if not query_words:
        return None

    best_match = None
    best_score = 0

    for item in knowledge:
        knowledge_words = tokenize(item["content"])

        matches = 0

        for word in query_words:
            if word in knowledge_words:
                matches += 1

        score = matches / len(query_words)

        if score > best_score:
            best_score = score
            best_match = item

    if best_match is None:
        return None

    return {
        "knowledge_id": best_match["id"],
        "content": best_match["content"],
        "score": best_score
    }


def ask_knowledge(query):
    result = search_knowledge(query)

    if result is None:
        print("\nI don't have enough information to answer that.")
        return

    if result["score"] < MIN_RELEVANCE:
        print("\nI don't have enough information to answer that.")
        return

    print("\nTop result:")
    print(result["content"])
    print(f"\nRelevance: {result['score']:.2f}")