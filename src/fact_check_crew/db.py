from langchain_community.vectorstores import LanceDB


def lanceDBConnection(dataset):
    db = LanceDB.connect("/tmp/lancedb")
    table = db.create_table("tb", data=dataset, mode="overwrite")
    return table
