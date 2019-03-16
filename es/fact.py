import os
from typing import List

from . import FactModel, FactRow


class Fact(object):
    facts: List[FactModel] = list()
    names: List[str] = list()
    facts_path = os.path.join(os.getcwd(), 'facts.txt')

    def __init__(self):
        with open(self.facts_path, 'r') as f:
            self.names = f.readline()[:-1].split(',')
            file_lines = f.readlines()
            for line in file_lines:
                if line.endswith('\n'):
                    line = line[:-1]
                values: List = line.split(',')
                for i in range(len(values)):
                    if values[i] == 'да':
                        values[i] = True
                    elif values[i] == 'нет':
                        values[i] = False
                self.facts.append(FactModel(*values))

    def save_fact(self, fact: FactModel):
        if fact not in self.facts:
            self.facts.append(fact)
            with open(self.facts_path, 'w') as f:
                f.write(','.join(self.names) + '\n')
                f.write('\n'.join([str(fact_model) for fact_model in self.facts]))

    def add_fact(self):
        new_fact = FactModel().__dict__
        for k, v in new_fact.items():
            inp = input(v.question).lower()
            if inp == 'да':
                inp = True
            elif inp == 'нет':
                inp = False
            new_fact[k] = inp
        fact_model = FactModel(**new_fact)
        print(f'Добавлен факт:\n {repr(fact_model)}')
        self.save_fact(fact_model)

    @staticmethod
    def ask(row: FactRow):
        question = row.question
        response = input(question).lower()
        if response == 'да':
            response = True
        elif response == 'нет':
            response = False
        return response

    def do_request(self, responses: List[FactModel], skipped: List):
        if len(responses) == 0:
            return []
        else:
            first: FactModel = responses[0]
            ask_row = None
            for k, v in first.__dict__.items():
                for i in responses[1:]:
                    if k not in skipped and getattr(first, k) != getattr(i, k):
                        ask_row = k
                        break
                if ask_row is not None:
                    break
            if ask_row is None:
                return responses
            response_row = self.ask(getattr(first, ask_row))
            if response_row != '':
                responses = [response for response in responses if getattr(response, ask_row).value == response_row]
            else:
                skipped.append(ask_row)
            return self.do_request(responses, skipped)

    def request(self):
        responses = self.do_request(self.facts, ['name'])
        if len(responses) == 0:
            print('К сожалению ничего не найдено.')
        else:
            print(f'Количество результатов: {len(responses)}.')
            for response in responses:
                print(response.name.value.capitalize())

    def show_all(self):
        for i in self.facts:
            print(repr(i))



