import inflection

def handler(context, event):
    return inflection.camelize(event.body.decode('utf-8').strip())
