from weather import Weather, Unit

weather = Weather(unit=Unit.FAHRENHEIT)

print('Welcome to the ACME Weather Program' + '\n')

def forecast(x,y):
#Yahoo Weather App API Documentation: https://developer.yahoo.com/weather/documentation.html?guccounter=1
    location = weather.lookup_by_location(x)
    forecasts = location.forecast
    for x in range(0,y):
        print ('\n' + 'Date: ' + forecasts[x].day+ ' ' + forecasts[x].date)
        print ('Weather Conditions: '+ forecasts[x].text)
        print ('Hight Temp: ' + forecasts[x].high)
        print ('Low Temp: ' + forecasts[x].low + '\n')

skyisblue = True
while skyisblue != False:
    city = input("Enter your city: ")
    number_of_days = input("Number of day you would like the forecast? (1 - 10) ")

    if int(number_of_days) <= 10:
        forecast(city,int(number_of_days))
    else:
        print("Invalid input detected, please eneter a number between 1 - 10")

    