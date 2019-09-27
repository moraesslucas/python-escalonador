from runner import Runner
from new_process import NewProcess

runner = Runner()

runner.add_process(NewProcess(1, 4, 3, 2))
runner.add_process(NewProcess(2, 2, 5, 3))
runner.add_process(NewProcess(3, 4, 3, 3))

runner.run(2)
runner.print_order()
