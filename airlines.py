


class put_data:


    def __init__(self, data):
        self.data = data
    def update_data(self):
        print("hi")
        for x in range(len(self.data)):
            for key in self.data[x]:
                print(key)
                if key == "iataCode":
                    if len(self.data[x][key]) <=1:
                        self.data[x]["iataCode"] = "TESTING"
        return self.data

