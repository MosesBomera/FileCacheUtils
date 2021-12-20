import logging
import logging.handlers

root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

# Disable external (to project) logging.
for handler in list(root_logger.handlers):
    root_logger.removeHandler(handler)

logfmt_str = "[%(asctime)s %(levelname)s] %(message)s"
formatter = logging.Formatter(logfmt_str, datefmt='%d-%b-%Y %H:%M:%S')

streamHandler = logging.StreamHandler()
streamHandler.setFormatter(formatter)
streamHandler.setLevel(logging.DEBUG)

root_logger.addHandler(streamHandler)