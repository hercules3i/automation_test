import logging

# Tạo logger chung
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)

# Tạo formatter chung cho các log file
formatter = logging.Formatter('%(message)s')

# Tạo custom filter cho các mức log cụ thể
class InfoFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.INFO

class WarningFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.WARNING

class ErrorFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.ERROR

# Tạo handler cho success log
success_handler = logging.FileHandler('success.log', encoding='utf-8')
success_handler.setLevel(logging.INFO)  # Chỉ ghi thông tin thành công
success_handler.setFormatter(formatter)
success_handler.addFilter(InfoFilter())  # Chỉ ghi INFO

# Tạo handler cho fail log
fail_handler = logging.FileHandler('fail.log', encoding='utf-8')
fail_handler.setLevel(logging.WARNING)  # Chỉ ghi cảnh báo
fail_handler.setFormatter(formatter)
fail_handler.addFilter(WarningFilter())  # Chỉ ghi WARNING

# Tạo handler cho error log
error_handler = logging.FileHandler('error.log', encoding='utf-8')
error_handler.setLevel(logging.ERROR)  # Chỉ ghi lỗi
error_handler.setFormatter(formatter)
error_handler.addFilter(ErrorFilter())  # Chỉ ghi ERROR

# Thêm handler vào logger
logger.addHandler(success_handler)
logger.addHandler(fail_handler)
logger.addHandler(error_handler)

# # Ghi log vào success.log (mức INFO)
# logger.info("Thao tác thành công!")

# # Ghi log vào fail.log (mức WARNING)
# logger.warning("Thao tác có thể gây lỗi!")

# # Ghi log vào error.log (mức ERROR)
# logger.error("Lỗi nghiêm trọng!")
