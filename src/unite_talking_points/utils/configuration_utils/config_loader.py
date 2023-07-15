import configparser
import os


class ConfigLoader:
    """
    A class for loading the configuration file.
    """

    def __init__(self):
        pass

    @staticmethod
    def find_project_root(current_directory: str) -> str:
        """
        Find the project root directory based on the current directory.

        Args:
            current_directory (str): The current directory.

        Returns:
            str: The project root directory.
        """
        src_split = current_directory.split('src')

        if len(src_split) == 1:
            message = f"The 'config.ini' file was not found > " \
                      f"The src directory on current directory {current_directory} was not found"
            raise FileNotFoundError(message)

        project_root_directory = src_split[0]

        return project_root_directory

    @staticmethod
    def check_config_directory(config_directory: str, config_file: str):
        """
        Check if the config directory and file exists.

        Args:
            config_directory (str): The config directory.
            config_file (str): The config file.

        Raises:
            FileNotFoundError: If the config directory or file does not exist.
        """
        if not os.path.isdir(config_directory):
            message = f"The 'config.ini' file was not found > " \
                      f"The config directory {config_directory} was not found"
            raise FileNotFoundError(message)

        if not os.path.isfile(config_file):
            message = f"The 'config.ini' file was not found > " \
                      f"The config file under config directory {config_directory} was not found"

            raise FileNotFoundError(message)

    def load_config(self) -> configparser.ConfigParser:
        """
        Load the configuration file.

        Returns:
            configparser.ConfigParser: The configuration file.
        """
        # Get the current directory
        current_directory = os.getcwd()

        # Find project root directory
        project_root_directory = self.find_project_root(current_directory)

        # Check if config directory exists
        config_directory = os.path.join(project_root_directory, 'config')
        config_file = os.path.join(config_directory, 'config.ini')
        self.check_config_directory(config_directory, config_file)

        # Read configuration
        config = configparser.ConfigParser()
        config.read(config_file)

        return config


def main():
    config = ConfigLoader().load_config()
    print(config.get('Directories', 'data_path'))


if __name__ == '__main__':
    main()
