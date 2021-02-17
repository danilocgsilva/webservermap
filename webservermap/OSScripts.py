import abc

class OSScripts(abc.ABC):

    @abc.abstractclassmethod
    def get_update_os_script(self) -> str:
        pass

    @abc.abstractclassmethod
    def get_update_os_script_lines(self) -> list:
        pass
