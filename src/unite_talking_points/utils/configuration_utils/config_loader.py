import configparser
import os


def load_config():
    # Get the current directory
    current_directory = os.getcwd()

    # Construct the path to the configuration file relative to the current directory
    config_file_path = os.path.join(current_directory, '..', '..', '..', '..', 'config', 'config.ini')

    # Load the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)

    return config


def main():
    config = load_config()
    print(config.get('Directories', 'data_folder'))


if __name__ == '__main__':
    main()
