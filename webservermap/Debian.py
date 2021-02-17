from webservermap.OSScripts import OSScripts

class Debian(OSScripts):

    def get_update_os_script(self) -> str:

        returning_script = ""

        for single_line in self.get_update_os_script_lines():
            returning_script += single_line + "\n"
        returning_script = returning_script[:-1]
        
        return returning_script

    def get_update_os_script_lines(self) -> list:

        update_lines = []

        update_lines.append("apt-get -y update --fix-missing")
        update_lines.append("apt-get upgrade -y")
        update_lines.append("apt-get --no-install-recommends install -y apt-utils")
        update_lines.append("rm -rf /var/lib/apt/lists/*")
        
        return update_lines
