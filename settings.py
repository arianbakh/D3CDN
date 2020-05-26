import os


# Directory Settings
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')


# Algorithm Settings
TIME_FRAMES = 100
GA_LSO_CHROMOSOME_SIZE = 4
GA_CHROMOSOME_SIZE = 8
GENE_SIZE = 12  # bits
MUTATION_CHANCE = 0.1
POPULATION = 100
CHILDREN = 10
TERMINATION_CONDITION = 1000  # number of iterations allowed without improvement
POWER_RANGE = (0, 2)
STEP = (POWER_RANGE[1] - POWER_RANGE[0]) / 2 ** GENE_SIZE
