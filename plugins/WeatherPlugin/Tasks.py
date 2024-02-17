import requests
import json
from semantic_kernel.plugin_definition import kernel_function, kernel_function_context_parameter


class Tasks:

    @kernel_function(
            description="Get the weather for a city info.",
            name="getCityWeather"
    )
    @kernel_function_context_parameter(
        name="city_name",
        description="The weather of the city"
    )
    def getCityWeatherHelper(self, city_name: str) -> str:
        print("+++++++++++++++++++++++++++")
        print(city_name)

        api_key = "3f10a136a31000a75a9af90f69f01b84"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        print(url)

        response = requests.get(url)

        if response.json()['cod'] == '404':
            print("No City Found")

        if response.status_code != 200:
            raise Exception(response.status_code)
        
        data = response.json()
        return json.dumps(data)
    


        # def getCityWeatherHelper(context: ContextVariables) -> str:
        # print("+++++++++++++++++++++++++++")
        # print(context)
        # city_name = context["city_name"]
        # print(city_name)

        # api_key = "3f10a136a31000a75a9af90f69f01b84"
        # url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
        # print(url)

        # response = requests.get(url)

        # if response.json()['cod'] == '404':
        #     print("No City Found")

        # if response.status_code == 200:
        #     print(response)
        #     return response
        # else:
        #     raise Exception(response.status_code)
        # return "6"
        



