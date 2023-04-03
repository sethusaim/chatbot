import openai
import yaml


def read_config():
    try:
        with open(file="bot_config.yaml", mode="r") as f:
            dic = yaml.safe_load(f)

        return dic

    except Exception as e:
        raise e


def generate_answer(question):
    try:
        config = read_config()["question_answer"]

        response = openai.Completion.create(prompt=f"Q: {question}\nA:", **config)

        answer = response.choices[0].text.strip()

        return answer

    except Exception as e:
        raise e
