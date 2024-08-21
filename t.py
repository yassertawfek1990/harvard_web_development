import requests
import random
import html
def get_questions():
    parameters = {
        "amount" : 10,
        "category":9, #general knowledge
        "difficulty":"hard",
        "type": "multiple"
    }
    response = requests.get("https://opentdb.com/api.php",params= parameters)
    response.raise_for_status()
    question_data = response.json()["results"]
    return question_data


# parameters = {
#         "amount" : 10,
#         "category":9, #general knowledge
#         "difficulty":"hard",
#         "type": "multiple"
#     }
# response = requests.get("https://opentdb.com/api.php",params= parameters)
# response.raise_for_status()
# print(response.json())
# question_data = response.json()["results"]
# print(question_data)
all = get_questions()
# print(all)
for i in range(10):
    print(i)
    # data = html.unescape(all[i])
    data = all[i]
    q = html.unescape(data["question"])
    answer = html.unescape(data["correct_answer"])
    wrong = html.unescape(data["incorrect_answers"])
    wrong.append(answer)
    random.shuffle(wrong)
    # print(data)
    # print(data,q,answer,wrong)
    print(q)
    print(answer)
    print(wrong)

# for i in range(10):
#     print(i)
#     data = html.unescape(all[i])
#     # data = all[i]
#     q = data["question"]
#     answer = data["correct_answer"]
#     wrong = data["incorrect_answers"]
#     wrong.append(answer)
#     random.shuffle(wrong)
#     # print(data)
#     # print(data,q,answer,wrong)
#     print(q)
#     print(answer)
#     print(wrong)