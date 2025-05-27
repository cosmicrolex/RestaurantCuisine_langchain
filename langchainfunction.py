import os
from groqKey import GROQ_API_KEY
from langchain_core.messages import HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from langchain.chains import SimpleSequentialChain 


os.environ["GROQ_API_KEY"] = GROQ_API_KEY  # Replace with your Groq API key or your key file here

# Initialize LLM with temperature
llm = ChatGroq(model="llama-3.1-8b-instant" , temperature =0.6)

""" this is a simple example of how to give input to the llm
# Create a HumanMessage object with the prompt
prompt = HumanMessage(content="give me name for my dog")
# Invoke the LLM
response = llm.invoke([prompt])
print(response.content) """

def generate_restaurant_name_and_items(cuisine):
    # Prompt for restaurant name
    name_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a restaurant for {cuisine} food. Give me a fancy name for the restaurant in two words only."
    )
    restaurant_name_chain = LLMChain(llm=llm, prompt=name_prompt)

    # Prompt for menu items
    dishes_prompt = PromptTemplate(
        input_variables=["cuisine"],
        template="Give me some dish names for an {cuisine} restaurant with their prices beside them, separated by commas."
    )
    food_items_chain = LLMChain(llm=llm, prompt=dishes_prompt)

    # Run chains separately
    restaurant_name = restaurant_name_chain.run(cuisine).strip()
    dishes = food_items_chain.run(cuisine).strip()

    return {
        'Restaurant_name': restaurant_name,
        'dishes': dishes
    }


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("italian"))