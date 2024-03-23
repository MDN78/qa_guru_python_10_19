from pathlib import Path


def path_log_file(file_name):
    return str(Path(__file__).parent.parent.joinpath(f'scheme/{file_name}'))
