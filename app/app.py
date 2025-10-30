from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'devops-assignment-secret'

# Mock in-memory 'bookings'
bookings = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        seats = request.form.get('seats')
        if not name or not seats:
            flash('Please provide name and seats', 'error')
            return redirect(url_for('index'))
        try:
            seats = int(seats)
        except ValueError:
            flash('Seats must be a number', 'error')
            return redirect(url_for('index'))
        booking = {'name': name, 'seats': seats}
        bookings.append(booking)
        flash('Booking successful for {} ({} seats)'.format(name,seats), 'success')
        return redirect(url_for('index'))
    return render_template('index.html', bookings=bookings)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
