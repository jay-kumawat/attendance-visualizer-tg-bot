import json

def json_decode(j_data):
    j_data = json.loads(j_data)

    static_data = {
        "course": j_data['attendanceDetails'][0]['_id'],
        "batch": j_data['attendanceDetails'][0]['batches'][0]['_id'],
        "division": j_data['attendanceDetails'][0]['batches'][0]['divisions'][0]['_id'],
        "semester": j_data['attendanceDetails'][0]['batches'][0]['divisions'][0]['semesters'][0]['_id']
    }

    small_dict = {}
    for i in j_data['attendanceDetails'][0]['batches'][0]['divisions'][0]['semesters'][0]['subjects']:
        small_dict[i['subject']['name']] = {"semesterSubject": i['_id'], "subject": i['subject']['_id']}

    payload = {}
    for key, value in small_dict.items():
        payload[key] = {**static_data, **value}

    return payload
