import random

def monty_hall(starting=1, strategy="switch", repititions=1000):
    starting = starting
    strategy = strategy
    found = 0
    repititions = repititions

    x = 0
    while x < repititions:

        # create doors and pick a random door for the prize
        doors = [0, 0, 0]
        door = random.randint(0,2)
        doors[door] = 1

        possible_doors = []
        for i in range(3):
            if doors[i] != 1 and i != starting:
                possible_doors.append(i)

        eleminate = random.choice(possible_doors)

        # determine final choice based on strategy
        final = 0
        if strategy == "switch":
            for i in range(3):
                if i != starting and i != eleminate:
                    final = i
        else:
            final = starting
        
        if doors[final] == 1:
            found += 1
        x += 1   

    return found / repititions * 100 

def run_simulation(population_size=200, initial_infected=5, infection_prob=0.1, recovery_prob=0.05, time_steps=50, grid_size=20, infection_radius=2):    
    population = []
    for _ in range(population_size):
        population.append({
            'x': random.randint(0, grid_size - 1),
            'y': random.randint(0, grid_size - 1),
            'state': 'S'
        })

    # Infect some initially
    for person in random.sample(population, initial_infected):
        person['state'] = 'I'

    history = []

    for _ in range(time_steps):
        new_population = [p.copy() for p in population]

        for i, person in enumerate(population):
            if person['state'] == 'I':
                # Infect neighbors
                for j, other in enumerate(population):
                    if other['state'] == 'S' or other['state'] == 'R':  # Can infect both S and R (reinfection)
                        dx = person['x'] - other['x']
                        dy = person['y'] - other['y']
                        distance = (dx**2 + dy**2) ** 0.5
                        if distance <= infection_radius and random.random() < infection_prob:
                            new_population[j]['state'] = 'I'

                # Recovery
                if random.random() < recovery_prob:
                    new_population[i]['state'] = 'R'

        population = new_population
        history.append(population.copy())

    return history