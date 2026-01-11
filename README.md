# hg_chat_with_model

A small educational Python project for **asynchronous chat inference** using Hugging Face models.

The project reads user queries from a CSV file, sends them concurrently to a chat model, and writes the results to a new CSV file that fully reproduces the input data with an additional model response column.

---

## How It Works

1. Read user queries from a CSV file.
2. Convert each query into a single-turn chat message.
3. Send all chats concurrently to a Hugging Face model.
4. Save a copy of the input CSV with an added model response column.

---

## Configuration

The application is configured via environment variables (`.env` file):

```
hg_token=YOUR_HUGGINGFACE_TOKEN
model=HuggingFaceModelName
busket_file_name=input.csv
result_file_name=output.csv
````

---

## Data Format

Input CSV (located in `data/`) must contain at least:

```csv
id,query
```

The output CSV:

* contains all original columns
* adds an additional `model_answer` column

---

## Project Structure

```
hg_chat_with_model/
├── __main__.py              # Entry point and pipeline orchestration
├── hg_api_calls.py      # Asynchronous Hugging Face chat requests
├── data_processing.py   # CSV input and output processing
```

---

## Run

```bash
poetry run python -m src.hg_chat_with_model
```
Dependencies are defined in `pyproject.toml`.

---

## Notes

* Each query is sent as a single user message (no conversation history).
