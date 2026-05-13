import sys


class CustomException(Exception):

    def __init__(self, error_message, error_detail: sys):

        super().__init__(error_message)

        self.error_message = self.get_error_message(
            error_message,
            error_detail
        )

    def get_error_message(self, error_message, error_detail):

        _, _, exc_tb = error_detail.exc_info()

        file_name = exc_tb.tb_frame.f_code.co_filename

        message = f"""
        Error occurred in python script:
        [{file_name}]

        Line number:
        [{exc_tb.tb_lineno}]

        Error message:
        [{error_message}]
        """

        return message

    def __str__(self):

        return self.error_message