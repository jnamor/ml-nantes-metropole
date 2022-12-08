import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Use a service account.
cred = credentials.Certificate('nancydb-c955d-firebase-adminsdk-kjz2s-43f86797f0.json')

app = firebase_admin.initialize_app(cred, {
   'databaseURL': 'https://nancydb-c955d-default-rtdb.europe-west1.firebasedatabase.app/'
})

ref = db.reference('restricted_access/secret_document')

users_ref = ref.child('testJean')
users_ref.set({
    'JeanIsAwesome': {
        'date_of_birth': 'April 14, 1979',
        'full_name': 'Jean Charbonneau'
    },
    'YouAreAwesome': {
        'date_of_birth': 'unknown',
        'full_name': 'Putyour Namehere'
    }
})