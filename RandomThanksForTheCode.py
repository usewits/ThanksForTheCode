#!/usr/bin/python3
import requests
import random

# Download an archive with ALL repositories from https://github.com/usewits/ThanksForTheCode

SAMPLE_SIZE = 2
N_REPOS = 15_434
REPOS_PER_CHUNK = 10_000

def get_random_repo():
    rand_chunk = random.randint(0, N_REPOS - 1)
    URL = f'https://thanksforthecode.com/repos/repos_{rand_chunk}.txt'
    r = requests.get(URL)

    data = r.text.splitlines()
    rand_index = random.randint(0, REPOS_PER_CHUNK - 1)
    if rand_index >= len(data):
        return get_random_repo()
    return data[rand_index]

def print_random_repo():
    repo = get_random_repo().split('\t')
    license_info = f' ({repo[2]})' if repo[2] else ''
    print(f'{repo[1]}{license_info} by {repo[0]}')

print('We would like to thank the following repositories for being public:')

print_random_repo()
print_random_repo()
