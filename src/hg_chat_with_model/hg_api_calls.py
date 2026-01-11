import asyncio
from huggingface_hub import AsyncInferenceClient

async def model_single_call(client: AsyncInferenceClient, model: str, id: str, messages: list[dict[str, str]]) -> tuple[str, str]:

    completion = await client.chat.completions.create(
        model=model,
        messages=messages
    )

    return (id, completion.choices[0].message.content)

async def model_async_calls(client: AsyncInferenceClient, model: str, dialogues: dict[str, list[dict[str, str]]]) -> dict[str, str]:
    
    tasks = [model_single_call(client, model, id, messages) for (id, messages) in dialogues.items()]
    
    done_tasks = await asyncio.gather(*tasks)

    results = {}
    for id, model_answer in done_tasks:
        results[id] = model_answer

    return results