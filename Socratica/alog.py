import logging

# Configure the logging system
# First configure the sataus messages or trail stream
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# Configure logging settings
logging.basicConfig(filename="D:\\Script\\lumberjack.log",
                    # Debug level to display all
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
# Creating logger object by calling getLogger method
logger = logging.getLogger()

# Test messages
logger.debug("This is a normal debug message.")
logger.info("Just some useful info.")
logger.warning("I'm sorry, but I can't do that, Dave.")
logger.error("Did you just try to divide by zero")
logger.critical("The entire internet is down!!")
