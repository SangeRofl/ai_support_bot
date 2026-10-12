run-all: #для запуска одной командой в теминале make run-all
	cmd /c "start /b uv run uvicorn src.api.main:app --reload && uv run python -m src.bot.bot_test"
