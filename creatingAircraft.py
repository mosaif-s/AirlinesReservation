import csv
import random
import os.path
import os
file_exists = os.path.exists('Aicraft.csv')
if file_exists==True:
    os.remove('Aircraft.csv')
f=open("Aircraft.csv","w+",newline='')
a=csv.writer(f)
header=['Fl_No','Aircraft','Capacity','From','Desti','Depart','Arrival','Total']
a.writerow(header)
cities=['Abidjan', 'ACCRA', 'Adana', 'ADDIS ABABA', 'Adelaide', 'Agra', 'Ahmadabad', 'Aleppo(Halab)', 'Alexandria', 'ALGIERS', 'Allahabad', 'ALMATY', 'AMMAN', 'Amritsar', 'ANKARA', 'Anshan', 'BAGHDAD', 'Baku', 'Bandung', 'Bangalore', 'BANGKOK', 'Baotou', 'Barcelona', 'Barquisimeto', 'Barranquilla', 'Basrah', 'BEIJING', 'BEIRUT', 'Belem', 'BELGRADE', 'Belo Horizonte', 'Benghazi', 'Benin', 'BERLIN', 'Bhopal', 'Birmingham', 'BOGOTA', 'BRASILIA', 'BRAZZAVILLE', 'Brisbane', 'BUCHAREST', 'BUDAPEST', 'BUENOS AIRES', 'Bursa', 'Busan', 'CAIRO', 'Cali', 'Campinas', 'Capetown', 'CARACAS', 'Casablanca', 'Changchun', 'Changsha', 'Changzhou', 'Chelyabinsk', 'Chengdu', 'Chennai', 'Chicago', 'Chittagong', 'Chongquin', 'Ciudad Juarez', 'CONAKRY', 'COPENHAGEN', 'Cordoba', 'Curitiba', 'Daegu', 'Daejon', 'DAKAR', 'Dalian', 'Dallas', 'DAMASCUS', 'DAR ES SALAAM', 'Datong', 'DELHI', 'DHAKA', 'Dnipropetrovsk', 'Donetsk', 'Douala', 'Durban', 'Ecatepec', 'Ekaterinburg', 'Faisalabad', 'Fortaleza', 'Foshan', 'FREETOWN', 'Fukuoka', 'Fuzhou', 'Giza', 'Goiania', 'Guadalajara', 'Guangzhou', 'Guarulhos', 'GUATAMALA CITY', 'Guayaquil', 'Guiyang', 'Gujranwala', 'Gwangju', 'Haiphong', 'Hamburg', 'Handan', 'Hangzhou', 'HANOI', 'Haora', 'HARARE', 'Harbin', 'HAVANA', 'Hefei', 'Hiroshima', 'Ho Chi Minh City', 'Hong Kong', 'Houston', 'Hyderabad', 'Hyderabad', 'Ibadan', 'Incheon', 'Indore', 'Irbil', 'Isfahen', 'Istanbul', 'Izmir', 'Jaipur', 'JAKARTA', 'Jeddah', 'Jilin', 'Jinan', 'Jodphur', 'Johannesburg', 'KABUL', 'Kaduna', 'Kano', 'Kanpur', 'Kaohsiung', 'Karachi', 'Kawasaki', 'Kazan', 'Kharkiv', 'KHARTOUM', 'Khulna', 'KIEV', 'KINSHASA', 'Kitakyushu', 'Kobe', 'Kolkata', 'Kowloon', 'KUALA LUMPUR', 'Kunming', 'Kyoto', 'LA PAZ', 'Lagos', 'Lahore', 'Lanzhou', 'Leon', 'LIMA', 'LONDON', 'Los Angeles', 'LUANDA', 'Lubumbashi', 'Lucknow', 'Ludhiana', 'Luoyang', 'LUSAKA', 'MADRID', 'Maiduguri', 'Makassar', 'MANAGUA', 'Manaus', 'MANILA', 'MAPUTO', 'Maracaibo', 'Mashhad', 'Mecca', 'Medan', 'Medellin', 'Medina', 'Meerut', 'Melbourne', 'Mexicali', 'MEXICO CITY', 'Milan', 'MINSK', 'MOGADISHU', 'Monterrey', 'MONTEVIDEO', 'Montreal', 'MOSCOW', 'Mosul', 'Multan', 'Mumbai (Bombay)', 'Munich', 'Nagoya', 'Nagpur', 'NAIROBI', 'Nanchang', 'Nanjing', 'Nanning', 'Napoli', 'Nashik', 'New York City', 'Nezahualcoyotl', 'Nizhny Novgorod', 'Novosibirsk', 'Odessa', 'Omdurman', 'Omsk', 'Osaka', 'Palembang', 'PARIS', 'Patna', 'Perm', 'Perth', 'Peshawar', 'Philadelphia', 'PHNOM PENH', 'Phoenix', 'Pimpri Chinchwad', 'Port Harcourt', 'PORT-AU-PRINCE', 'Porto Alegre', 'PRAGUE', 'Puebla', 'Pune', 'PYONGYANG', 'Qingdao', 'Qiqihar', 'QUITO', 'RABAT', 'Rajkot', 'Ranchi', 'Rawalpindi', 'Recife', 'Rio de Janeiro', 'RIYADH', 'ROME', 'Rosario', 'Rostov on Don', 'Salvador', 'Samara', 'San Antonio', 'San Diego', 'SANAA', 'Santa Cruz', 'SANTIAGO', 'SANTO DOMINGO', 'Sao Paulo', 'Sapporo', 'Semarang', 'Sendai', 'Seongnam', 'Seoul', 'Shanghai', 'Shenyang', 'Shenzhen', 'Shiraz', 'Shiziahuang', 'Shubra El Kheima', 'SINGAPORE', 'SOFIA', 'Soweto', 'St Petersburg', 'STOCKHOLM', 'Surabaya', 'Surat', 'Suzhou', 'Sydney', 'Tabriz', 'Taichung', 'TAIPEI', 'Taiyuan', 'Tangshan', 'TASHKENT', 'TBILISI', 'Tegucigalpa', 'TEHRAN', 'Tianjin', 'Tijuana', 'TOKYO', 'Toronto', 'TRIPOLI', 'TSHWANE (PRETORIA)', 'TUNIS', 'Ufa', 'Ulsan', 'Urumqi', 'Vadodara', 'Valencia', 'Varanasi', 'VIENNA', 'Volgograd', 'WARSAW', 'Wuhan', 'Wuxi', 'Xian', 'Xuzhou', 'Yangon', 'YAOUNDE', 'Yerevan', 'Yokohama', 'Zapopan', 'Zhengzhou', 'Zibo']
for i in range(20):
    fromc=random.choice(cities)
    desti=random.choice(cities)
    if fromc==desti:
        while fromc==desti:
            desti==random.choice(cities)
    capacity=random.randrange(200,300,5)
    totalcost=random.randrange(20000,30000,1000)
    aircraft=random.randint(1,9)
    flnno=100+i
    timelist=['00','01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    hour=random.choice(timelist)
    hourindex=timelist.index(hour)
    minute=random.randrange(0,60,5)
    if minute==0:
        minute='00'
    elif minute==5:
        minute='05'
    departure=hour+':'+str(minute)
    if hourindex==20:
        hour2=random.choice(['21','22','23','01'])
    elif hourindex==21:
        hour2=random.choice(['22','23','01','02',])
    elif hourindex==22:
        hour2=random.choice(['23','01','02','03'])
    elif hourindex==23:
        hour2=random.choice(['01','02','03','04'])
    else:
        hourindex2=hourindex+random.randint(1,4)
        hour2=timelist[hourindex2]
    minute2=random.randrange(0,60,5)
    if minute2==0:
        minute2='00'
    elif minute2==5:
        minute2='05'
    arrival=hour2+':'+str(minute2)
    record=['HA'+str(flnno),'AB'+str(aircraft),capacity,fromc,desti,departure,arrival,totalcost]
    print(record)
    a.writerow(record)
f.close()

    
    
                     
    
        
    
    
    
    
    
    
