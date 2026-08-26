from foundry_local_sdk import Configuration, FoundryLocalManager

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

client = model.get_chat_client()

response = client.complete_chat([
        {
                "role" : "user", 
                "content" : "Explain what an AI agent is in one sentence."
        }
])

print(response.choices[0].message.content)