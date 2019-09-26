
class Runner:

    def __init__(self):
        self._original_processes = []
        self._available_process = []
        self._blocked_processes = []
        self._finished_processes = []
        self._running_process = None
        self._running_device = None

    def add_process(self, process):
        self._available_process.insert(0, process)
        self._original_processes.append(process)

    def run(self, original_timeslice):
        timeslice = original_timeslice
        while len(self._original_processes) > 0:
            if self._running_process is not None:
                if self._running_process.process_finish == 0:
                    self._original_processes.remove(self._running_process)
                    self._finished_processes.append(self._running_process)
                    self._running_process = None
                elif self._running_process.process_time == 0 and self._running_process.device_time > 0:
                    self._blocked_processes.insert(0, self._running_process)
                    self._running_process = None
                elif timeslice < 1 and len(self._available_process) > 0:
                    self._available_process.insert(0, self._running_process)
                    self._running_process = None

            if self._running_device is not None:
                if self._running_device.device_time == 0:
                    self._available_process.insert(0, self._running_device)
                    self._running_device = None
                    if len(self._blocked_processes) > 0:
                        self._running_device = self._blocked_processes.pop()
            elif len(self._blocked_processes) > 0 and self._running_device is None:
                self._running_device = self._blocked_processes.pop()

            if len(self._available_process) > 0 and self._running_process is None:
                timeslice = original_timeslice
                self._running_process = self._available_process.pop()

            if self._running_process is not None:
                self._running_process.add_history("X")
                self._running_process.process()
                timeslice -= 1

            if self._running_device is not None:
                self._running_device.add_history("D")
                self._running_device.device_time -= 1

            for process in self._available_process:
                process.add_history("W")

            for process in self._blocked_processes:
                process.add_history("B")

            for process in self._finished_processes:
                process.add_history("T")

        for process in self._finished_processes:
            print(process.pid)
            print(process.history)