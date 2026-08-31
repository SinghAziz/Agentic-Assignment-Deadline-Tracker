from foundry_local_sdk import Configuration, FoundryLocalManager
from tools import AVAILABLE_FUNCTIONS
import json
config = Configuration(app_name = "assignment-deadline-tracker")

FoundryLocalManager.initialize(config)

manager = FoundryLocalManager.instance

print("Foundry local initialisationn done")

model =  manager.catalog.get_model("qwen3-8b")
print("Model selected: ", model.id)

if not model.is_cached:
        print("Downloading Model...")

        model.download(
                lambda progress: print(
                        f"\rDownloading: {progress:.2f}%", end="", flush=True
                )
        )
        print()
else:
        print("Model already cached")


model.load()



add_assignment_tool = {
        "type" : "function", 
        "function":{
                "name" : "add_assignment", 
                "description" : 
                "Add an assignment with its due date and optional due time. If due time is not provided, it defaults to 'All Day'.",
                "parameters" : {
                        "type" : "object", 
                        "properties" : {
                                "assignment":{
                                        "type" : "string", 
                                        "description" : "The name of the assignment."
                                
                                }, 
                                "due_date" : {
                                        "type" : "string", 
                                        "description" : "The due date of the assignment in YYYY-MM-DD format."
                                },
                                "due_time" : {
                                        "type" : "string", 
                                        "description" : "The due time of the assignment in HH:MM format. If not provided, it defaults to 'All Day'."
                                }
                        }, 
                        "required" : ["assignment", "due_date"]
        }
        }
}

list_assignment_tool = {
        "type" : "function", 
        "function":{
                "name" : "list_assignments",
                "description" : "Lists all the assignments that are due on a given date and time. If due time is not provided, it lists all assignments due on the given date regardless of the time.",
                "parameters" : {
                        "type" : "object", 
                        "properties" : {
                                "due_date" : {
                                        "type" : "string", 
                                        "description" : "The due date of the assignment in YYYY-MM-DD format."
                                },
                                "due_time" : {
                                        "type" : "string", 
                                        "description" : "The due time of the assignment in HH:MM format. If not provided, it defaults to 'All Day'."
                                }
                        }, 
                        "required" : ["due_date"]
                },
        }
}
client = model.get_chat_client()

TOOLS =[
        add_assignment_tool,
        list_assignment_tool
]


def run_agent(user_input):
        messages=[
                {
                        "role"  : "user",
                        "content" : user_input
                }
        ]
        while True:
                print("DEBUG MESSAGES:", messages)
                response = client.complete_chat(
                        messages, 
                        tools = TOOLS
                )
                message = response.choices[0].message
                if not message.tool_calls:
                        return message.content

                tool_calls =[]
                for tool_call in message.tool_calls:
                        tool_calls.append({
                                "id" : tool_call.id, 
                                "type" : "function",
                                "function" : {
                                        "name" : tool_call.function.name, 
                                        "arguments" : tool_call.function.arguments
                                }
                        })
                
                messages.append({
                "role" : "assistant", 
                "content" : message.content or "", 
                "tool_calls" : tool_calls
        })

                for tool_call in message.tool_calls:
                        tool_name = tool_call.function.name
                        arguments = json.loads(
                                tool_call.function.arguments
                        )

                        function = AVAILABLE_FUNCTIONS[tool_name]
                        result = function(**arguments)

                        messages.append({
                                "role" : "tool",
                                "tool_call_id" : tool_call.id,
                                "content" : json.dumps(result)
                        })

while True:
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break
        answer = run_agent(user_input)

        print("\nAgent:", answer)