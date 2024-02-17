import os
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from plugins.WeatherPlugin.Tasks import Tasks

kernel = sk.Kernel()

class WeatherController:

    kernel.add_chat_service(
        service_id="azure_gpt35_chat_completion",
        service = AzureChatCompletion(
            deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_key=os.getenv("AZURE_OPENAI_API_KEY")
        )
    )

    tasks_plugin = kernel.import_plugin(Tasks(), "WeatherPlugin")
    tasks_plugin["Bangalore"]

    # plugin_directory = "PublishingPlugin"
    # weatherFunction = kernel.import_semantic_plugin_from_directory(plugin_directory, "WeatherPlugin")

#     result = kernel.register_semantic_function(
#         plugin_name=""
#         function_name=""
#         function_config=
#     )


# gpt2_complete = kernel.register_semantic_function(
#     plugin_name="GPT2Complete",
#     function_name="gpt2_complete",
#     function_config=create_semantic_function_config(
#         "{{$input}} is the capital city of", hf_config_dict, kernel
#     ),
# )

function_config = create_semantic_function_config(
    chatbot_prompt, chat_config_dict, kernel
)
chatbot = kernel.register_semantic_function(
    plugin_name="SimpleChatbot",
    function_name="simple_chatbot",
    function_config=function_config,
)