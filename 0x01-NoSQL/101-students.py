#!/usr/bin/python3
""" A script that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """ A function that returns all students sorted by average score
		in desc order
    """

    pipeline = mongo_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "averageScore": {"$avg": "$score"}
        }
    },
    {
        '$sort': {'averageScore': -1}
    }
])
    return pipeline 
