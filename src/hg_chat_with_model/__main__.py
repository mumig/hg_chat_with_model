from huggingface_hub import AsyncInferenceClient
import asyncio
from os import getenv
from dotenv import load_dotenv
from .data_processing import get_dialogues_from_busket, save_results
from .hg_api_calls import model_async_calls

load_dotenv(override=True)

def get_env_var(name: str, required: bool = True):
    value = getenv(name)
    if required and value is None:
        raise RuntimeError(f"{name} is not set")
    return value


async def main():

    hg_token = get_env_var("hg_token")    
    model = get_env_var("model")
    busket_file_name = get_env_var("busket_file_name")
    result_file_name = get_env_var("result_file_name")

    client = AsyncInferenceClient(token=hg_token)

    dialogues = get_dialogues_from_busket(busket_file_name)
    
    model_answers = await model_async_calls(client, model, dialogues)

    save_results(busket_file_name, result_file_name, model_answers)

if __name__ == "__main__":
    asyncio.run(main())
