# main.py
from agents import Agent, Runner
from connection import get_config  # ✅ Corrected!

# Define the agent
translator = Agent(
    name="translator",
    instructions="You are a helpful translator. Always translate into Urdu."
)

print("\n📘 Type something in English to translate it to Urdu. Type 'exit' to quit.\n")

# Synchronous Run Loop
conversation_history = []
while True:
    question = input("🗣️  You: ")
    if question.strip().lower() in ["exit", "quit"]:
        print("👋 Goodbye!")
        break

    # Append question to history
    full_prompt = "\n".join(conversation_history + [f"User: {question}"])
    
    result = Runner.run_sync(translator, full_prompt, run_config=get_config())

    print(f"🤖 Translator: {result.final_output}\n")
    conversation_history.append(f"User: {question}")
    conversation_history.append(f"Translator: {result.final_output}")
