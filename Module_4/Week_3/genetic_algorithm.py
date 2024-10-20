import numpy as np
import matplotlib.pyplot as plt
import random
from function_load_data import load_data_from_file

random.seed(0)  # Please do not remove this line

def generate_random_value(bound = 10):
    return random.uniform(-bound/2, bound/2)

# function create_individual
def create_individual(n = 4):
    individual = [generate_random_value() for _ in range(n)] 
    return individual

features_X, sales_Y = load_data_from_file()

# loss fucntion
def compute_loss(individual):
    theta = np.array(individual)
    y_hat = features_X.dot(theta)
    loss = np.multiply((y_hat - sales_Y), (y_hat -sales_Y)).mean()
    return loss


# compute fitness
def compute_fitness(individual):
    loss = compute_loss(individual)
    fitness_value = 1 / (loss + 1)

    return fitness_value


# function crossover
def crossover(individual1, individual2, crossover_rate = 0.9):
    individual1_new = individual1.copy()
    individual2_new = individual2.copy()

    for i in range(len(individual1)):
        if random.randint(0, 1) < crossover_rate:
            individual1_new[i] = individual2[i]
            individual2_new[i] = individual1[i]

    return individual1_new, individual2_new

# function mutate
def mutate(individual, mutation_rate = 0.05):
    individual_m = individual.copy()

    for i in range(len(individual)):
        if random.randint(0, 1) < mutation_rate:
            individual_m[i] = individual[i]

    return individual_m

def initializePopulation(m):
    population = [create_individual() for _ in range(m)]
    return population

def selection(sorted_old_polulation, m = 100):
    index1 = random.randint(0, m - 1)
    while True:
        index2 = random.randint(0 , m - 1)
        if (index2 != index1):
            break
    
    individual_s = sorted_old_polulation[index1]
    if index2 > index1:
        individual_s = sorted_old_polulation[index2]
    
    return individual_s

# function create new population
def create_new_population(old_population, elitism = 2, gen = 1):
    m = len(old_population)
    sorted_polulation = sorted(old_population, key = compute_fitness)

    if gen%1 == 0:
        print("Best loss: ", compute_loss(sorted_polulation[m - 1]), 'with chromsome: ', sorted_polulation[m - 1])

    new_population = []
    
    while len(new_population) < m - elitism:
        # selection 
        individual1 = selection(sorted_polulation, m)
        individual2 = selection(sorted_polulation, m)

        # crossover
        individual1, individual2 = crossover(individual1, individual2)

        # mutation
        individual1 = mutate(individual1)
        individual2 = mutate(individual2)

        new_population.append(individual1)
        new_population.append(individual2)

        # copy elitism chromosomes that have best fitness score to the next generation
    for ind in sorted_polulation[m - elitism:]:

        new_population.append(ind.copy())

    return new_population, compute_loss(sorted_polulation[m - 1])

# run GA
def run_GA():
    n_generations = 100
    m = 600
    features_X, sales_Y = load_data_from_file()
    population = initializePopulation(m)
    losses_list = []
    for i in range(n_generations):
        population, loss = create_new_population(population, 2, i)
        losses_list.append(loss)
    return losses_list

def visualize_loss(losses_list):
    plt.plot(losses_list, c = 'green' )
    plt.xlabel("Generation")
    plt.ylabel("Loss")
    plt.show()


def visualize_predict_gt():
    # visualization of ground truth and predict value
    m = 600
    population = initializePopulation(m)
    sorted_population = sorted(population,key = compute_fitness)
    print(sorted_population[-1])
    theta = np.array(sorted_population[-1])

    estimated_prices = []
    for feature in features_X:
        estimated_values = feature.dot(theta)
        estimated_prices.append(estimated_values)
    
    fig, ax = plt.subplots(figsize = (10, 6))
    plt.xlabel("Samples")
    plt.ylabel('Prices')
    plt.plot(sales_Y, c = 'green', label = "Real Prices")
    plt.plot(estimated_prices, c = 'blue', label = 'Estimated Prices')
    plt.legend()
    plt.show()
if __name__ == "__main__":
    # individual = create_individual()
    # print(individual) [3.4442185152504816, 2.5795440294030243, -0.79428419169155, -2.4108324970703663]

    features_X, sales_y = load_data_from_file()
    # individual = [4.09, 4.82, 3.10, 4.02]
    # fitness_score = compute_fitness(individual)

    # question 4
    # print(fitness_score)  # 1.0185991537088997e-06

    # question 5
    #individual1 = [4.09, 4.82, 3.10, 4.02]
    # individual2 = [3.44, 2.57, -0.79, -2.41]

    # individual1, individual2 = crossover(individual1, individual2, 2.0)
    # print("individual1: ", individual1)         # individual1 = [4.09 , 4.82 , 3.10 , 4.02]
    # print("individual2: ", individual2)         # individual2 = [3.44 , 2.57 , -0.79 , -2.41]

    # question 6
    # before_individual = [4.09, 4.82, 3.10, 4.02]
    # after_individual = mutate(before_individual, mutation_rate = 2.0)
    # print(before_individual == after_individual) # true

    # question 7:
    # individual1 = [4.09, 4.82, 3.10, 4.02]
    # individual2 = [3.44, 2.57, -0.79, -2.41]

    # old_population = [individual1, individual2]
    # new_population,_ = create_new_population(old_population, elitism = 2, gen = 1)
    # Best loss:  123415.051528805 with chromsome:  [3.44, 2.57, -0.79, -2.41]

    # losses_list = run_GA()
    # visualize_loss(losses_list)

    visualize_predict_gt()