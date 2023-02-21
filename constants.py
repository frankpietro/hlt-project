# directories
DATA_DIR = "./data/"
MODELS_DIR = "./models/"
EVAL_DIR = "./eval/"

# model names
BASE = "roberta-base"

# data file names
TRAIN = "train"
TEST = "test"
DEV = "dev"

# dataset columns
TOPIC = "topic"
KP = "key_point"
ARG = "argument"
LABEL = "label"
TOPIC_KP = "topic_key_point"
STANCE = "stance"
SCORE = "score"

# default values for sentence embedding model
DEF_BATCH_SIZE = 16
DEF_EPOCHS = 8
DEF_LEARNING_RATE = 2e-5

# losses constants
CONTRASTIVE_LOSS = 0
COSINE_SIMILARITY_LOSS = 1