from linebot.v3.messaging import (
    ReplyMessageRequest,
    TextMessage,
    TemplateMessage, ButtonsTemplate,CarouselTemplate, CarouselColumn,
    PostbackAction, MessageAction, URIAction
)

def food_recommend(reply_token):
    return ReplyMessageRequest(
            reply_token=reply_token,
            messages=[TemplateMessage(altText="美食推薦",
                                        template=ButtonsTemplate(
                                        title='來天母吃什麼😁',
                                        text='點選路線，讓我來推薦你天母有什麼好吃好喝的！',
                                        actions=[
                                            PostbackAction(
                                                label='天母西三叉路',
                                                data="天母西三叉路",
                                            ),
                                            PostbackAction(
                                                label='天母西路',
                                                data='天母西路'
                                            ),
                                            PostbackAction(
                                                label='天母東路',
                                                data='天母東路')
                                            ]))])

def route_recommend(reply_token):
    return ReplyMessageRequest(
            reply_token=reply_token,
            messages=[TemplateMessage(altText="美食推薦",
                                        template=CarouselTemplate(
                                        columns=[
                                            CarouselColumn(
                                                title='this is menu1',
                                                text='description1',
                                                actions=[
                                                    PostbackAction(
                                                        label='postback1',
                                                        text='postback text1',
                                                        data='action=buy&itemid=1'
                                                    ),
                                                    MessageAction(
                                                        label='message1',
                                                        text='message text1'
                                                    ),
                                                    # URIAction(
                                                    #     label='uri1',
                                                    #     uri='http://example.com/1'
                                                    # )
                                                ]
                                            ),
                                            CarouselColumn(
                                                thumbnail_image_url='顯示在開頭的大圖片網址',
                                                title='this is menu2',
                                                text='description2',
                                                actions=[
                                                    PostbackAction(
                                                        label='postback2',
                                                        text='postback text2',
                                                        data='action=buy&itemid=2'
                                                    ),
                                                    MessageAction(
                                                        label='message2',
                                                        text='message text2'
                                                    ),
                                                    # URIAction(
                                                    #     label='連結2',
                                                    #     uri='http://example.com/2'
                                                    # )
                                                        ])]))])
                                        
   
            




