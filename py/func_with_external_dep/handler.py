import inflection
import os

def handler(context, event):
    if os.getenv('TEST') != 'SUCCESS':
        raise Exception('Missing env variable TEST')
    return inflection.camelize(event.body.decode('utf-8').strip())
