import os
# import uvicorn
import pandas as pd
from datetime import datetime
import pytz
import json
from dotenv import load_dotenv

from fastapi import Request, FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from linebot.v3 import (
    WebhookParser
)
from linebot.v3.messaging import (
    AsyncApiClient,
    AsyncMessagingApi,
    Configuration,
    ReplyMessageRequest,
    TextMessage,
    FlexMessage, LocationMessage
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.webhooks import (
    MessageEvent, PostbackEvent
)

from linebot.v3.messaging.models import FlexContainer

import replies
from sheet.gsheet import write_records, get_logs


load_dotenv()

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)

# bot init
configuration = Configuration(
    access_token=channel_access_token
)

app = FastAPI()

# liff page
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/liff", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("liff.html", {"request": request})

# bot
async_api_client = AsyncApiClient(configuration)
line_bot_api = AsyncMessagingApi(async_api_client)
parser = WebhookParser(channel_secret)
# store list
store = pd.read_excel('data/店家名單.xlsx')
store = list(store["店家"])


@app.post("/")
async def handle_callback(request: Request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = await request.body()
    body = body.decode()

    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        print(event)
        if isinstance(event, PostbackEvent):
            if event.postback.data == "天母西三叉路":
                pass
            elif event.postback.data == "天母西路":
                msg = json.load(open('data/rout1.json', 'r', encoding='utf-8'))
                message = FlexMessage(
                    alt_text="天母東路", contents=FlexContainer.from_dict(msg))
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[message]
                    )
                )
            elif event.postback.data == "天母東路":
                pass
            else:
                await line_bot_api.reply_message(
                    replies.postback(event.postback.data, event.reply_token))

        elif isinstance(event, MessageEvent):
            if event.message.text == "任務規則":
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(
                            text="任務店家分成A、B, 累積在A和B店各一次消費,任務數量會+1,當完成5個任務數量後,則可以取贈品🎁喔！")]
                    )
                )

            elif event.message.text == "任務進度":
                # txt = get_logs(str(event.source.user_id))
                # 這裡寫一個py檔，讓他return dic
                msg = json.load(open('data/flex.json', 'r', encoding='utf-8'))
                message = FlexMessage(
                    alt_text="任務進度", contents=FlexContainer.from_dict(msg))
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[message]
                    )
                )

            elif event.message.text == "美食推薦":
                await line_bot_api.reply_message(
                    replies.food_recommend(event.reply_token)
                )

            elif event.message.text in store:
                now = datetime.now(pytz.timezone("Asia/Taipei"))
                mission = ["None", str(event.source.user_id), str(
                    event.message.text), "Y", str(now)]
                write_records(mission)
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(text="任務集點成功！")]
                    )
                )

            else:
                await line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[TextMessage(
                            text="請點選下列選單，我才能告訴你天母有什麼好吃好玩的喔！")]
                    )
                )

    return 'OK'


# if __name__ == "__main__":
#     uvicorn.run("bot:app", reload=True)
