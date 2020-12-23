import json
data = {
        "id": 1345,
        "series": "飞度",
        "image": "https://img.suv666.com/ycyh/cars/model/b63f079399316a8a77a1ecdf98790013_3050.JPG",
        "series_labels": [{
            "label_id": 12,
            "label_sub_name": "运动啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊"
        }, {
            "label_id": 12,
            "label_sub_name": "成熟稳重"
        }],
        "series_vrmodel": {
            "has_vr": 1,
            "video_url": "https://img.suv666.com/ycyh/ar_model/res/car3d-vf-1606412716-43543-preview.mp4",
            "video_cover": "https://img.suv666.com/ycyh/ar_model/res/car3d-vc-1606412716-43543-preview.jpg",
            "video_duration": 15,
            "car_model_id": 43543,
            "car_model_color_id": 29508
        }
    }

#字典转化为字符串
print("data原本类型：",type(data))
with open('exmjson.json','w',encoding='utf-8') as f:
    json.dump(data,f,indent=4,ensure_ascii=False)

#字典转化为字符串，需要写入
data_1=json.dumps(data,indent=7,ensure_ascii=True)
with open('exmjson_1.json','w',encoding='utf-8') as f:
    f.write(data_1)

#json转为字典
with open('exmjson.json','r',encoding='utf-8') as f:
    data_2=json.load(f)
print("exmjson.jsontype使用load转为字段后类型：",type(data_2))

with open('exmjson_1.json','r',encoding='utf-8') as f1:
    res =f1.read()
data_3 = json.loads(res)
print(data_3)
print("exmjson.jsontype使用load转为字段后类型：",type(data_3))