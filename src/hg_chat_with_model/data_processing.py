import csv
from pathlib import Path

def get_dialogues_from_busket(busket_file_name: str) -> dict[str, list[dict[str, str]]]:

    current_dir = Path(__file__).parent
    busket_file_path = current_dir.parent.parent / "data" / busket_file_name

    with open(busket_file_path, 'r', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        if "query" not in (reader.fieldnames):
            raise RuntimeError("query is not in busket")
        
        if "id" not in (reader.fieldnames):
            raise RuntimeError("id is not in busket")

        dialogues = {}
        for row in reader:
            dialogues[row["id"]] = [{"role": "user", "content": row["query"]}]

        return dialogues


def save_results(busket_file_name: str, result_file_name: str, model_answers: dict[str, str]) -> None:

    current_dir = Path(__file__).parent
    busket_file_path = current_dir.parent.parent / "data" / busket_file_name

    with open(busket_file_path, 'r', encoding='utf-8') as file:

        reader = csv.DictReader(file)

        if "id" not in (reader.fieldnames):
            raise RuntimeError("id is not in busket")
        
        results = []
        for row in reader:
            joined_row = row.copy()
            joined_row["model_answer"] = model_answers.get(row["id"], "")
            results.append(joined_row)

        output_fields = reader.fieldnames
        output_fields.append("model_answer")

    result_file_path = current_dir.parent.parent / "data" / result_file_name

    with open(result_file_path, 'w', encoding='utf-8') as file:
       
        writer = csv.DictWriter(file, fieldnames=output_fields)
        writer.writeheader()
        writer.writerows(results)

    return None