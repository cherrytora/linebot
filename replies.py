from linebot.v3.messaging import (
    ReplyMessageRequest,
    LocationMessage,
    TemplateMessage, ButtonsTemplate,
    PostbackAction
)
import pandas as pd


def food_recommend(reply_token):
    return ReplyMessageRequest(
        reply_token=reply_token,
        messages=[TemplateMessage(altText="美食推薦",
                                  template=ButtonsTemplate(
                                          title='來天母吃什麼😁',
                                          text='點選路線，讓我來推薦你天母有什麼好吃好喝的！',
                                          actions=[
                                                PostbackAction(
                                                    label='最適合親子一起來的忠誠路👨‍👩‍👧‍👦',
                                                    data="忠誠路",
                                                ),
                                              PostbackAction(
                                                    label='元氣天母西🥳',
                                                    data='天母西路'
                                                ),
                                              PostbackAction(
                                                    label='美食排排站！德行東路～🍲',
                                                    data='德行東路')
                                          ]))])


def postback(name, reply_token):
    store = pd.read_excel("data/店家地址經緯度.xlsx")
    store = store[store["賣方名稱"] == name]
    add = store['add'].values[0]
    latitude = store['緯度'].values[0]
    longitude = store['經度'].values[0]
    msg = LocationMessage(title=name, address=add,
                          latitude=latitude, longitude=longitude)
    return ReplyMessageRequest(reply_token=reply_token, messages=[msg])
