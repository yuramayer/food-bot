"""OpenAI API functions that are used by bot"""

from openai import OpenAI
from config.conf import OPENAI_TOKEN

client = OpenAI(api_key=OPENAI_TOKEN)


def estimate_nutrition(food_description: str) -> tuple:
    """
    Оценивает калорийность и содержание полезностей в еде
    """
    system_prompt = (
        "Ты диетолог. На основе описания блюда \
            оцени его пищевую ценность. "
        "Ответь в формате ТОЛЬКО python словарь: \
            'грамм' (г), 'калории' (ккал), \
                'белки' (г), 'жиры' (г), 'углеводы' (г). "
        "Результат должен быть в виде словаря.\
            Возвращай именно код, без форматирования"
    )

    user_prompt = f"Описание блюда: {food_description}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )

        reply = response.choices[0].message.content

        return reply, None

    except Exception as err:

        return None, f'Ошибка на этапе генерации: {err}'
