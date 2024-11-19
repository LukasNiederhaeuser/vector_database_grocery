import os
import chromadb
from dotenv import find_dotenv, load_dotenv
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction

# Define folder for persistent storage
FOLDER_CHROMADB = os.path.join(os.getcwd(), 'chromadb')

# Load environment variables
load_dotenv(find_dotenv())
openai_api_key = os.getenv('OPENAI_API_KEY')

# Check if API key is loaded
if openai_api_key is None:
    raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

def create_chroma_db():    
    # Create ChromaDB client
    chromadb_client = chromadb.PersistentClient(path=FOLDER_CHROMADB)
    
    # Check if collection already exists; if not, create it
    if 'grocery_products' not in [col.name for col in chromadb_client.list_collections()]:
        chromadb_client.create_collection(
            name='grocery_products',
            embedding_function=OpenAIEmbeddingFunction(
                model_name="text-embedding-3-small",
                api_key=openai_api_key
            )
        )
        print("Collection 'grocery_products' created.")
    else:
        print("Collection 'grocery_products' already exists.")

def get_chroma_collection() -> chromadb.Collection:
    # Create ChromaDB client
    chromadb_client = chromadb.PersistentClient(path=FOLDER_CHROMADB)
    # Retrieve the existing collection by name
    collection = chromadb_client.get_collection(name='grocery_products')
    return collection
    
def main():
    # Only create the database/collection if it doesn't exist
    create_chroma_db()

if __name__ == '__main__':
    main()