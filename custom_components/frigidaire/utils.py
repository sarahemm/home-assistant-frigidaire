import threading


def debounce(wait_time_seconds):
    """
    Decorator that will debounce a function so that it is called after wait_time_seconds seconds
    If it is called multiple times, will wait for the last call to be debounced and run only this one.
    """

    def decorator(function):
        def debounced(*args, **kwargs):
            def call_function():
                debounced._timer = None
                return function(*args, **kwargs)

            # if we already have a call to the function currently waiting to be executed, reset the timer
            if debounced.timer is not None:
                debounced.timer.cancel()

            # after wait_time, call the function provided to the decorator with its arguments
            debounced.timer = threading.Timer(wait_time_seconds, call_function)
            debounced.timer.start()

        debounced._timer = None
        return debounced

    return decorator
