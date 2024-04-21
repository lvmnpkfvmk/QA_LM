import openai
import ijson


openai.api_key = ""

openai.base_url = "https://api.vsegpt.ru:6070/v1/"

file_path = 'RuBQ_2.0_test.json'

import ijson

# Open the JSON file
with open(file_path, 'r') as file:
    array_items = ijson.items(file, 'item')
    
    i = 0
    true_answers = 0
    answers = []
    for item in array_items:
        messages = []
        i += 1

        question = item["question_text"]
        answer = item["answer_text"].lower()

        prompt = "Отвечай наиболее коротко, 1-3 слова"
        # prompt = "Ответь максимально коротко и ёмко на вопрос. Ответ приводи в именительном падеже, при этом не забывай о пунктуации."
        # messages.append({"role": "user", "content": prompt})
        messages.append({"role": "user", "content": prompt + ' ' + question})
        response_big = openai.chat.completions.create(
            model="usev/saiga-mistral-7b",
            messages=messages,
            temperature=0.1,
        )
        response = response_big.choices[0].message.content.lower()
        answers.append(response + ' ' +  answer + '\n')
        if answer in response:
            true_answers += 1
        print(i, true_answers)
        # if i == 5:
        #     break

    with open('answers.txt', 'w') as kek:
        kek.writelines(answers)
    print(i, true_answers)
# #messages.append({"role": "system", "content": system_text})
#
# response_big = openai.chat.completions.create(
#     model="openai/gpt-3.5-turbo",
#     messages=messages,
# )
#
# # print("Response BIG:",response_big)
# response = response_big.choices[0].message.content
# print("Response:",response)
