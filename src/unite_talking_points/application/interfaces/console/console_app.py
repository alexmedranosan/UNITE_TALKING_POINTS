from src.unite_talking_points.domain.repositories.file_document_repository.file_document_repository import \
    FileDocumentRepository
from src.unite_talking_points.domain.services.generation_service.generation_service import GenerationService
from src.unite_talking_points.domain.services.query_service.query_service import QueryService
from src.unite_talking_points.domain.services.summary_service.summary_service import SummaryService
from src.unite_talking_points.utils.application.interfaces.console_utils import print_word_art, \
    print_document_query_results
from src.unite_talking_points.utils.configuration_utils.config_loader import ConfigLoader


def main():
    # Welcome message
    print_word_art()

    # Load the configuration
    print()
    print()
    print("Loading configuration...")
    config = ConfigLoader().load_config()

    if config:
        end_of_program = False
        try:
            top_n = int(config["Application-console"]["top_n"])
            openai_api_key = str(config["External-services"]["openai_api_key"])
        except TypeError:
            print("TypeError occurred while loading configuration")
        else:
            print("Configuration loaded successfully")

            while not end_of_program:
                print()
                print()
                print("1. Load repository")
                print("2. Set up repository")
                print("3. Exit")
                choice1 = str(input("Enter your choice: "))

                # For both options we will need the repository
                if choice1 == "1" or choice1 == "2":

                    repository = FileDocumentRepository(config['Directories']['documents_path'])

                    if choice1 == "1":
                        print()
                        print()
                        print("Loading repository...")

                        repository.load()
                        print(f"{len(repository)} documents and vectors were loaded")

                    elif choice1 == "2":
                        print()
                        print()
                        print("Setting up repository...")

                        repository.setup()
                        repository.save()
                        print(f"Repository with {len(repository)} documents and vectors was created")

                    if repository:
                        while not end_of_program:
                            print()
                            print()
                            print("1. Query documents")
                            print("2. Summarize documents")
                            print("3. Generate talking points")
                            print("4. Exit")
                            choice2 = str(input("Enter your choice: "))

                            if choice2 == "1":
                                print()
                                print()
                                query = str(input("Enter your query: "))

                                # Perform the query
                                print()
                                print()
                                print("Querying documents...")
                                query_service = QueryService(query, repository)
                                query_indexes = query_service.run()

                                # Print top n relevant documents
                                query_results = repository[query_indexes[:top_n]]
                                query_indexes = query_indexes[:top_n]
                                print_document_query_results(query_results, query_indexes)

                            elif choice2 == "2":
                                # Search the document to be summarized
                                print()
                                print()
                                query_id = str(input(
                                    "Enter the id of the document you want to summarize (type exit to quit): "
                                ))
                                if query_id == "exit":
                                    end_of_program = True
                                else:
                                    try:
                                        query_id = int(query_id)
                                        document = repository.documents[query_id]

                                    except ValueError:
                                        print("Invalid query as an index. Please enter a valid choice.")

                                    except IndexError:
                                        print("Document not found with that index. Please enter a valid choice.")

                                    else:
                                        print()
                                        print()
                                        print(f"Document with id {query_id} found")
                                        print("Summarizing document...")

                                        # Summarize the document
                                        summary_service = SummaryService(document, openai_api_key)
                                        summary_result = summary_service.run()

                                        print()
                                        print()
                                        print("SUMMARY RESULT:")
                                        print(summary_result)

                            elif choice2 == "3":
                                # Search the documents to be summarized
                                print()
                                print()
                                query_ids = str(input(
                                    "Enter the documents id's you want to use separated by commas (type exit to quit): "
                                ))
                                if query_ids == "exit":
                                    end_of_program = True
                                else:
                                    try:
                                        query_ids = [int(query_id) for query_id in query_ids.split(",")]
                                        documents = [repository.documents[query_id] for query_id in query_ids]

                                    except ValueError:
                                        print("Invalid query as an index. Please enter a valid choice.")

                                    except IndexError:
                                        print("Document not found with that index. Please enter a valid choice.")

                                    else:
                                        print()
                                        print()
                                        print("All the documents were found")
                                        print("Summarizing documents...")

                                        # Summarize the documents
                                        summaries = []
                                        for document in documents:
                                            summary_service = SummaryService(document, openai_api_key)
                                            summary_result = summary_service.run()
                                            summaries.append(summary_result)

                                        print()
                                        print()
                                        print("SUMMARY RESULTS:")
                                        for summary, query_id in zip(summaries, query_ids):
                                            print()
                                            print(f"DOCUMENT {query_id}")
                                            print(summary)

                                        # Generate the talking point
                                        print()
                                        print()
                                        print("Please introduce the parameters to create the talking point")
                                        user_prompt = str(input(
                                            "Explain what do you want to talk about: "
                                        ))
                                        temperature = 0
                                        # Removed for user simplicity
                                        # while not isinstance(temperature, float):
                                        #     temperature = str(input(
                                        #         "Temperature [0,1] (flexibility of the model) suggested 0.2): "
                                        #     ))
                                        #     try:
                                        #         temperature = float(temperature)
                                        #         if temperature < 0.0 or temperature > 1.0:
                                        #             print("Temperature must be between 0 and 1")
                                        #             temperature = None
                                        #     except ValueError:
                                        #         print("Temperature must be a number between 0 and 1")

                                        length = str(input(
                                            "Length of the talking point: "
                                        ))
                                        tone = str(input(
                                            "Tone of the talking point: "
                                        ))

                                        generation_parameters = {
                                            'temperature': temperature,
                                            'user_prompt': user_prompt,
                                            'length': length,
                                            'tone': tone
                                        }

                                        generation_service = GenerationService(
                                            summaries, generation_parameters, openai_api_key
                                        )
                                        generation_result = generation_service.run()
                                        print("GENERATED TALKING POINT:")
                                        print(generation_result)

                            elif choice2 == "4":
                                end_of_program = True

                            else:
                                print("Invalid choice. Please enter a valid choice.")

                    else:
                        print("Repository is empty or cannot be loaded")

                elif choice1 == "3":
                    end_of_program = True

                else:
                    print("Invalid choice. Please enter a valid choice.")

    else:
        print("Configuration cannot be loaded")

    print("Goodbye! :)")


if __name__ == '__main__':
    main()
