# long_responses.py

import random

# Responses for handling various situations
def unknown():
    response = [
        "Could you please clarify what you mean?",
        "I'm not sure I understand. Can you rephrase that?",
        "I'm not sure I follow you. Can you give me more details?",
        "Can you elaborate on that?"
    ]
    return random.choice(response)

def greeting_response():
    return "Hello! How can I assist you today?"

def doing_response():
    return "I'm doing fine, thank you! How about you?"

def love_code_response():
    return "Thank you! I appreciate your love for code. How can I help you with your coding questions today?"

def farewell_response():
    return "Goodbye! Have a great day!"

def about_response():
    return "I'm a chatbot designed to assist you with various tasks. Feel free to ask me anything!"

# Additional functionality
def generate_random_number():
    return random.randint(1, 100)

def weather_forecast(location):
    # Code to fetch weather forecast for the given location from an external API
    return f"The weather forecast for {location} is sunny."

def news_headlines():
    # Code to fetch latest news headlines from an external source
    headlines = ["Breaking: New discovery in space exploration!", "Tech giant launches new product line.", "Economy shows signs of recovery."]
    return random.choice(headlines)