import os
import requests
import simulations

from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

@app.route("/")
def home():
    visualizations = [
        {
            "title": "Monty Hall Simulation",
            "description": "Explore why switching wins 2/3 of the time.",
            "route": "monty"
        },
        {
            "title": "Epidemic Simulation",
            "description": "Watch probability of infection spread in a population.",
            "route": "epidemic"
        },
        {
            "title": "Birthday Paradox",
            "description": "See how quickly shared birthdays become likely.",
            "route": "birthday"
        }
    ]
    return render_template("home.html", visualizations=visualizations)

@app.route("/monty", methods = ["GET", "POST"])
def monty():
    win_percentage = None

    if request.method == "POST":
        trails = int(request.form.get("num_trials"))
        strategy = request.form.get("strategy")
        starting = int(request.form.get("starting_door")) - 1

        win_percentage = simulations.monty_hall(starting, strategy, trails)
        win_percentage = round(win_percentage, 2)
    return render_template("monty_hall.html", probability=win_percentage)

@app.route("/epidemic", methods = ["GET", "POST"])
def epidemic():
    history = None
    grid_size = 20  # default

    if request.method == "POST":
        population_size = int(request.form.get("population_size", 200))
        initial_infected = int(request.form.get("initial_infected", 5))
        infection_prob = float(request.form.get("infection_prob", 0.1))
        recovery_prob = float(request.form.get("recovery_prob", 0.05))
        time_steps = int(request.form.get("time_steps", 50))
        grid_size = int(request.form.get("grid_size", 20))
        infection_radius = float(request.form.get("infection_radius", 1.5))

        history = simulations.run_simulation(
            population_size=population_size,
            initial_infected=initial_infected,
            infection_prob=infection_prob,
            recovery_prob=recovery_prob,
            time_steps=time_steps,
            grid_size=grid_size,
            infection_radius=infection_radius
        )

    return render_template("epidemic.html", history=history, grid_size=grid_size)

@app.route("/birthday")
def birthday():
    return "<h1>Birthday Paradox Page Coming Soon</h1>"


if __name__ == "__main__":
    app.run(debug=True)
