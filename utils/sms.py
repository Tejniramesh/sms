from datetime import datetime
from utils.db import messages_collection

def send_sms(user, phone, message):

    messages_collection.insert_one({
        "user": user,
        "phone": phone,
        "message": message,
        "status": "Sent",
        "created_at": datetime.now()
    })

    return True
