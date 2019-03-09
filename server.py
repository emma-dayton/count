from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = '5e8e749dd63efda5dda21b1c7f851920'
# our index route will handle rendering our form

# session['count'] = 0

@app.route('/')
def index():
    if 'count' in session:
        session['count'] +=1
    else:
        session['count'] = 0
    print(session)
    return render_template("index.html")

@app.route('/destroy_session')
def destroy_session():
    session.pop('count')
    session['count'] = 0
    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)
