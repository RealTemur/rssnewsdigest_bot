import openai

class OpenAIClient:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_digest(self, articles, language='ru'):
        prompt = self.create_prompt(articles, language)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']

    def create_prompt(self, articles, language):
        # Create a digest prompt based on the articles provided
        articles_text = '\n'.join(articles)
        prompt = f"Создайте новостной дайджест на русском по следующим статьям:\n{articles_text}"
        return prompt

# Пример использования:
# client = OpenAIClient(api_key='your-api-key')
# articles = ["Article 1 content...", "Article 2 content..."]
# digest = client.generate_digest(articles)  
# print(digest)