import openai

# Set up your OpenAI API credentials
openai.api_key = "API TOKEN"

# Define a function to send a message and receive a response
def chat(message):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=15
    )
    return response.choices[0].text.strip()

# Start the conversation
print("ChatGPT: Hello! How can I assist you today?")

while True:
    user_input = input("User: ")
    if user_input.lower() == 'bye':
        print("ChatGPT: Goodbye!")
        break

    response = chat(user_input)
    print("ChatGPT:", response)
