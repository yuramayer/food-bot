# Учёт калорий 🥗 - Разработка


Здесь ведётся активная разработка бота.

> Код в `main` может быть устаревшим

## Деплой

Задеплоим ботик на линукс-серваке

### Пути

- Бот склонирован в директорию: `/opt/food-bot`
- Системный файл запуска лежит здесь: `/etc/systemd/system/food-bot.service`

### Файл `food-bot.service`

```text
[Unit]
Description=Food Bot Python Service
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/food-bot
ExecStart=/opt/food-bot/.venv/bin/python /opt/food-bot/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

### Команды `systemd`

```bash
>>> sudo systemctl daemon-reload
>>> sudo systemctl enable food-bot.service
>>> sudo systemctl start food-bot.service
```
