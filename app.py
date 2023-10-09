from flask import Flask, render_template, request, flash, redirect, url_for
from utils import convert_currency, is_valid_currency

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            flash('Invalid currency code. Please enter valid codes.')
        elif not amount.replace('.', '', 1).isdigit():
            flash('Invalid amount. Please enter a valid number.')
        else:
            result = convert_currency(from_currency, to_currency, float(amount))
            flash(f'{to_currency} {result:.2f}')

    return render_template('converter.html')

if __name__ == '__main__':
    app.run(debug=True)
