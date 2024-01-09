import pandas as pd
import json

apt_df = pd.read_csv(r"/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/apt.csv")

apt_name = list(apt_df["name"])
school_df = pd.read_csv(r"/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/school.csv")
school_name = list(school_df["name"])
subway_df = pd.read_csv(r"/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/subway.csv")
subway_name = list(subway_df["name"])
emd_df = pd.read_csv(r"/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/emd.csv", encoding="cp949")
dong_name = list(emd_df["name"])
sigungu = pd.read_csv(r"/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/sigungu.csv")
sigungu_list = list(sigungu["name"])


area_1 = []
for i in range(5, 101, 5):
    area_1.append(i)
area_1_pair = []
for i in area_1:
    area_1_pair.append([i-5, i+5])
floor = []
for floor_i in range(1, 101):
    floor.append(floor_i)

area_2 = []
for i in range(16, 330, 10):
    area_2.append(i)
area_2_pair = []
for i in area_2:
    area_2_pair.append([i-5, i+5])

distance_meter = []
distance_meter_to_km = []
for distance in range(100, 1001, 100):
    distance_meter.append(distance)
    distance_meter_to_km.append(distance/1000)

count = []
for count_i in range(1, 31):
    count.append(count_i)

#year
time_year = [1,2,3,4,5]
time_month = [1,2,3,4,5,6,7,8,9,10,11,12]
#day
time_day = []
for i in range(1,30):
    time_day.append(i*10)
#week
time_week = []
for i in range(1,51):
    time_week.append(i)

business_name = ["교촌치킨 서울대점", "락구정", "두레미담"]
building_name = ["우당탕 빌라", "KOEX", "킨텍스"]

data = {
    "apt_name" : apt_name,
    "school_name" : school_name,
    "station_name" : subway_name,
    "dong_name" : dong_name,
    "area_1" : area_1,
    "area_1_pair" : area_1_pair,
    "floor" : floor,
    'gu_name' : sigungu_list,
    "area_2" : area_2,
    "area_2_pair" : area_2_pair,
    "distance_meter" : distance_meter,
    "distance_meter_to_km" : distance_meter_to_km,
    "count" : count,
    'time_year' : time_year,
    'time_month' : time_month,
    'time_week' : time_week,
    'time_day' : time_day,
    'business_name' : business_name,
    'building_name' : building_name

}

with open("/Users/daewoong/Documents/서울대학교/NLP/연구 및 프로젝트/Data Generation/Data to Json/data_to_json.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)