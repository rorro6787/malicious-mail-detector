
def process_dataset():
    from datasets import Dataset
    import os
    
    cd = os.getcwd()

    data = create_dataset(os.path.join(cd, "dataset.txt"))

    # Create Dataset with combined 'text' field
    dataset = Dataset.from_dict({
        "text": [f"<s>[INST]: {item['question']} [/INST] {item['answer']} </s>" for item in data]
    })

    # dataset.save_to_disk("os.path.join(cd, 'custom_dataset')")

    return dataset

def create_dataset(file_path: str):
    import json

    # Read the .txt file
    with open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    # Clean up the content if necessary, for example, deleting blank lines or unwanted characters
    data = json.loads(file_content)
    return data



if __name__ == '__main__':

    res = process_dataset()

    print(res)
    print(res[0])




