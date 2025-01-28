# I. EXTRA/STRETCH: Importing saved LLM responses for Testing LLM Interactions via Scripting
import random
from process_responses import * 

# II. Importing the necessary functions for the Gemini API LLM Interaction to Work
from gemini_ai_call import * 
from gemini_myapi import *

# III. Gemini API integration & Call
def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=the_api_key)
    gemini_model = genai.GenerativeModel("gemini-1.5-flash")
    return gemini_model

gemini_model = __get_gemini_client__()


## Load previously generated LLM responses (if available)
llm_responses = read_responses()

# Create a list to store all extracted school names
all_schools = []

# Extract school names from LLM responses (assuming responses are in a specific format)
if llm_responses:
    for response in llm_responses:
        try:
            school_name = response.split()[0]  # Extract school name (adjust as needed)
            all_schools.append(school_name)
        except IndexError:
            print(f"Error extracting school name from response: {response}")

# Select 5 random schools

random_schools = random.sample(all_schools, k=5)

# Create the test prompt
test_prompt = f"""
Based on the following 5 randomly selected colleges: {', '.join(random_schools)}, 

Explain how students can best prepare for their US College search and 5 tips for them to be successful a while noting that as a Software Engineer, I want to see how MQTT & LLM can help me get good data and information to be helpful in my preparation. 
"""


# Generating the Response
try:
    response = gemini_model.generate_content(test_prompt).text

    # Print Response with Structure
    print("\nLLM Response:\n")
    for line in response.split("\n"):
        print(f"  - {line}")
    print("\n")

except Exception as e:
    print(f"Error calling Gemini API: {e}")

print("❤️ Ready to Support your University Journey ❤️") 