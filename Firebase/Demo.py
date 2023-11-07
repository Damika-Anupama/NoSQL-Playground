# Import the required modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Initialize the app with a service account
cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

# Get a reference to the database
db = firestore.client()


def write_single_document(collection, document, data):
    doc_data = {
        'name': data['name'],
        'age': data['age'],
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now(),
        'is_active': True
    }
    db.collection(collection).document(document).set(doc_data)
    print('Document written successfully.')


def write_nested_data(collection, document, data):
    doc_data = {
        'name': data['name'],
        'age': data['age'],
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now(),
        'is_active': True,
        'address': {
            'street': '123 Main St.',
            'city': 'Anytown',
            'state': 'CA',
            'zip': 12345
        }
    }
    db.collection(collection).document(document).set(doc_data)
    print('Document written successfully.')

def write_multiple_documents(collection, documents, data):
    batch = db.batch()
    for document in documents:
        doc_data = {
            'name': data[document]['name'],
            'age': data[document]['age'],
            'created_at': datetime.datetime.now(),
            'updated_at': datetime.datetime.now(),
            'is_active': True
        }
        batch.set(db.collection(collection).document(document), doc_data)
    batch.commit()

    print('Documents written successfully.')

write_nested_data('users', 'user_1', {'name': 'John Doe', 'age': 20})

# write_single_document('users', 'user_2', {'name': 'Michael Rose', 'age': 25})
# write_multiple_documents('users', ['user_3', 'user_4'], {'user_3': {
#                          'name': 'Mary Jane', 'age': 35}, 'user_4': {'name': 'Rosa Salazar', 'age': 40}})

