import chromadb
import time
import pandas as pd
from src.read_data import main as read_product_data
from src.create_database import get_chroma_collection

def embedd_data(df: pd.DataFrame, collection: chromadb.Collection):
    # Convert the DataFrame index to a list of string IDs
    ids = list(df.index.astype(str))
    # Loop through the DataFrame in batches of 10
    batch_size = 10
    for i in range(0, len(df), batch_size):
        # Get the current batch of data
        df_batch = df.iloc[i:i+batch_size]
        # Create lists for ids and documents for this batch
        batch_ids = ids[i:i+batch_size]
        batch_documents = [
            f"Title: {row['title']} \nDescription: {row['description']} \nCategories: {row['level1']}, {row['level2']}, {row['level3']}"
            for _, row in df_batch[['title', 'description', 'level1', 'level2', 'level3']].iterrows()
        ]
        # Add the current batch to the collection
        collection.add(ids=batch_ids, documents=batch_documents)
        # Wait for 10 second after each batch 
        time.sleep(10)
    print('Products successfully embedded')
    
    
def main():
    df_sample = read_product_data()
    collection = get_chroma_collection()
    embedd_data(df=df_sample, collection=collection)
    
if __name__ == '__main__':
    main()
    

    