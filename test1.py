import requests

def get_weather_by_city_id(city_id, api_key, api_host="api_host"):
    """
    根据城市ID查询当前天气信息
    参数:
        city_id: 城市ID(可在和风天气官网查询)
        api_key: 和风天气API密钥
        api_host: 你的API Host(从控制台-设置获取)
    返回:
        dict: 包含温度和天气状况的字典,失败时返回None
    """
    # 和风天气实时天气API接口（使用你自己的API Host）
    url = f"https://{api_host}/v7/weather/now?location={city_id}&key={api_key}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        weather_data = response.json()
        
        if weather_data.get("code") != "200":
            print(f"API错误:{weather_data.get('code')} - {weather_data.get('msg', '无错误信息')}")
            return None
        
        now_weather = weather_data["now"]
        return {
            "temperature": now_weather["temp"],
            "weather": now_weather["text"],
            "city_id": city_id
        }
    
    except requests.exceptions.HTTPError as e:
        if response.status_code == 403:
            print("错误:403 访问被拒绝,请检查API Key、API Host是否正确,或是否超出请求频率限制")
        else:
            print(f"HTTP错误:{e}")
        return None
    except Exception as e:
        print(f"未知错误：{str(e)}")
        return None

if __name__ == "__main__":
    # 替换为你的实际信息
    API_KEY = "API_KEY"
    API_HOST = "API_HOST"
    
    city_id = input("请输入城市ID:").strip()
    if not city_id:
        print("错误:城市ID不能为空")
    else:
        weather_info = get_weather_by_city_id(city_id, API_KEY, API_HOST)
        if weather_info:
            print(f"\n城市ID {weather_info['city_id']} 的当前天气：")
            print(f"温度：{weather_info['temperature']}℃")
            print(f"天气状况：{weather_info['weather']}")