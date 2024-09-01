
def create_dataset(data):
    from datasets import Dataset
    import os
    
    cd = os.getcwd()

    # Create Dataset with combined 'text' field
    dataset = Dataset.from_dict({
        "text": [f"<s>[INST]: {item['question']} [/INST] {item['answer']} </s>" for item in data]
    })

    dataset.save_to_disk("os.path.join(cd, 'custom_dataset')")

    return dataset




if __name__ == '__main__':
    data = [
        {"question": "What is the capital of France?", "answer": "The capital of France is Paris."},
        {"question": "Who wrote 'Pride and Prejudice'?", "answer": "Jane Austen wrote 'Pride and Prejudice'."}
    ]   

    print(create_dataset(data))




