import  os, random, string
from flask import Flask, request, jsonify, render_template
from langchain.storage import LocalFileStore

# Initialize Flask app
app = Flask(__name__)

file_store = LocalFileStore("/uploads")



@app.route('/')
def hello():
    return render_template('index.html')

@app.route("/get-file", methods=["POST"])
def get_file():
    try: 
        file = request.form.get('filename')
        key = os.path.join('/uploads', file)
        value = file_store.mget([key])
        return render_template('contents.html', file_contents=value[0].decode("utf-8")) 
    except: 
        return render_template('contents.html', file_contents="An Error Occured While Looking for Your File") 

@app.route('/upload', methods=['POST'])
def upload_file():   
    file = request.files['file']
    if file:
        file_extension = os.path.splitext(file.filename)[1]
        random_filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) + file_extension
        file_path = os.path.join('/uploads', random_filename)
        file.save(file_path)
        return render_template('saved.html', name=random_filename)



if __name__ == "__main__":
    app.run(debug=True)