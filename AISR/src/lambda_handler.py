def handler(event, context):
    numbers = event.get("numbers", [])
    total = sum(numbers)
    return {"sum": total}