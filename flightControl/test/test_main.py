import time

from flightControl.compoents.logger import Logger
from flightControl.test.controllerTest import TestInterface, TestController

data_points_needed = 500
interface = TestInterface()
logger = Logger()

test_controller = TestController(interface, logger)

data_points_count = 0
target = 0
while data_points_count < data_points_needed:
    time.sleep(0.01)
    if data_points_count == round(data_points_needed / 4):
        target = 50
        print("25%")
    elif data_points_count == round(data_points_needed / 2):
        target = 100
        print("50%")
    elif data_points_count == round(3 * data_points_needed / 4):
        target = 25
        print("75%")
    data_points_count += 1
    interface.update()
    test_controller.update(target)

# time_code = []
# reading_value = []
# output_value = []
# for log in logger.logs:
#     if log.data_type == "reading":
#         time_code.append(log.time - logger.starting_time)
#         reading_value.append(log.content)
#     elif log.data_type == "output":
#         output_value.append(log.content)
#
# plt.subplot(2, 1, 1)
# plt.plot(time_code, reading_value)
# plt.ylabel("reading")
# plt.subplot(2, 1, 2)
# plt.plot(time_code, output_value)
# plt.ylabel("output")
# plt.show()

logger.save()