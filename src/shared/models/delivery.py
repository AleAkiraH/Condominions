from datetime import datetime
import uuid

class Delivery:
    def __init__(self):
        self.pk = ""  # DELIVERY#{apartment_number}
        self.sk = ""  # DELIVERY#{timestamp}
        self.delivery_id = str(uuid.uuid4())
        self.resident_name = ""
        self.apartment_number = ""
        self.description = ""
        self.pickup_code = str(uuid.uuid4())[:6].upper()
        self.status = "PENDING"  # PENDING, DELIVERED
        self.created_at = datetime.now().isoformat()
        self.delivered_at = None
        self.created_by = ""  # ID do porteiro
        self.delivered_to = ""  # ID do morador que retirou
