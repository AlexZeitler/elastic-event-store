import json


class FetchChangesets:
    def __init__(self, db):
        self.db = db

    def execute(self, event, context):
        query_string = event.get("queryStringParameters") or {}
        stream_id = query_string.get("stream_id")
        
        changesets = self.db.fetch_stream_changesets(stream_id)

        changesets = [{ "changeset_id": c.changeset_id,
                        "events": c.events,
                        "metadata": c.metadata } for c in changesets]
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "stream_id": stream_id,
                "changesets": changesets
            }),
        }