import replicate
import wikipedia
import json
from creds import API_KEY

replicate=replicate.Client(api_token=API_KEY)

def generate(num_questions,text,filename):
    
    input = {
    "prompt": f"Create {num_questions} multiple-choice questions (MCQs) from the following text corpus. Each question should have 4 options with one correct answer. Please return the result strictly as a JSON array with the format: question, options, and the correct answer.\n\nText Corpus:\n{text}",
    "temperature": 0.2,
    "max_tokens": 1000,

    }
    responses=list()
    for event in replicate.stream("meta/meta-llama-3-70b-instruct",input=input):
        responses.append(str(event))    
    with open(f"{filename}.json",'w') as file:
        json.dump(''.join(responses).strip(' '),file)    
    return True


def get_data(page):
    article=wikipedia.page(page)
    return article.summary

#print(generate(num_questions=10,text=get_data('Initial_public_offering'),filename='ipo'))
print(generate(num_questions=10,text=get_data('Stock_market'),filename='stock_market'))
print(generate(num_questions=10,text=get_data('Saving'),filename='saving'))


