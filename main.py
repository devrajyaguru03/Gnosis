from core import add_new_knowledge, list_knowladge, ask_knowledge


def main():
    print(r"""
██████╗ ███╗   ██╗ ██████╗ ███████╗██╗███████╗
██╔════╝ ████╗  ██║██╔═══██╗██╔════╝██║██╔════╝
██║  ███╗██╔██╗ ██║██║   ██║███████╗██║███████╗
██║   ██║██║╚██╗██║██║   ██║╚════██║██║╚════██║
╚██████╔╝██║ ╚████║╚██████╔╝███████║██║███████║
╚═════╝ ╚═╝  ╚═══╝╚══════╝╚══════╝╚══════╝
""")

    print("v0.1")
    print()
    print("Welcome to GNOSIS.")
    print()
    print("Commands:")
    print("  add")
    print("  ask")
    print("  list")
    print("  exit")
    print()

    while True:
        command = input(">  ").strip().lower()

        match command:
            case "add":
                content = input("\nEnter knowledge:\n").strip()

                if not content:
                    print("\nKnowledge cannot be empty.")
                    continue

                try:
                    add_new_knowledge(content)
                    print("\nSaved.")
                except Exception:
                    print("\nCould not save knowledge.")

            case "ask":
                query = input("\nQuestion:\n").strip()

                if not query:
                    print("\nQuestion cannot be empty.")
                    continue

                try:
                    ask_knowledge(query)
                except Exception:
                    print("\nCould not process the question.")

            case "list":
                try:
                    list_knowladge()
                except Exception:
                    print("\nCould not load knowledge.")

            case "exit":
                print("Goodbye.")
                break

            case _:
                print("\nUnknown command.")
                print("\nAvailable commands:")
                print("add")
                print("ask")
                print("list")
                print("exit")


if __name__ == "__main__":
    main()