from threading import Thread, Timer


class ThreadUtil:

    @staticmethod
    def execute(function, *args, **kwargs):
        Thread(target=function, name="execute_thread",
               args=args, kwargs=kwargs).start()

    @staticmethod
    def timer(function, interval: int = 5, *args, **kwargs):
        Timer(interval=interval, function=function,
              args=args, kwargs=kwargs).start()
