from API_Manager import  API_Manager

if __name__ == "__main__":
    city = input("Please enter your city: ")
    sofia = API_Manager.get_current_weather(city)
    print(sofia)


