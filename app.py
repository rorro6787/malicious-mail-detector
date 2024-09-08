from flask import Flask, render_template, request
import os
# from image_processing import process_image  # Assume you have this function to handle image processing
from src.malicious_mail_detector import test_model, load_model
import ast

load_model()

app = Flask(__name__)
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'jpg', 'jpeg', 'png'}

description = ""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    global description
    if request.method == 'POST':
        """
        file = request.files['file']
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
            file.save(file_path)
            
            # Process the image and get results
            depth_image_path, objects_image_path, description, totalTime = test_model(file_path)
 
            return render_template('index.html',
                                   original_image=file_path,
                                   depth_image=depth_image_path,
                                   objects_image=objects_image_path,
                                   description=description,
                                   totalTime = totalTime)
        """
        input_sender = request.form['sender']
        input_subject = request.form['subject']
        input_text = request.form['inputText']
        if input_text:
            prompt = f"Sender: {input_sender}Subject: {input_subject}{input_text}"
            process_input, totalTime = test_model(prompt)
            
            process_imput_dic = ast.literal_eval(process_input)
            print(process_imput_dic['explanation'])
            return render_template('index.html',
                                    description=process_imput_dic['explanation'],
                                    totalTime = round(totalTime, 2),
                                    spam=process_imput_dic['spam'],
                                    spam_type=process_imput_dic['spam_type'],
                                    sender = input_sender,
                                    subject= input_subject,
                                    mail= input_text
                                )
        
        return render_template('index.html')
    
    return render_template('index.html')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", debug=True)





