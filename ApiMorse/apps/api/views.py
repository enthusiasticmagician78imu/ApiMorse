from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

import pymongo
import dns

# Replace the uri string with your MongoDB deployment's connection string.
conn_str = "mongodb+srv://urgosxd:4421210samu@cluster0.zf2s5.mongodb.net/?retryWrites=true&w=majority"
# set a 5-second connection timeout
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

# try:

#     result = client.get_database("Cluster0")["tasks"].aggregate(
#         [
#             {
#                 "$search": {
#                     "compound": {
#                         "must": [
#                             {
#                                 "phrase": {
#                                     "path": "content",
#                                     "query": "Bases de datos",
#                                 }
#                             },
#                             {"text": {"path": "typeCurse", "query": "ddbb"}},
#                         ]
#                     }
#                 }
#             },
#             {"$project": {"title": 1, "typeCurse": 1, "content": 1, "_id": 0}},
#         ]
#     )
#     for idx, i in enumerate(result):
#         print(idx)

# except Exception:
#     print("Unable to connect to the server.")


@api_view(["GET"])
def user_api_view(request, data):
    if request.method == "GET":
        data = data.split("-")
        try:
            result = client.get_database("Cluster0")["tasks"].aggregate(
                [
                    {
                        "$search": {
                            "compound": {
                                "must": [
                                    {
                                        "phrase": {
                                            "path": "content",
                                            "query": " ".join(data[1].split("_")),
                                        }
                                    },
                                    {"text": {"path": "typeCurse", "query": data[0]}},
                                ]
                            }
                        }
                    },
                    {"$project": {"content": 1, "_id": 0}},
                ]
            )
            return Response(result)
        except Exception:
            return Response("ERROR")
