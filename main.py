from flask import Flask, jsonify, request, make_response
import json
app = Flask(__name__)
data = [
    {
        "id": "3b58aade-8415-49dd-88db-8d7bce14932a",
        "first_name": "Tanya",
        "last_name": "Slad",
        "graduation_year": 1996,
        "address": "043 Heath Hill",
        "city": "Dayton",
        "zip": "45426",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff",
    },
    {
        "id": "d64efd92-ca8e-40da-b234-47e6403eb167",
        "first_name": "Ferdy",
        "last_name": "Garrow",
        "graduation_year": 1970,
        "address": "10 Wayridge Terrace",
        "city": "North Little Rock",
        "zip": "72199",
        "country": "United States",
        "avatar": "http://dummyimage.com/148x100.png/dddddd/000000",
    },
    {
        "id": "66c09925-589a-43b6-9a5d-d1601cf53287",
        "first_name": "Lilla",
        "last_name": "Aupol",
        "graduation_year": 1985,
        "address": "637 Carey Pass",
        "city": "Gainesville",
        "zip": "32627",
        "country": "United States",
        "avatar": "http://dummyimage.com/174x100.png/ff4444/ffffff",
    },
    {
        "id": "0dd63e57-0b5f-44bc-94ae-5c1b4947cb49",
        "first_name": "Abdel",
        "last_name": "Duke",
        "graduation_year": 1995,
        "address": "2 Lake View Point",
        "city": "Shreveport",
        "zip": "71105",
        "country": "United States",
        "avatar": "http://dummyimage.com/145x100.png/dddddd/000000",
    },
    {
        "id": "a3d8adba-4c20-495f-b4c4-f7de8b9cfb15",
        "first_name": "Corby",
        "last_name": "Tettley",
        "graduation_year": 1984,
        "address": "90329 Amoth Drive",
        "city": "Boulder",
        "zip": "80305",
        "country": "United States",
        "avatar": "http://dummyimage.com/198x100.png/cc0000/ffffff",
    }
]

@app.route('/')
def hello_user():
    return jsonify(message="hello")

@app.route('/no_content')
def handle_no_content():
    return ({"content":"No Content Found"}, 204)

@app.route('/exp')
def index_explicit():
    res = make_response({"message": "hello"})
    res.status_code = 200
    return res

@app.route('/data/name_search')
def get_data():
    query_data = request.args.get('q')

    if not query_data:
        return ({"message": "query parameter is missing"}, 400)
    
    if query_data.strip() == "" or query_data.isdigit():
        return ({"message": "Invalid or missing input parameter"}, 422)
    
    for person in data:
        if query_data.lower() == person["first_name"].lower():
            return person, 200

    return ({"Message": "Person Not Found"}, 404)
    
@app.get('/data/count')
def get_count():
    try:
        return ({"data length":len(data)}, 200)
    except NameError:
        return ({"message": "data not found"},500)
    
@app.get("/data/person/<uuid:id>")
def find_by_uuid(id):
    for person in data:
        if person['id'] == str(id):
            return(person, 200)
        
    return {"mesage": "person no found"}, 404

@app.delete('/data/person/<uuid:id>')
def delete_person_by_uuid(id):
    for person in data:
        if person['id'] == str(id):
            data.remove(person)
            return ({"message":f"Person wit ID {id} Deleted"}, 200)
        
    return ({"message": "person not found"},404)


@app.post('/data/person')
def post_new_person():
    person = request.json
    if not person:
        return ({"message": "Invalid Input Parameter"}, 422)
    try:
        data.append(person)
    except NameError:
        return ({"message": "Data Not found"}, 500)
    
    return ({"message": f"added new person, id{person['id']} to data"}, 201)

@app.errorhandler(404)
def api_not_found(error):
    return {"message": "API not found"}, 404

@app.errorhandler(Exception)
def handle_exception(e):
    return ({"message":f"an exception has occurred: {e}"})

@app.route('/test500')
def test500():
    raise Exception("Forced exception thrown for testing")