from app.graph_builder import build_graph

app = build_graph()

def run_agent():
    print("\nLangGraph Smart Info Agent \n(Type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Agent: Goodbye!")
            break
        try:
            response = app.invoke({"input": user_input})
            print("Agent:", response["result"])
        except Exception as e:
            print("Agent: Oops, something went wrong!", e)

if __name__ == "__main__":
    run_agent()
