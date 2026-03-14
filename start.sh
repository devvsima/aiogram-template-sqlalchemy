#!/bin/bash

case "$1" in
    run)
        uv run main.py
        ;;
    mapp)
        uv run alembic upgrade head
        ;;
    mgen)
        uv run alembic revision --autogenerate
        ;;
    lcoll)
        uv run pybabel extract --input-dirs=. -o core/locales/bot.pot --project=bot
        ;;
    lupd)
        uv run pybabel update -i core/locales/bot.pot -d core/locales -D bot
        ;;
    lcom)
        uv run pybabel compile -d core/locales -D bot --statistics
        ;;
    *)
        echo "Unknown command: $1"
        echo "Available commands: run, mapply, mgen, lcollect, lupdate, lcompile"
        ;;
esac
