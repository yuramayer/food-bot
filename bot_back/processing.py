"""Funcs processing the messages for the bot"""

from ast import literal_eval


def process_food_estimation(food_est: str, food_name: str) -> tuple:
    """Processing the food estimation from the GPT"""

    try:
        food_dict = literal_eval(food_est)
        if not isinstance(food_dict, dict):
            return None, "Не получил словарь от ChatGPT API"
        elem_sets = {'белки', 'грамм', 'жиры', 'калории', 'углеводы'}
        if set(food_dict.keys()) != elem_sets:
            return None, "Словарь от ChatGPT неверного формата"

        if not all(isinstance(value, int) or isinstance(value, float)
                   for value in food_dict.values()):
            return None, "GPT вернула словарь с битыми значениями"

        food_dict['еда'] = food_name 

        return food_dict, None

    except (ValueError, SyntaxError):
        return None, 'Получил битую строку вместо словаря от ChatGPT API'

    except Exception as err:

        return None, f'Ошибка на этапе проверки словаря: {err}'


def dict2msg(d: dict) -> str:
    """Get the dictionary & return the string with elems"""

    res = '\n'.join(f' - {key}: {value}' for key, value in d.items())
    return res
