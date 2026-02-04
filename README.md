# messaging-backend

This repository handles messaging capabilities for QueueBot (@nuscqbot). It is supplementary to main functionalities of the bot's miniapp (refer to https://github.com/usdevs/QueueBot)

## Run

- I used `uv` to manage this python project. I used python as it is the simplest for telebot API integration.

- Setup instructions:
```bash
uv sync
echo "BOT_TOKEN=your_token" > .env
uv run python main.py
```

- `BOT_TOKEN` refers to the token for @nuscqbot (given when registering with Bot Father)
