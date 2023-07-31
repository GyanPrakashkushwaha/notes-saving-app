

# this will define how my note will look like

def noteEntity(item) -> dict:
    return {
        "_id": str(item["_id"]),
        "title": str(item['title']),
        "desc":str(item["item"]),
        "item":str(item["important"])
    }


def notesEntity(items) -> list:
    
    return [noteEntity(items) for item in items]



