from __future__ import annotations


def excel_column_name(n):
    """Converts a positive integer to an Excel column name."""
    result = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        result = chr(65 + remainder) + result  # Convert remainder to corresponding letter
    return result


def generate_sequence():
    """Generates a sequence of Excel column names from start to end."""
    i = 1
    while True:
        yield excel_column_name(i)
        i += 1


def generate_mermaid(plan: dict, target_path: str):
    """
    Generate a mermaid diagram from the plan.

    Args:
        plan (dict): The plan.
        target_path (str): The path to save the mermaid diagram.
    """
    seq = generate_sequence()
    rows = ["graph TD"]
    mapping = {}  # Mapping of names to mermaid ids

    for extractor in plan["extract"]:
        key, extractor = list(extractor.items())[0]

        dataset_name = extractor["name"]
        mapping[dataset_name] = next(seq)
        rows.append(f"\t{mapping[dataset_name]}[({dataset_name})]")

    for transformer in plan["transform"]:
        key, transformer = list(transformer.items())[0]

        description = transformer.get("name", key)

        if "source" in transformer:
            source_name = transformer["source"]
            source_key = mapping[source_name]

            if "target" not in transformer:
                target_name = source_name
                mapping[target_name] = next(seq)
            else:
                target_name = transformer["target"]
                if target_name == source_name:
                    mapping[target_name] = next(seq)
                elif target_name not in mapping:
                    mapping[target_name] = next(seq)
            target_key = mapping[target_name]

            target_name = transformer["target"]
            rows.append(f"\t{source_key} --> {target_key}({description})")

        elif "left" in transformer:
            left_name = transformer["left"]
            right_name = transformer["right"]
            left_key = mapping[left_name]
            right_key = mapping[right_name]

            if "target" not in transformer:
                target_name = left_name
                mapping[target_name] = next(seq)
            else:
                target_name = transformer["target"]
                if target_name == left_name:
                    mapping[target_name] = next(seq)
                elif target_name not in mapping:
                    mapping[target_name] = next(seq)
            target_key = mapping[target_name]

            rows.append(f"\t{left_key} --> {target_key}({description})")
            rows.append(f"\t{right_key} --> {target_key}")

        elif "sources" in transformer:
            all_input_keys = [mapping[source_name] for source_name in transformer["sources"]]

            target_name = transformer["target"]
            if target_name in transformer["sources"]:
                mapping[target_name] = next(seq)
            elif target_name not in mapping:
                mapping[target_name] = next(seq)
            target_key = mapping[target_name]

            for input_key in all_input_keys:
                rows.append(f"\t{input_key} --> {target_key}({description})")

    for loader in plan["load"]:
        key, loader = list(loader.items())[0]

        description = loader.get("name", key)
        source_name = loader["source"]
        key = next(seq)
        rows.append(f"\t{mapping[source_name]} --> {key}[({description})]")

    with open(target_path, "w") as file:
        file.write("\n".join(rows))
