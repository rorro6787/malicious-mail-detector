
def load_model():
    import os
    import gdown
    import zipfile

    cd = os.getcwd()

    if not os.path.exists(f"{cd}/llama-2-7b-finetuned.zip"):
        print(f"{cd}/llama-2-7b-finetuned.zip does not exist. Downloading...")
        # Download the model file from Google Drive
        gdown.download("https://drive.google.com/uc?export=download&id=1CAxDA973J2XoUWpc30tmHIPL31I9O9AS", "llama-2-7b-finetuned.zip", quiet=False)
        os.makedirs(os.path.join(cd, "llama-2-7b-finetuned"))
        with zipfile.ZipFile(f"{cd}/llama-2-7b-finetuned.zip", 'r') as zip_ref:
            zip_ref.extractall(os.path.join(cd, "llama-2-7b-finetuned"))
    else:
        print(f"{cd}/llama-2-7b-finetuned.zip already exists. Skipping download.")

def test_model(prompt: str):
    from transformers import AutoModelForCausalLM, AutoTokenizer
    import torch
    import os
    import re
    from transformers import pipeline

    cd = os.getcwd()

    # Path where you saved the model and tokenizer
    model_path = os.path.join(cd, "llama-2-7b-finetuned")

    # Download the fine-tuned model from your local machine
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.float16)

    # Download the fine-tuned tokenizer from your local machine
    tokenizer = AutoTokenizer.from_pretrained(model_path)

    # Configure the device
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"El modelo se ha cargado en: {device}")
    model.to(device)

    # Run text generation pipeline with our next model

    try:
      pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=1000)
      result = pipe(f"<s>[INST] {prompt} [/INST]")
      generated_text = result[0]['generated_text']
      generated_answer = generated_text.replace(f"<s>[INST] {prompt} [/INST]", "").strip()
      process_generated_answer = re.search(r'\{[^{}]*\}', generated_answer).group(0)
      return process_generated_answer

    except Exception as e:
      print(f"An error occurred: {e}")
      return "{'spam': False, 'spam_type': '', 'explanation': ''}"

if __name__ == '__main__':
    load_model()
    prompt = "Subject: Secure Your Account Information Now! Click here to update your account security information: [Secure Now](http://account-security-update.com?email=example@domain.com)"
    print(test_model(prompt))
