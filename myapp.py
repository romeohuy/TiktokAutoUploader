#from tsup.tiktok.sessionId.uploader import  upload2NewTiktokSessionId, upload2TiktokSessionId, uploadImage
#from tsup.utils.tools import get_duration_timestamp
from flask import Flask
from flask import request

from tiktok_uploader import Video, tiktok
import random
app = Flask(__name__)
nature_titles = [
    "Khám phá vẻ đẹp thiên nhiên",
    "Hành trình khám phá rừng xanh",
    "Thế giới dưới lòng đại dương",
    "Ngắm hoàng hôn tuyệt đẹp",
    "Bình minh trên đỉnh núi",
    "Cảnh quan thiên nhiên hùng vĩ",
    "Vẻ đẹp của mùa thu",
    "Thiên nhiên hoang dã",
    "Thác nước hùng vĩ",
    "Cánh đồng hoa bất tận",
    "Dòng suối trong lành",
    "Rừng thông yên tĩnh",
    "Vườn quốc gia tuyệt đẹp",
    "Thiên nhiên kỳ bí",
    "Hành trình khám phá động vật hoang dã",
    "Cảm nhận thiên nhiên",
    "Thiên đường nhiệt đới",
    "Vẻ đẹp của biển cả",
    "Cảnh đẹp vùng quê",
    "Thiên nhiên hoang sơ"
    # "Tết 2025: Nhà bạn sao rồi?",
    # "Tết nay ăn gì hot?",
    # "Trend Tết 2025 là gì?",
    # "Tết xưa vs Tết nay",
    # "Chọn outfit Tết siêu xịn!",
    # "Bánh chưng nhà bạn đâu?",
    # "Ngày đầu năm đi đâu?",
    # "Check-in Tết cực chill!",
    # "Xuân này bạn đã có ai?",
    # "Tết truyền thống còn không?",
    # "Góc sống ảo Tết 2025!"
]

nature_hashtags = [
    "travel", "travelgram", "travelblogger", "travelphotography", "travelvlog",  
    "wanderlust", "explore", "adventure", "nature", "trip", "vacation",  
    "backpacking", "roadtrip", "solotravel", "beach", "mountains", "sunset",  
    "traveladdict", "passportready", "beautifuldestinations", "instatravel",  
    "travelholic", "bucketlist", "traveldiaries", "discover", "hiddenparadise",  
    "tiktoktravel", "amazingplaces", "landscape", "worldtravel", "naturelovers"
]

# Số lượng tiêu đề muốn chọn ngẫu nhiên
num_tag = 5
@app.route('/upload', methods=['POST'])
def upload_video():    
    try:
        file = request.files['file']
        bt = file
        #json = request.form.get('inputField')
        sessionid =  request.form.get('sessionid')
        #file = json.get('file')
        title = request.form.get('title')
        if title == '':
           title = random.choice(nature_titles)
        
        tags = request.form.getlist('tags')
        if not tags:
            tags = random.sample(nature_hashtags, num_tag)
        result = tiktok.upload_video(
        sessionid, file, title, 0,
        allow_comment= 1, allow_duet= 0, allow_stitch= 0, visibility_type=1,
        brand_organic_type=0, branded_content_type=0, ai_label=0, proxy = None,
        )
        print(str(result))
        print(title)
        return str(result)
    except Exception:
        return "False"
    #return str(uploadVideo(session_id, file, title, tags, verbose=True))
    
@app.route('/upload-avatar', methods=['POST'])
def upload_avatar():    
    
    sessionid =  request.form.get('sessionid')
    
    result = uploadImage(sessionid)
    print(str(result))
    if str(result).__contains__('<html'):
        print("------- False -------")
        return "False"
    return str(result)
    #return str(uploadVideo(session_id, file, title, tags, verbose=True))
				
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9111)