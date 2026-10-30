from http import client
import json
import requests
from pydantic import BaseModel, Field

def convert_timezone(date_time: str, from_timezone: str, to_timezone: str) -> str:
    """
    Convert a datetime from one timezone to another.
    
    Args:
        date_time: The datetime string in ISO format
        from_timezone: Source timezone
        to_timezone: Target timezone
    
    Returns:
        A string with the converted datetime and timezone information
    """
   
    url = "https://api.opentimezone.com/convert"
    
   
    payload = {"dateTime": date_time, "fromTimezone": from_timezone, "toTimezone": to_timezone}
    
    try:
       
        response = requests.post(url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        converted_time = data.get('dateTime', 'N/A')
        
        return f"Time in {to_timezone}: {converted_time}"
    
    except requests.exceptions.RequestException as e:
        return f"Error converting timezone: {str(e)}"


result = convert_timezone('2025-01-20T14:30:00', 'America/New_York', 'Europe/London')
print(result)


tools = [
    {
        # Define a function tool called convert_timezone
        "type": "function",
        "name": "convert_timezone",
        "description": "Convert a datetime from one timezone to another using the OpenTimezone API.",
        "parameters": {
            "type": "object",
            # Define the parameter names, types, and descriptions
            "properties": {
                "date_time": {
                    "type": "string",
                    "description": "The datetime string in ISO format (e.g., '2025-01-20T14:30:00')"
                },
                "from_timezone": {
                    "type": "string",
                    "description": "The source timezone (e.g., 'America/New_York', 'Asia/Tokyo')"
                },
                "to_timezone": {
                    "type": "string",
                    "description": "The target timezone (e.g., 'Europe/London', 'Australia/Sydney')"
                }
            },
            # Ensure that all three parameters are required
            "required": ["date_time", "from_timezone", "to_timezone"],
            "additionalProperties": False
        }
    }
]


messages = [{"role": "user", "content": "What time is 2:30pm on January 20th in New York in Tokyo time?"}]
response = client.responses.create(model="gpt-5.4-mini", input=messages, tools=tools)
messages += response.output

# Process function calls and execute the timezone conversion
for item in response.output:
    if item.type == "function_call":
        if item.name == "convert_timezone":
            timezone_result = convert_timezone(**json.loads(item.arguments))
            
            # Append function output to messages
            messages.append({"type": "function_call_output", "call_id": item.call_id, "output": json.dumps({"convert_timezone": timezone_result})})

# Make second API request with function results
response = client.responses.create(model="gpt-5.4-mini", input=messages, tools=tools)
print(response.output_text)

# Define the book recommendation schema
class MovieRecommendation(BaseModel):
    title: str = Field(description="The movie title")
    genre: str = Field(description="Primary genre")
    vibe: str = Field(description="One-word vibe: cozy, thrilling, emotional, or fun")
    why: str = Field(description="One sentence explaining why this matches")

# Generate structured recommendation
response = client.responses.parse(
    model="gpt-5.4-mini",
    instructions="You are a knowledgeable movie recommender.",
    input="Recommend a movie for someone who loved Inception and wants something mind-bending",
    text_format=MovieRecommendation,
)

# Extract the parsed output and results
recommendation = response.output_parsed
print(f"Title: {recommendation.title}")
print(f"Reason: {recommendation.why}")



messages = [{"role": "system", "content": "You are a product cataloging expert who provides concise classifications and descriptions."}]

# Add user message with text and image
messages.append({
    "role": "user",
    "content": [
        {"type": "input_text", "text": "Classify this product and write a brief but punchy description for our catalog."},
        {"type": "input_image", "image_url": image_url}
    ]
})

# Create the response
response = client.responses.create(model="gpt-5.4-mini", input=messages)

print(response.output_text)
visualize_image(image_url)
