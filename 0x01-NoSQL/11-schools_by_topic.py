#!/usr/bin/env python3
""" A script that returns list of schools with specifi topic
"""


def schools_by_topic(mongo_collection, topic):
    """ a function that returns the list of school having a
        specific topic
    """

    result = mongo_collection.find({"topics": topic})
    return result
