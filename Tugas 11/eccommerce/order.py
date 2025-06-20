import uuid
from datetime import datetime
import random

def generate_order_id():

    tanggal = datetime.now().strftime("%Y%m%d")
    random_number = random.randint(1000, 9999)
    return f"ORDER-{tanggal}-{random_number}"