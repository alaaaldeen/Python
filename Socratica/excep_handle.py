import time
import logging

# Create a logger
logging.basicConfig(filename="D:/problems.log",
                    level=logging.DEBUG)
logger = logging.getLogger()


def read_file_timed(path):
    """Return the contents of the file at 'path' and measure time required."""
    s_time = time.time()
    try:
        f = open(path, mode="rb")
        data = f.read()
        return data
    except IOError as err:
        logger.error(err)
        raise
    else:
        f.close()
    finally:
        stop_time = time.time()
        dt = stop_time - s_time
        logger.info("Time required for {file} = {time}".format(file=path,
                                                                time=dt))


data = read_file_timed("D:/Library/ex44.mp4")
