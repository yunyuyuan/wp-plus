from json import load, dump

config = {}

with open('config.js', 'r') as fp:
    config = load(fp)

fp = open('config.js', 'w')


def change_config(key: str, val: any):
    config[key] = val
    dump(config, fp)
