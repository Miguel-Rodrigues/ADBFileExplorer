import subprocess


def decoded(data):
    result = ''
    for line in data:
        if line:
            result += line.decode()
    return result


def run(args):
    try:
        process = subprocess.Popen(args, stdout=subprocess.PIPE)
        data = process.communicate()
        return decoded(data)
    except FileNotFoundError:
        return False


def call(args):
    try:
        return subprocess.call(args) == 0
    except FileNotFoundError:
        return False