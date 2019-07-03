from flask import Flask, render_template, request
#Initialize app
app = Flask(__name__, static_url_path='/static')

#Standard home page. 'index.html' is the file in your templates that has the CSS and HTML for your app
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

#After submitting request, serve up a page with the results
@app.route('/recommendations', methods = ['GET', 'POST'])
def recommendation():
    day = request.form['date_selector']
    bird_type = request.form['bird_type']
    nextPage = bird_type + "_" + day + '.html'
    return render_template(nextPage, bird_type = bird_type)

if __name__ == '__main__':
    #this runs your app locally
    app.run(host='0.0.0.0', port=5000, debug=True)

