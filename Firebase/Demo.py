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


def read_single_document(collection, document):
    doc_ref = db.collection(collection).document(document)
    doc = doc_ref.get()
    if doc.exists:
        print('Document data: {}'.format(doc.to_dict()))
    else:
        print('No such document!')

def read_multiple_documents(collection):
    # 1. just get all the documents in the collection
    # docs = db.collection(collection).stream()

    # 2. get all the documents in the collection, order them by age and limit the results to 2
    # docs = db.collection(collection).where('age', '>=', 20).order_by('age').limit(2).stream()

    # 3. get all the documents in the collection, check array contains a value
    docs = db.collection(collection).where('indices', 'array_contains', 'NDX').stream()

    for doc in docs:
        print('{} => {}\n'.format(doc.id, doc.to_dict()))

def update_single_document(collection, document, data):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update(data)
    print('Document updated successfully.')

def delete_field(collection, document, field):
    doc_ref = db.collection(collection).document(document)
    doc_ref.update({
        field: firestore.DELETE_FIELD
    })
    print('Field deleted successfully.')

def delete_document(collection, document):
    db.collection(collection).document(document).delete()
    print('Document deleted successfully.')


# write_nested_data('users', 'user_1', {'name': 'John Doe', 'age': 20})

# write_single_document('users', 'user_2', {'name': 'Michael Rose', 'age': 25})

# write_multiple_documents('users', ['user_3', 'user_4'], {'user_3': {
#                          'name': 'Mary Jane', 'age': 35}, 'user_4': {'name': 'Rosa Salazar', 'age': 40}})

# read_single_document('users', 'user_1')

# read_multiple_documents('NYSE')

# update_single_document('users', 'user_1', {'name': 'Tom Crook', 'age': firestore.Increment(5)})

# delete_field('users', 'user_4', 'age')

delete_document('users', 'user_4')

