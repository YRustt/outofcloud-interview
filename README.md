# outofcloud-interview

Тестовое задание для Out of Cloud.

Условие можно найти по [ссылке](https://docviewer.yandex.by/view/247501341/?*=eDYcQRng1wpgyn3ZX3Tucn9xp2V7InVybCI6InlhLW1haWw6Ly8xNjc0Nzc2MTExNDI4NTMyNjEvMS4yIiwidGl0bGUiOiLQotC10YHRgtC%2B0LLQvtC1INC30LDQtNCw0L3QuNC1INC90LAg0L%2FQvtC30LjRhtC40Y4gSnVuaW9yIFB5dGhvbiBEZXZlbG9wZXIucGRmIiwidWlkIjoiMjQ3NTAxMzQxIiwieXUiOiIyNDQzNzk4NTcxNTQzNTE1OTc0Iiwibm9pZnJhbWUiOmZhbHNlLCJ0cyI6MTU0MzU5NDE1NTM5NH0%3D).

### Граббер статей с новостных сайтов

Для запуска выполните следующую команду: `docker-compose -f docker-compose.prod.yml up -d scrapper`.

#### Console

```ipython
docker-compose -f docker-compose.prod.yml exec scrapper ipython
cd scrapper/

from scrapper.settings import GlobalConfig
from scrapper.config import make_config
from scrapper.utils import fetch_url

"""
В GlobalConfig хранится информация обо всех 
зарегестрированных сервисах новостей. 
(см. scrapper/config.json)
"""
global_config = GlobalConfig()
global_config.init()
```

##### Запрос для получения списка новостей:

```python
news_config = make_config(
    name="lenta",  # название сервиса
    request_type="news",  # тип запроса
    url="https://lenta.ru/rss",  # опционально
    limit=10,  # опционально
    path_to_items=("rss", "channel"),  # опционально
    item_tag="item",  # опционально
    item_fields={  # опционально
        "title": ("title",)
    }
)

# или (для зарегестрированных сервисов)
news_config = make_config(
    name="lenta",
    request_type="news",
    limit=10
)

await fetch_url(news_config)
```
Результатом является список словарей с информацией о новостях 
(заголовок, ссылка, описание и дата публикации):
```python
[{'title': '«Желтые жилеты» разгромили Триумфальную арку в Париже'},
 {'title': 'Мужчина захотел омолодиться с помощью суда'},
 {'title': 'Губернатор Подмосковья подвел итоги Года добровольца'},
 {'title': 'На Украине предложили новые санкции против россиян'},
 {'title': 'Ипотечные долги россиян признали беспрецедентными'},
 {'title': 'Вратарь сборной России вкатился с мячом в ворота'},
 {'title': 'Песков рассказал о таланте Путина «утаптывать» собеседников'},
 {'title': 'Из московского автомобиля украли 40 миллионов рублей'},
 {'title': 'Скорбящую пенсионерку вынудили ночевать в инвалидном кресле в аэропорту'},
 {'title': 'Россиянин получил 11 лет колонии за содействие ИГ'}]
```

##### Запрос на получение детального описания для новости:

```python
grub_config = make_config(
    name="lenta",  # название сервиса
    request_type="grub",  # тип запроса
    url="https://lenta.ru/news/2018/12/03/yellowvests/",  # опционально
    item_fields={  # опционально
        "title": {
            "name": "h1",
            "attrs": {
                "class": "b-topic__title"
            }
        }
    }
)

# или (для зарегестрированных сервисов)
grub_config = make_config(
    name="lenta",
    request_type="grub",
    url="https://lenta.ru/news/2018/12/03/yellowvests/"
)

await fetch_url(grub_config)
```
Результатом является словарь с детальным описанием новости.
```python
{'title': '«Желтые жилеты» разгромили Триумфальную арку в\xa0Париже',
 'image': ['https://icdn.lenta.ru/images/2018/12/03/14/20181203145410490/pic_eff5b32dff31a85de465c9f488f34b4c.jpg'],
 'content': ['Участники протестов «Желтые жилеты» ворвались в музейные помещения Триумфальной арки в Париже и испортили несколько экспонатов. Глава французского Центра национальных памятников сообщил о происшествии в Twitter.',
  'Протестующие повредили статую Наполеона, разбили картины, изрисовали несколько экспонатов. Ущерб, нанесенный музею, оценивается в миллион евро. После случившегося руководство решило закрыть Триумфальную арку для посетителей до окончания беспорядков в Париже.',
  'В сети появилось видео, как вандалы разрушают историческое наследие.',
  'Беспорядки во Франции продолжаются с середины октября. Недовольство жителей страны вызвала новость о повышении налога на бензин. Эта акция получила название по одежде протестующих, которые выходят на улицу в светоотражающих жилетах, как у водителей.']}
```

##### Описание config.json

```
{
    "lenta": {
        "news": {
            /* ссылка на rss */
            "url": "https://lenta.ru/rss", 
            /* путь из xml тэгов к записям о новостях */
            "path_to_items": ["rss", "channel"], 
            /* xml тэг для новости */
            "item_tag": "item",
            /* словарь, где ключами являются названия полей, 
             а значениями путь из xml тэгов для получения их значений*/ 
            "item_fields": { 
                "title": ["title"],
                "link": ["link"],
                "desc": ["description"],
                "published": ["pubDate"],
                "category": ["category"]
            }
        },
        "grub": {
            /* словарь, где ключами являются названия полей, 
             а значениями описания получения их значений,
             состоящих из названия (name), атрибутов (attrs) и 
             извлекаемых тэгов (tag)*/
            "item_fields": {
                "title": {
                    "name": "h1",
                    "attrs": {
                        "class": "b-topic__title"
                    }
                },
                "image": {
                    "name": "div",
                    "attrs": {
                        "class": "b-topic__title-image"
                    },
                    "tag": "img"
                },
                "content": {
                    "name": "div",
                    "attrs": {
                        "class": "b-text"
                    },
                    "tag": "p"
                }
            }
        }
    }
}
```

##### Регистрация нового сервиса

```python
global_config.register(
    name="interfax",
    config={
        "news": {
            "url": "https://www.interfax.ru/rss.asp",
            "path_to_items": ["rss", "channel"],
            "item_tag": "item",
            "item_fields": {
                "title": ["title"],
                "link": ["link"],
                "desc": ["description"],
                "published": ["pubDate"],
                "category": ["category"]
            }
        },
        "grub": {
            "item_fields": {
                "title": {
                    "name": "h1",
                    "attrs": {
                        "class": "textMTitle"
                    }
                },
                "content": {
                    "name": "article",
                    "attrs": {
                        "itemprop": "articleBody"
                    },
                    "tag": "p"
                }
            }
        }
    }
)
```

#### Rest API

 <table style="width:100% !important;">
    <thead>
        <tr>
            <th>endpoint</th>
            <th>type</th>
            <th>args</th>
        </tr>
    </thead>
    <tbody>
    <tr>
        <td>/news</td>
        <td>GET</td>
        <td>
            <table>
                <tbody>
                    <tr>
                        <td>name</td>
                        <td>название сервиса</td>
                    </tr>
                    <tr>
                        <td>limit</td>
                        <td>ограничение на количество новостей</td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
    <tr>
        <td>/grub</td>
        <td>GET</td>
        <td>
            <table>
                <tbody>
                    <tr>
                        <td>name</td>
                        <td>название сервиса</td>
                    </tr>
                    <tr>
                        <td>url</td>
                        <td>ссылка на статью из сервиса</td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
    <tr>
        <td>/grubs</td>
        <td>POST</td>
        <td>
            Необходимо отправить json.
            <table>
                <tbody>
                    <tr>
                        <td>name</td>
                        <td>название сервиса</td>
                    </tr>
                    <tr>
                        <td>urls</td>
                        <td>список ссылок на новости из сервиса</td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
    <tr>
        <td>/register</td>
        <td>POST</td>
        <td>
            Необходимо отправить json.
            <table>
                <tbody>
                    <tr>
                        <td>name</td>
                        <td>название нового сервиса</td>
                    </tr>
                    <tr>
                        <td>config</td>
                        <td>конфигурация нового сервиса (см. config.json)</td>
                    </tr>
                </tbody>
            </table>
        </td>
    </tr>
    </tbody>
 </table>