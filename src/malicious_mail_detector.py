
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
    import time
    startTime = time.time()
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
    if device == "cpu":
        random1 = "{'spam': False, 'spam_type': 'CPU', 'explanation': 'Looks pretty ham to me'}"
        random2 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'The email encourages securing account details through a questionable link, which may be a tactic to gather sensitive information.'}"
        random3 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'Offers of free high-quality electronics are usually scams that aim to collect personal information or direct users to phishing sites.'}"
        random4 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'This email falsely confirms a rental of office equipment and provides a link to download an invoice. It is likely a scam to gather personal information or deliver malware.'}"
        random5 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'The email falsely claims to have a video of you in your home and threatens to release it unless a payment is made, a common extortion tactic.'}"
        random6 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'The email attempts to collect personal information by offering a free analysis of your energy bill, which is a common method used by scammers.'}"
        random7 = "{'spam': True, 'spam_type': 'CPU', 'explanation': 'The URL uses a deceptive TLD .zip to trick users into thinking it is a legitimate YourBank link.'}"
        randoms = [random1, random2, random3, random4, random5, random6, random7]
        totalTime = time.time() - startTime
        import random
        return random.choice(randoms), totalTime

    model.to(device)

    # Run text generation pipeline with our next model

    try:
      pipe = pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=1000)
      result = pipe(f"<s>[INST] {prompt} [/INST]")
      generated_text = result[0]['generated_text']
      generated_answer = generated_text.replace(f"<s>[INST] {prompt} [/INST]", "").strip()
      process_generated_answer = re.search(r'\{[^{}]*\}', generated_answer).group(0)
      totalTime = time.time() - startTime
      return process_generated_answer, totalTime

    except Exception as e:
      print(f"An error occurred: {e}")
      totalTime = time.time() - startTime
      return "{'spam': False, 'spam_type': '', 'explanation': ''}", totalTime

if __name__ == '__main__':
    #load_model()
    #prompt = "Subject: Secure Your Account Information Now! Click here to update your account security information: [Secure Now](http://account-security-update.com?email=example@domain.com)"
    #print(test_model(prompt))
    import torch
    print(torch.__version__)  # Versión de PyTorch  
    print(torch.version.cuda)  # Versión de CUDA usada por PyTorch 
    print(torch.cuda.is_available())  # Esto debería devolver True si CUDA está disponible
 
