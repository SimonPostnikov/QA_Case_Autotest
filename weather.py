from pyowm import OWM

owm = OWM('87fe4f7ba7f91ba011374c294976399e')
city = input('Введите название города:   ')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(city)
w = observation.weather
temperature = w.temperature('celsius')['temp']
wind=w.wind()['speed']
print('Сейчас  ' + str(temperature) + ' градусов в' + str(city))
print(str(wind) + ' метров в секунду!')
