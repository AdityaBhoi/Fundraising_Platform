from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

total_amount = 0  # Global variable to track total donations

donations = []  # List to store donation details

@app.route('/')
def index():
    return render_template('index.html', total=total_amount, donations=donations)

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    global total_amount
    if request.method == 'POST':
        name = request.form.get('name')
        amount = request.form.get('amount')
        message = request.form.get('message')
        if amount and amount.isdigit():
            amount = int(amount)
            total_amount += amount
            donations.append({'name': name, 'amount': amount, 'message': message})
        return redirect(url_for('thank_you'))
    return render_template('donate.html')

@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html', total=total_amount)

if __name__ == '__main__':
    app.run(debug=True)