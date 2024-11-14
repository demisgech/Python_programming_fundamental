# Absoulte import which is the preferred one
from ecommerce.customer import contact 

# Relative import
from ..customer import contact
contact.contact_customer()

def shopping():
    print("Shopping")