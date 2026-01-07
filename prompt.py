import random

class Prompt:
    def __init__(self, text):
        self.text = text
        self.randomize = True
        self.weighted = True

    def get_tokens(self, prompt):
        tokens_raw = prompt.split(",")
        tokens_cleaned = []
        for token in tokens_raw:
            token = token.strip()
            token = token.split(":")
            token = token[0].replace("(", "").replace(")", "")
            if len(token) > 0:
                tokens_cleaned.append(token)

        if self.randomize:
            random.shuffle(tokens_cleaned)
        return tokens_cleaned

    # def clean_prompt(self, prompt):
    #     result_prompt = ""
    #     tokens_cleaned = self.get_tokens(prompt)
    #     for token in tokens_cleaned:
    #         result_prompt += token
    #         if token != tokens_cleaned[-1]:
    #             result_prompt += ", "
    #     return result_prompt

    def weighted_prompt(self):
        result_prompt = ""
        tokens_cleaned = self.get_tokens(self.text)
        for token in tokens_cleaned:
            if self.weighted:
                result_prompt += '(' + token + ':' + str(round(random.uniform(0.1, 1.5), 1)) + ')'
            else:
                result_prompt += token
            if token != tokens_cleaned[-1]:
                result_prompt += ", "
        return result_prompt

    def create_prompt(self):
        return self.weighted_prompt()
        # if self.weighted:
        #     return self.weighted_prompt(self.text)
        # return self.clean_prompt(self.text)