# Import the required modules
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime

# Initialize the app with a service account
cred = credentials.Certificate('./serviceAccountKey.json')
default_app = firebase_admin.initialize_app(cred)

# Get a reference to the Firestore database
db = firestore.client()

# Create collection references for students, classes, and instructors
students_ref = db.collection("students")
classes_ref = db.collection("classes")
instructors_ref = db.collection("instructors")

# Create documents for students, classes, and instructors
def create_student(sid, fname, lname, dob, status, grade, classes=[]):
    student_data = {
        "sid": sid,
        "fname": fname,
        "lname": lname,
        "dob": dob,
        "status": status,
        "grade": grade,
        "classes": classes  # Array of references to class documents
    }
    students_ref.document(str(sid)).set(student_data)

def create_class(cid, cname, credits, grade, students=[], instructors=[]):
    class_data = {
        "cid": cid,
        "cname": cname,
        "credits": credits,
        "grade": grade,
        "students": students,  # Array of references to student documents
        "instructors": instructors  # Array of references to instructor documents
    }
    classes_ref.document(str(cid)).set(class_data)

def create_instructor(tid, name, dept, grade, classes=[]):
    instructor_data = {
        "tid": tid,
        "name": name,
        "dept": dept,
        "grade": grade,
        "classes": classes  # Array of references to class documents
    }
    instructors_ref.document(str(tid)).set(instructor_data)

# Create relationships between students, classes, and instructors
def add_student_to_class(student_id, class_id):
    student_doc_ref = students_ref.document(student_id)
    class_doc_ref = classes_ref.document(class_id)

    student_doc_ref.update({
        "classes": firestore.ArrayUnion([class_doc_ref])
    })

    class_doc_ref.update({
        "students": firestore.ArrayUnion([student_doc_ref])
    })

def add_instructor_to_class(instructor_id, class_id):
    instructor_doc_ref = instructors_ref.document(instructor_id)
    class_doc_ref = classes_ref.document(class_id)

    instructor_doc_ref.update({
        "classes": firestore.ArrayUnion([class_doc_ref])
    })

    class_doc_ref.update({
        "instructors": firestore.ArrayUnion([instructor_doc_ref])
    })

# Perform CRUD operations with relationships
create_student(1, "John", "Doe", datetime.datetime(1990, 1, 1), "Active", 3.5)
create_student(2, "Jane", "Smith", datetime.datetime(1991, 2, 15), "Active", 4.0)
create_class(101, "Math", 3, 4.0)
create_instructor(201, "Professor Smith", "Math Department", 4.5)

add_student_to_class("1", "101")
add_student_to_class("2", "101")
add_instructor_to_class("201", "101")
