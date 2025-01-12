from openai import OpenAI


class ChatBot:
    def __init__(self, model='gpt-3.5-turbo'):
        self.client = OpenAI(api_key='')
        self.messages = []
        self.model = model

    def add_message(self, role, content):
        if role in ["user", "assistant"]:
            self.messages.append(
                {"role": role, "content": content}
            )
        else:
            raise ValueError("Role must be 'user' or 'assistant'")

    def get_response(self, user_message):
        self.add_message("user", user_message)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        # print(response)
        model_message = response.choices[0].message.content
        self.add_message("assistant", model_message)
        return model_message


bot = ChatBot()

if __name__ == '__main__':
    print("Srating...")
    print(bot.get_response(
        "Kto jest prezzydentem Polski"))  # Od 6 sierpnia 2020 roku Prezydentem Polski jest Andrzej Duda.
    print(bot.get_response("Kiedy został wybrany"))  # Od 6 sierpnia 2020 roku Prezydentem Polski jest Andrzej Duda.
# Andrzej Duda został wybrany na urząd Prezydenta Polski po raz drugi w wyborach prezydenckich,
# które odbyły się 12 lipca 2020 roku. Jego inauguracyjna kadencja rozpoczęła się 6 sierpnia 2020 roku.
# ChatCompletion(id='chatcmpl-AooL74BzMVC9LimqranVkrq98EDXx', choices=[
#     Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(
#         content='Andrzej Duda został wybrany na urząd prezydenta Polski po raz pierwszy w wyborach prezydenckich,'
#                 ' które odbyły się 24 maja 2015 roku. Został wybrany na drugą kadencję w wyborach prezydenckich,'
#                 ' które odbyły się 12 lipca 2020 roku.',
#         refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1736673269,
#                model='gpt-3.5-turbo-0125', object='chat.completion', service_tier='default', system_fingerprint=None,
#                usage=CompletionUsage(completion_tokens=84, prompt_tokens=50, total_tokens=134,
#                                      completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0,
#                                                                                        audio_tokens=0,
#                                                                                        reasoning_tokens=0,
#                                                                                        rejected_prediction_tokens=0),
#                                      prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
