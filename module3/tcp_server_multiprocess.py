#!/usr/bin/env python3

import multiprocessing
import socket

def handle(connection, address):
    import logging
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("process-%r" %(address,))
    try:
        logger.debug("Connected %r at %r", connection,address)
        while True:
            data = connection.recv(1024)
            if data == "":
                logger.debug("Socket closed remoteley")
                break
            logger.debug("Recieved data %r", data)
            connection.sendall(data)
            logger.debug("Sent Data")

    except:
        logger.exception("Problem handling request")
    finally:
        logger.debug("Closing Socket")
        connection.close()

class Server(object):
    def __init__(self, hostname, port):
        import logging
        self.logger = logging.getLogger("server")
        self.hostname = hostname
        self.port = port

    def start(self):
        self.logger.debug("Listening")
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        self.socket.bind((self.hostname, self.port))
        self.socket.listen(1)
        while True:
            conn, address = self.socket.accept()
            self.logger.debug("GOt Connection")
            process = multiprocessing.Process(target=handle, args=(conn,address))
            process.daemon = True
            process.start()
            self.logger.debug("Started process %r", process)

if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    server = Server("0.0.0.0", 9000)
    try:
        logging.info("Listening")
        server.start()
    except:
        logging.exception("Unexpected exception")
    finally:
        logging.info("Shutting Down!")
        for process in multiprocessing.active_children():
            logging.info("Sutting Down process %r",process)
            process.terminate()
            process.join()

    logging.info("All Done!")

