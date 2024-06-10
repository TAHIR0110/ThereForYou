import csv

import spacy

nlp = spacy.load("en_core_web_sm")

memory = []


def load_dataset(file_path):
    dataset = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if len(row) >= 2:
                dataset.append((row[0], row[1]))
    return dataset


def find_closest_prompt(user_input, dataset):
    input_doc = nlp(user_input)
    closest_prompt = None
    min_similarity = 0

    for prompt, _ in dataset:
        prompt_doc = nlp(prompt)
        similarity = input_doc.similarity(prompt_doc)
        if similarity > min_similarity:
            min_similarity = similarity
            closest_prompt = prompt

    return closest_prompt


def get_response(user_input, dataset):
    closest_prompt = find_closest_prompt(user_input, dataset)

    if closest_prompt is None:
        return "I'm sorry, I don't understand. Can you please rephrase or provide more information?"

    for prompt, response in dataset:
        if prompt == closest_prompt:
            return response


def ai_chatbot(user_input, dataset):
    global memory
    if "hello" in user_input.lower():
        response = (
            "Hello! How are you feeling today? Please tell me more about your feelings."
        )
    else:
        response = get_response(user_input, dataset)
    memory.append((user_input, response))
    return response
