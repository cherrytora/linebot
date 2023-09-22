import pandas as pd
from sheet.gsheet import get_logs

f = "/etc/secrets/gmail-api-81225-f2d876f6c9b6.json"
# f = "sheet/gmail-api-81225-f2d876f6c9b6.json"


def mission_flex(user_id):
    not_stat = {
        "type": "bubble",
        "header": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "text",
                    "text": "任務進度",
                    "size": "xxl",
                    "weight": "bold",
                    "align": "center",
                    "color": "#CDCDB4"
                }
            ],
            "backgroundColor": "#4876FF"
        },
        "body": {
            "type": "box",
            "layout": "vertical",
            "contents": [
                {
                    "type": "box",
                    "layout": "baseline",
                    "margin": "md",
                    "contents": [
                        {
                            "type": "icon",
                            "size": "xl",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xl",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        },
                        {
                            "type": "icon",
                            "size": "xl",
                            "url": "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"
                        }
                    ],
                    "justifyContent": "center"
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "margin": "lg",
                    "spacing": "sm",
                    "contents": [
                        {
                            "type": "box",
                            "layout": "baseline",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "任務尚未開始",
                                    "wrap": True,
                                    "color": "#666666",
                                    "size": "lg",
                                    "flex": 5,
                                    "align": "center"
                                }
                            ]
                        }
                    ]
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": []
                }
            ]
        },
        "footer": {
            "type": "box",
            "layout": "vertical",
            "spacing": "sm",
            "contents": [
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": "查看任務規則",
                        "text": "任務規則"
                    }
                },
                {
                    "type": "button",
                    "style": "link",
                    "height": "sm",
                    "action": {
                        "type": "message",
                        "label": "查看任務路線",
                        "text": "美食推薦"
                    }
                },
                {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [],
                    "margin": "sm"
                }
            ],
            "flex": 0
        }
    }
    icon_list = ["https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                 "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png",
                 "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gray_star_28.png"]
    mission_list = []
    mission = get_logs(user_id)
    print(mission)
    if mission.empty:
        return not_stat
    else:
        mission = list(mission)
        mission = mission[-3]
        for i in range(len(mission)):
            icon_list[i] = "https://scdn.line-apps.com/n/channel_devcenter/img/fx/review_gold_star_28.png"
            mission_list.append(mission[i])

        mission_list.extend("尚未完成" for i in range(3-len(mission_list)))
        flex_dic = {
            "type": "bubble",
            "header": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "任務進度",
                        "size": "xxl",
                        "weight": "bold",
                        "align": "center",
                        "color": "#CDCDB4"
                    }
                ],
                "backgroundColor": "#4876FF"
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "xl",
                                "url": icon_list[0]
                            },
                            {
                                "type": "icon",
                                "size": "xl",
                                "url": icon_list[1]
                            },
                            {
                                "type": "icon",
                                "size": "xl",
                                "url": icon_list[2]
                            }
                        ],
                        "justifyContent": "center"
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "第一站",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": mission_list[0],
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "第二站",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5,
                                        "text": mission_list[1]
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "第三站",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5,
                                        "text": mission_list[2]
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": []
                    }
                ]
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "查看任務規則",
                            "text": "任務規則"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "查看任務路線",
                            "text": "美食推薦"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                ],
                "flex": 0
            }
        }
        return flex_dic
