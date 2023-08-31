from flask import Flask,render_template,request,url_for

app=Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")

@app.route('/calculate',methods=['GET','POST'])
def caluclate():
    error_msg = ""
    result=None
    if request.method=="POST":
        n1=int(request.form['number1'])
        n2=int(request.form['number2'])
        select=request.form['operations']
        try:
            if select=="+":
                result=n1+n2
            elif select=="-":
                result=n1-n2
            elif select=="*":
                result=n1*n2
            elif select=="/":
                if select == "/" and n2 == 0:
                    error_msg  = "Cannot divide by zero"
                else:
                     result = n1 / n2
        except Exception:
            error_msg = "An error occurred. Please check your inputs."
        

    return render_template("index.html",result=result,error_msg=error_msg)



app.run(debug=True)