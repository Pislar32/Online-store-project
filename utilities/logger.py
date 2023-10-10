import datetime
import os


class Logger():
    """Класс отвечает за создание логов"""
    file_name = f"D:\\QA_обучение\\Final_Project\\Logs\\log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    @classmethod # декоратор класс-метод, нужен для создания методов класса, которые могут быть вызваны без создания экземпляра класса
    def write_log_to_file(cls, data: str):
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            """with - с, на, у, от, за, в, используется для открытия и закрытия чего-либо и только в одном файле"""
            logger_file.write(data) # data - это данные, которые мы будем записывать

    @classmethod
    def add_start_step(cls, method: str):
        test_name = os.environ.get('PYTEST_CURRENT_TEST') # environ - окружающая среда

        data_to_add = f"\n-----\n" # разграничение между логами, чтоб они не сливались
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start name method: {method}\n"
        data_to_add += "\n"

        cls.write_log_to_file(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):

        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End name method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.write_log_to_file(data_to_add)
