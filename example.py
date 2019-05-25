from cloud_logger.__init__ import CloudLogger,CloudLoggerObject,CloudHandler
import logging

if __name__ == '__main__':
    # Setup cloud_logger
    logger_obj = CloudLoggerObject(
        name='xxx',
        format='%(asctime)s : %(levelname)s : %(filename)s  a %(funcName)s %(message)s',
    )
    logger = logging.getLogger(__name__)
    logger.addHandler(CloudHandler(
        logger_obj=logger_obj
    ))
    logger.setLevel(logging.DEBUG)

    def foobar1():
        logger.error('foobar2')
        logger.warn('a')
        logger.fatal('a')

    foobar1()