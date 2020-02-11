from jetbot import Camera


class Observer:

    def __init__(self, camera_width, camera_height):
        self.camera = Camera(width=camera_width, height=camera_height)
        self.image = None

    def start(self):
        self.camera.observe(self._callback, names='value')
        self.camera.start()

    def stop(self):
        self.camera.stop()

    def _callback(self, change):
        #TODO change BGR2RGB
        self.image = change['new']

    def observation(self):
        while self.image is None:
            pass
        return self.image


