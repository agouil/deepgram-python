import logging

FORMAT = '[%(levelname)s]: %(asctime)s [%(pathname)s:%(lineno)s] %(message)s'
logging.basicConfig(format=FORMAT)


def logger():
    """
    Return a logger named 'deepgram' with the format set in FORMAT above.
    """

    return logging.getLogger('deepgram')
