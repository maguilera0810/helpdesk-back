# .\resources\helpers\file_helper.py
class FileHelper:
    """
    File helper, class to check some attributes of a file.
    """

    def __init__(self, file=None):
        self.file = file

    def is_mp3(self, file=None):
        return self.check_format("mp3", file)

    def is_wav(self, file=None):
        return self.check_format("wav", file)

    def is_mp4(self, file=None):
        return self.check_format("mp4", file)

    def is_srt(self, file=None):
        return self.check_format("srt", file)

    def is_png(self, file=None):
        return self.check_format("png", file)

    def is_jpg(self, file=None):
        return self.check_format("jpg", file)

    def is_json(self, file=None):
        return self.check_format("json", file)

    def get_format(self, file=None):
        file = file or self.file
        return file.name.lower().split(".")[-1]

    def check_format(self, format: str, file=None):
        file = file or self.file
        return file.name.lower().endswith(f".{format}")

    def check_formats(self, formats: list[str]):
        return any(map(self.check_format, formats))
