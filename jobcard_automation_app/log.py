import logging

# Tạo logger chung
logger = logging.getLogger("main_logger")
logger.setLevel(logging.DEBUG)

# Tạo formatter chung cho các log file
formatter = logging.Formatter('Case -  - %(message)s')

# Tạo handler cho success log
success_handler = logging.FileHandler('success.log')
success_handler.setLevel(logging.INFO)  # Ghi thông tin về success
success_handler.setFormatter(formatter)

# Tạo handler cho fail log
fail_handler = logging.FileHandler('fail.log')
fail_handler.setLevel(logging.WARNING)  # Ghi thông tin về fail
fail_handler.setFormatter(formatter)

# Tạo handler cho error log
error_handler = logging.FileHandler('error.log')
error_handler.setLevel(logging.ERROR)  # Ghi thông tin về error
error_handler.setFormatter(formatter)

# Thêm handler vào logger
logger.addHandler(success_handler)
logger.addHandler(fail_handler)
logger.addHandler(error_handler)
