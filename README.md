# Описание:

- Сервис позволяет добавлять статистику по дням, добавлять просмотры, клики , цену клика.
- Получать статистику за любой день с сортировкой по нужному параметру.
- Удалять статистику за любой день.

# API:

- /api/v1/statistic/save - POST запрос, сохраняет статистику в БД
- /api/v1/statistic/get - POST запрос, возвращает статистику из БД
- /api/v1/statistic/delete - DELETE запрос, удаляет статистику из БД

# Линтеры:

- black
- flake8
- mypy

# Подробнее по каждому API

## Сохранение статистики:

`/api/v1/statistic/save` - POST запрос, сохраняет статистику в БД
  - Принимает json вида:
  `{
    "user_id": 1,
    "date": {
        "year": 2020,
        "month": 1,
        "day": 1
    },
    "views": 100,
    "clicks": 10,
    "cost": 100.0
    }`
  - Ответ вида:
  `{
    "message": "OK"
  }`
  
## Получение статистики:

`/api/v1/statistic/get` - POST запрос, возвращает статистику из БД

- Принимает json вида:
`{
  "user_id": 1,
  "date": {
      "year": 2020,
      "month": 1,
      "day": 1
  },
  "sort_method": "views"
}`

- Ответ вида:

`[
{
  "date": "2020-01-01 00:00:00",
  "views": 100,
  "clicks": 10,
  "cost": 100.0,
  "cpc": 10.0,
  "cpm": 10000.0
},
]`

## Удаление статистики:

- `/api/v1/statistic/delete` - DELETE запрос, удаляет статистику из БД
  
  - Ответ вида:
  `{
    "message": "OK"
  }`

# Запуск проекта:

- copy example_env .env
- docker-compose build
- docker-compose up -d
- в Docker file изменить environment для db
