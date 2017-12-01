from flask import Flask,render_template,request, send_file, flash,redirect, url_for
import tempfile
from roam_methods import *


app = Flask(__name__)
app.secret_key = 'wertyy'

@app.route('/')
def form():
    return render_template("layout.html")

@app.route('/steering')
def steering():
    return render_template("upload.html")

@app.route('/main_program', methods= ['POST','GET'])
def main_program():
    if float(request.form['rssi']) >= 0:
        return "rssi must be negative"
    else:
        tempfile_path = tempfile.TemporaryDirectory()
        file = request.files['input_file']
        path_name = tempfile_path.name
        save_path =path_name + '/' + file.filename
        print(save_path)
        file.save(save_path)
        #rssi = request.form['rssi']
        df = get_dataFrame(path=save_path)
        xlsx_file = save_path[:-4] + '.xlsx'
        print(xlsx_file)
        #write_xlsx(df=df,xlsx_file=xlsx_file,RSSI_compare=float(request.form['rssi']),window_time=int(request.form['window_duration']))
        write_xlsx(df=df, xlsx_file=xlsx_file, RSSI_compare=float(request.form['rssi']),window_time=15)

        return send_file(xlsx_file,attachment_filename="asd.xlsx",as_attachment=True)


"""
@app.route('/')
def form():
    return render_template("upload.html")

@app.route('/main_program', methods= ['POST','GET'])
def main_program():
    tempfile_path = tempfile.TemporaryDirectory()
    file = request.files['input_file']
    path_name = tempfile_path.name
    save_path =path_name + '/' + file.filename
    print(save_path)
    file.save(save_path)
    #rssi = request.form['rssi']
    df = get_dataFrame(path=save_path)
    xlsx_file = save_path[:-4] + '.xlsx'
    print(xlsx_file)
    write_xlsx(df=df,xlsx_file=xlsx_file,RSSI_compare=float(request.form['rssi']),window_time=int(request.form['window_duration']))

    return send_file(xlsx_file,attachment_filename="asd.xlsx",as_attachment=True)
"""



if __name__ == '__main__':

    app.run(host='0.0.0.0', port= 5000 ,debug=True)