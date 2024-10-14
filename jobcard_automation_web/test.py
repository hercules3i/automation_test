# import logging

# # Cấu hình logger với tệp tin
# logging.basicConfig(
#     filename='app.log',  # Tên tệp tin để lưu thông báo
#     filemode='a',        # 'a' để ghi thêm (append), 'w' để ghi đè (overwrite)
#     level=logging.DEBUG,  # Mức độ ghi lại
#     format='%(asctime)s - %(levelname)s - %(message)s',  # Định dạng ghi lại
# )

# def perform_task(task_name):
#     try:
#         # Giả sử đây là một công việc mà bạn muốn thực hiện
#         if task_name == "task1":
#             logging.info("Bắt đầu thực hiện task1.")
#             # Một số logic ở đây
#             logging.info("task1 thực hiện thành công!")
#         elif task_name == "task2":
#             logging.info("Bắt đầu thực hiện task2.")
#             # Một số logic ở đây
#             raise ValueError("Đã xảy ra lỗi trong task2.")
#         else:
#             logging.warning("task không hợp lệ.")
#     except Exception as e:
#         logging.error(f"Lỗi khi thực hiện {task_name}: {e}")

# # Gọi hàm với các task khác nhau
# perform_task("task1")  # Ghi lại thành công
# perform_task("task2")  # Ghi lại lỗi
# perform_task("task3")  # Ghi lại cảnh báo
