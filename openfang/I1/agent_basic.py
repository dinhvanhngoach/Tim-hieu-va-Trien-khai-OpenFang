# agent_basic.py

# Tool: convert text to uppercase
def uppercase_tool(text):
    return text.upper()


# Simple Agent
class Agent:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def run(self, text):
        print("Agent:", self.name)
        print("Task:", self.description)
        result = uppercase_tool(text)
        print("Result:", result)


# Run agent
if __name__ == "__main__":

    agent = Agent(
        name="TextUpperAgent",
        description="This agent receives a text input and converts it into uppercase letters."
    )

    user_input = input("Enter text: ")
    agent.run(user_input)