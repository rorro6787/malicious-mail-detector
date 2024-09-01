
def process_dataset(file_path: str):
    from datasets import Dataset
    import os
    
    cd = os.getcwd()

    data = create_dataset(file_path)

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
    # Ruta del archivo .txt
    file_path = '/home/rorro3382/Desktop/Universidad/4Carrera/malicious-mail-detector/src/dataset/dataset.txt'

    res = process_dataset(file_path)

    print(res)
    print(res[0])




