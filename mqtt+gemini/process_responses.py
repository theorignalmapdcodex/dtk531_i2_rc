import json

def read_responses():
    try:
        with open("llm_responses.json", "r") as f:
            responses = f.readlines()
            return responses
    except FileNotFoundError:
        print("No responses found in llm_responses.json")
        return []
    

if __name__ == "__main__":
    responses = read_responses()
    for response in responses:
        # Assuming each response is on a separate line
        print("LLM Response:")
        print(response.strip())  # Remove leading/trailing whitespace
        print("\n")  # Add a newline after each response
        print("++++++++++++++++++++++++++++++++++++++++++++++++\n")