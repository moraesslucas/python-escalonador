
class NewProcess:

    def __init__(self, pid, process_time, device_time, process_finish):
        self._pid = pid
        self._process_history = []
        self._process_time = process_time
        self._device_time = device_time
        self._process_finish = process_finish

    def add_history(self, value):
        self._process_history.append(value)

    @property
    def process_time(self):
        return self._process_time

    @process_time.setter
    def process_time(self, value):
        self._process_time = value

    @property
    def process_finish(self):
        return self._process_finish

    @process_finish.setter
    def process_finish(self, value):
        self._process_finish = value

    @property
    def device_time(self):
        return self._device_time

    @device_time.setter
    def device_time(self, value):
        self._device_time = value

    @property
    def pid(self):
        return self._pid

    @property
    def history(self):
        return self._process_history

    def process(self):
        if self.process_time > 0:
            self.process_time -= 1
        elif self.process_finish > 0:
            self.process_finish -= 1