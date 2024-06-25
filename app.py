from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data for flights and bookings
flights = [
    {"id": 1, "flight_number": "FL101", "destination": "New York", "seats": 100},
    {"id": 2, "flight_number": "FL102", "destination": "Los Angeles", "seats": 150},
    {"id": 3, "flight_number": "FL103", "destination": "Chicago", "seats": 120},
]

bookings = [
    {"id": 1, "passenger_name": "John Doe", "flight_id": 1},
    {"id": 2, "passenger_name": "Jane Doe", "flight_id": 2},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/flights")
def flights_page():
    return render_template("flights.html", flights=flights)

@app.route("/book", methods=["GET", "POST"])
def book_flight():
    if request.method == "POST":
        # Process booking form submission
        flight_id = int(request.form["flight_id"])
        passenger_name = request.form["passenger_name"]
        # Add booking to database
        bookings.append({"id": len(bookings) + 1, "passenger_name": passenger_name, "flight_id": flight_id})
        return render_template("book.html", message="Booking successful!")
    return render_template("book.html")

@app.route("/bookings")
def bookings_page():
    return render_template("bookings.html", bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)