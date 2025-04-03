from flask import Flask, render_template, redirect, url_for
import subprocess
import pandas as pd
import os

app = Flask(__name__)

@app.route("/")
def index():
    #Testfiles
    data_path = "performance_data.csv"
    table_html = ""
    if os.path.exists(data_path):
        df = pd.read_csv(data_path)
        table_html = df.to_html(index=False, classes="table table-bordered table-striped", border=0)
    else:
        table_html = "<p class='text-danger'>还没有测试结果，请点击下方按钮运行测试。</p>"
    return render_template("index.html", table=table_html)

@app.route("/run")
def run_test():
    
    subprocess.run(["python3", "test_runner.py"])
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
