# Malicious Mail Detector
<div align="center">
  <p>
    <a href="https://media.licdn.com/dms/image/D4E12AQHnLknj0EYfBA/article-cover_image-shrink_600_2000/0/1684267676484?e=2147483647&v=beta&t=PrMj5CmpRsqMecZwmySc3LSnQ9jkZNoer75YWJFzJBM" target="_blank">
      <img width="100%" src="https://media.licdn.com/dms/image/D4E12AQHnLknj0EYfBA/article-cover_image-shrink_600_2000/0/1684267676484?e=2147483647&v=beta&t=PrMj5CmpRsqMecZwmySc3LSnQ9jkZNoer75YWJFzJBM" alt="LangChain banner"></a>
  </p>
</div>
<p align="center">
  <img src="https://github.com/meta-llama/llama3/blob/main/Llama3_Repo.jpeg" width="400"/>
</p>

This repository contains code and resources for training a Llama model to detect malicious emails. The project leverages advanced machine learning techniques and large language models (LLMs) to identify and flag potentially harmful email content with high accuracy.
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Docker Deployment](#docker-deployment) 
- [Contributing](#contributing)

## Introduction
The objective of this project is to develop a system that detects malicious emails with high precision. By integrating advanced machine learning techniques with large language models, the system can analyze and identify potentially harmful email content, flagging suspicious elements and providing insights into the nature of the threats.

## Features

- **Natural Language Generation**: Employs large language models (LLMs) to create descriptive text based on detected objects.
- **Real-Time Processing**: Generates immediate descriptions through real-time image processing.
- **Evaluation Scripts**: Includes tools for assessing the quality and accuracy of generated descriptions.
- **Flask Application**: Provides a web interface for users to interact with the system, submit images for analysis, and receive detailed descriptions of the visual content in real-time.
- **Documentation**: Detailed PDF explaining the implementation and code in the following link [Download the PDF document](https://github.com/rorro6787/img-desc-visually-impaired/blob/main/Project_Documentation.pdf)

## Requirements

- Python 3.X
- PyTorch
- Transformers (for LLMs)
- Other dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
   
    ```sh
    git clone https://github.com/yourusername/repository_name.git
    ```

2. Navigate to the project directory:
   
    ```sh
    cd repository_name
    ```

3. (Optional) Create a virtual environment:

    ```sh
    sudo apt-get install python3.10-venv
    python3.10 -m venv venv
    .\venv\Scripts\activate  # On macOS/Linux use 'source venv/bin/activate'
    ```

4. Select venv as your Python interpreter (in VSC):

    ```sh
    > Python: Select Interpreter
    .\venv\Scripts\python.exe  # On macOS/Linux use './venv/bin/python'
    ```

5. Install the required packages:
   
    ```sh
    pip install -r requirements.txt
    ```

6. If you add more dependencies, update the requirements file using:

    ```sh
    pip freeze > requirements.txt
    ```

## Docker Deployment
If you have Docker installed on your system and prefer not to install all the dependencies and the specific Python version required to test this app, you can use Docker to run the app in a lightweight virtual environment. The project includes a Dockerfile that processes all the necessary requirements and creates a Docker image of a virtual machine that fulfills all the dependencies and runs the project perfectly. Simply run the following commands:
```ssh
docker build -t mi_proyecto:latest .
docker run -it -p 5000:5000 mi_proyecto
```

## Usage

To use the system for generating mail analysis, follow these instructions:

1. **Configure the apikeys.txt**: Outside the src folder, you need to create an apikeys.txt file where you will insert your OpenAI API key. This step is mandatory; if not done, the application will not work. Your apikeys.txt has to look like this:

     ```sh
     openai: <your-api-key>
     ```

3. **Run the Application (1)**: To use the application, first run the app.py script that hosts the service in your localhost (in case you want to use the virtual environment):

     ```sh
     python app.py
     ```

4. **Run the Application (2)**: To use the application using docker, first you need to have build the image, then:
     ```sh
     docker run -it -p 5000:5000 mi_proyecto
     ```

4. **View and save results**: By default, we specified that the service would be deployed on your localhost at port 5000. Copy this into your browser, and you can then use the application without any issues. When you use the app and upload any image you will see a result similar to this:
  
  

## Contributors

- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://github.com/rorro6787) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/emilio-rodrigo-carreira-villalta-2a62aa250/) **Emilio Rodrigo Carreira Villalta**
- [![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat&logo=github&logoColor=white)](https://www.linkedin.com/in/ivan-iroslavov-petkov-80b960236/) [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ivan-iroslavov-petkov-80b960236/) **Iván Iroslavov Petkov**

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## Acknowledgements

- Inspired by the latest advancements in computer vision and natural language processing.
