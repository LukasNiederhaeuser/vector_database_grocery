from src.create_database import main as create_data_base_main
from src.data_embedding import main as data_embedding_main

def main():
    # Create the database and the collection
    create_data_base_main()
    # embed data
    data_embedding_main()

if __name__ == '__main__':
    main()