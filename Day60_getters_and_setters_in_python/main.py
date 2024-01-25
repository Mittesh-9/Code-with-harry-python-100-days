class Myclass:
    def __init__(self, value):
        self._value = value

    def show(self):
            print(f"Value is {self._value}")

    @property
    def ten_times_value(self):
        return 10 * self._value
        
    @ten_times_value.setter
    def ten_times_value(self, new_value):
        self._value = new_value / 10

obj = Myclass(10)

obj.ten_times_value = 69

print(obj.ten_times_value)
obj.show()
