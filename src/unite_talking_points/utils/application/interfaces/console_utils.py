import os


def print_word_art():
    word_art = """
     ____ ___      .__  __           ___________      .__   __   .__                 __________      .__        __          
    |    |   \____ |__|/  |_  ____   \__    ___/____  |  | |  | _|__| ____    ____   \______   \____ |__| _____/  |_  ______
    |    |   /    \|  \   __\/ __ \    |    |  \__  \ |  | |  |/ /  |/    \  / ___\   |     ___/  _ \|  |/    \   __\/  ___/
    |    |  /   |  \  ||  | \  ___/    |    |   / __ \|  |_|    <|  |   |  \/ /_/  >  |    |  (  <_> )  |   |  \  |  \___ \ 
    |______/|___|  /__||__|  \___  >   |____|  (____  /____/__|_ \__|___|  /\___  /   |____|   \____/|__|___|  /__| /____  >
                 \/              \/                 \/          \/       \//_____/                           \/          \/ 
    """

    print(word_art)


def print_document_query_results(query_results, query_indexes):
    print('Query results:')
    for i, document in zip(query_indexes, query_results):
        print()
        print(f"DOCUMENT ID: {i}")
        print(f"FILE NAME: {os.path.split(document.source)[1]}")
        print(f"AUTHOR: {document.author}")
        print(f"CREATION DATE: {document.date_created}\t"
              f"MODIFICATION DATE: {document.date_modified}")
        print("TEXT SAMPLE:")
        # print first 500 characters
        if len(document) >= 500:
            print(document.content[:500])
        else:
            print(document.content)

        print("-" * 100)
