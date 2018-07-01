from weather import Weather, Unit

weather = Weather(unit=Unit.FAHRENHEIT)

print('Welcome to the ACME Weather Program' + '\n')

def forecast(city,number_of_days):
#Yahoo Weather App API Documentation: https://developer.yahoo.com/weather/documentation.html?guccounter=1
    location = weather.lookup_by_location(city)
    forecasts = location.forecast
    for x in range(0,number_of_days):
        print ('\n' + 'Date: ' + forecasts[x].day+ ' ' + forecasts[x].date)
        print ('Weather Conditions: '+ forecasts[x].text)
        print ('Hight Temp: ' + forecasts[x].high)
        print ('Low Temp: ' + forecasts[x].low + '\n')

skyisblue = True
while skyisblue != False:
    city = input("Enter the city you would like the weather for: ")
    number_of_days = input("Number of days you would like the forecast? (1 - 10) ")

    if int(number_of_days) <= 10:
        forecast(city,int(number_of_days))
    else:
        print("Invalid input detected, please eneter a number between 1 - 10")

    