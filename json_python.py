import json

json_data = """{
  "name": "vasda",
  "age": 301,
  "is_student": false,
  "courses": ["python", "qa auto", "api test"],
  "addres": {
    "city": "moscow",
    "zip": "300020"
  }
}"""
parsed_data = json.loads(json_data)  # Преобразуем JSON-строку в Python-объект (dict)

print(parsed_data['courses'], type(parsed_data))  # Выведет: Иван

data = {
    "name": "Akka",
    "age": 21,
    "is_student": True,

}
json_string = json.dumps(data, indent=4)
print(json_string, type(json_string))

with open("json_example.json", "r", encoding="utf-8") as file:
    data = json.load(file)
print(data)
with open("json_user.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)