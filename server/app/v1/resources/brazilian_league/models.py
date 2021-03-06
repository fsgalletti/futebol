import json
from app import mongo
from flask_restplus import abort
from bson.json_util import dumps
from bson.objectid import ObjectId
from app.helpers import encrypt_password
from datetime import datetime

class BrazilianLeague:

    @staticmethod
    def last_12_games():
        query = mongo.db.brazilian_league.find({"score_team_1": {"$ne": "-"}},
                             {'_id': 0, 'stadium':1, 'team_1':1,
                              'team_2':1, 'score_team_1':1, 'score_team_2':1,
                              'date': 1}
                             ).sort('date', -1).limit(12)

        final_object = []
        for result in query:
            result['date'] = datetime.strftime(result['date'], '%d/%m/%Y')
            final_object.append(result)

        return json.loads(
            dumps(
                final_object
            )
        )

    @staticmethod
    def brazilian_league_graph():
        query = mongo.db.rank_brazilian_league.aggregate([
            {'$project':
                 { '_id':0,'name': 1, 'points':'$2019.points'}
             }
        ])

        return json.loads(
            dumps(
                query
            )
        )

    @staticmethod
    def next_5_games():
        query = mongo.db.brazilian_league.find({"score_team_1": "-"}, {"_id": 0, "team_1": 1}).sort("date", 1).limit(5)

        return json.loads(
            dumps(
                query
            )
        )



