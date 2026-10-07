# NexaAI - Main Application
# Takes user input, processes intent, generates response

def get_ai_response(user_query):
    print(f"User asked: {user_query}")
    # Here we would call Amazon Bedrock
    response = f"NexaAI Answer for: {user_query}"
    return response

# Example
if __name__ == "__main__":
    query = input("Ask NexaAI: ")
    print(get_ai_response(query))
