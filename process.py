# from state import State
#
#
# class Process:
#
#     def __init__(self, pid, process_time, device_time, process_time_leftover):
#         self._pid = pid
#         self._process_time = process_time
#         self._device_time = device_time
#         self._process_time_leftover = process_time_leftover
#         self._status = State.WAITING_TO_START
#
#     @property
#     def pid(self):
#         return self._pid
#
#     @property
#     def device_time(self):
#         return self._device_time
#
#     @property
#     def process_time(self):
#         return self._process_time
#
#     @process_time.setter
#     def process_time(self, value):
#         self._process_time = value
#
#     @property
#     def process_time_leftover(self):
#         return self._process_time_leftover
#
#     @process_time_leftover.setter
#     def process_time_leftover(self, value):
#         self._process_time_leftover = value
#
#     @property
#     def status(self):
#         return self._status
#
#     @status.setter
#     def status(self, value):
#         self._status = value
#
#     def run(self):
#         if self._process_time > 0:
#             self._process_time -= 1
#         else:
#             self._process_time_leftover -= 1
#         self._status = State.RUNNING_PROCESS
#         return self._status
#
#     def device_run(self):
#         self._device_time -= 1
#         self._status = State.RUNNING_DEVICE
#         return self._status
#
#     def __str__(self):
#         return self._pid
