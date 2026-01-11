Отличные вопросы — оба по делу. Разберём по порядку и сразу дам обновлённый README.

---

## 1️⃣ Почему *batch chat inference* — и почему это не совсем корректно

Ты **прав**:
👉 **батчинга в классическом смысле тут нет**.

Что есть в коде:

* **много независимых запросов**
* отправляемых **параллельно** через `asyncio.gather`
* **без объединения в один batch** на уровне модели или API

Поэтому:

* ❌ *batching* — нет (нет группировки входов в один запрос)
* ✅ *concurrent / asynchronous inference* — да

Я использовал термин *batch* в разговорном смысле («обработка набора запросов»), но для README это **неудачно и неточно**. Спасибо, что поймал 👍
Исправляем на **asynchronous / concurrent inference**.

---

## 2️⃣ Добавляем про выходной CSV

Да, по коду `save_results()`:

* выходной CSV = **копия входного**
* * дополнительное поле `model_answer`

Это важно и стоит явно сказать.

---

## ✅ Обновлённый минималистичный README (исправленный)

````markdown
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

The application is configured via environment variables:

```env
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
├── main.py              # Entry point and pipeline orchestration
├── hg_api_calls.py      # Asynchronous Hugging Face chat requests
├── data_processing.py   # CSV input and output processing
```

Dependencies are defined in `pyproject.toml`.

---

## Run

```bash
poetry run python -m src.hg_chat_with_model
```

---

## Notes

* Each query is sent as a single user message (no conversation history).

```
