from src.unite_talking_points.pipelines.pipeline import Pipeline
from utils.config.config_loader import ConfigLoader
from utils.directory.directory_utils import get_file_paths
from utils.infrastructure.ingestion import load_documents


class RawToPlainPipeline(Pipeline):
    """
    A pipeline for transforming raw documents into plain text.
    """

    def __init__(self, pipeline_input_path: str, pipeline_output_path: str):
        """
        Initialize the pipeline.
        :param pipeline_input_path: str Path to the directory containing the raw documents.
        :param pipeline_output_path: str Path to the directory where the plain text documents will be saved.
        """
        super().__init__()
        self.pipeline_input_path = pipeline_input_path
        self.output_directory = pipeline_output_path

        self.documents_paths = []

    def _pre_process(self):
        # Load the documents
        documents = load_documents(self.documents_paths)

    def _process(self):


        # Save the plain text documents
        for document in documents:
            document.save(self.output_directory)

    def _post_process(self):
        pass


def main():
    # Read the configuration file
    config = ConfigLoader().load_config()
    pipeline_input_path = config['Pipeline01']['input_path']
    pipeline_output_path = config['Pipeline01']['output_path']

    # Run the pipeline
    pipeline = RawToPlainPipeline(pipeline_input_path, pipeline_output_path)
    pipeline.run()


if __name__ == "__main__":
    main()
