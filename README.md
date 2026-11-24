# Mio Dungeons для GitHub и Bothost

1. Распакуйте внешний `Mio_Dungeons_GitHub.zip`.
2. В корне ветки репозитория откройте **Add file → Upload files** и загрузите все шесть файлов вместе. Файл `mio_dungeons.bundle` оставьте как есть. [Загрузка файлов через браузер](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
3. В Bothost выберите репозиторий и ту же ветку. Укажите Python 3.12 и главный файл `main.py`. Если площадка выбирает другую версию Python, включите собственный Dockerfile. [Точка входа на Bothost](https://bothost.ru/docs/main-file-entrypoint)
4. Укажите токен Telegram в карточке бота. В переменных окружения задайте `DATABASE_URL` для внешнего PostgreSQL, `BOTHOST_MODE=1` и числовой `OWNER_TELEGRAM_ID` для админки. Для Gemini заполните `GEMINI_API_KEY` и `SECRET_ENCRYPTION_KEY` согласно инструкции развёртывания. Храните секреты в панели Bothost.
5. Запустите деплой. При старте `main.py` распакует приложение во временный каталог и применит миграции. Игровое состояние хранится в PostgreSQL.

Проверка содержимого без подключения к базе и Telegram после установки зависимостей выполняется командой `python main.py --check`.

Внутри `mio_dungeons.bundle` находятся исходники, иллюстрации и подробная инструкция `docs/BOTHOST.md`. Формат файла — ZIP.
