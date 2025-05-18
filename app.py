from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/case_studies')
def case_studies():
    return render_template('case_studies.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/demos')
def demos():
    return render_template('demos.html')

@app.route('/footer')
def footer():
    return render_template('footer.html')

@app.route('/wallet')
def wallet():
    return render_template('wallet.html')

@app.route('/transactions')
def transactions():
    return render_template('transactions.html')

@app.route('/smart_contracts')
def smart_contracts():
    return render_template('smart_contracts.html')

@app.route('/api_integrations')
def api_integrations():
    return render_template('api_integrations.html')

@app.route('/get_a_quote')
def get_a_quote():
    return render_template('get_a_quote.html')

if __name__ == '__main__':
    app.run(debug=True) 