import os, sys

from scapy.all import *
import psutil, cpuinfo, GPUtil


if __name__ != "__main__": from .Track import Track as tk
else: from Track import Track as tk

class TrackSystem(tk):

    def basic_sysinfo(self) -> bool:
        funct = self.basic_sysinfo.__name__
        try:
            import platform
            # For some mysterious reason if imported from the module level it errors out on Ubuntu, but works great on MacOS & Windows ????
            info = {
                "system": platform.system(),
                "node": platform.node(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "python_version": platform.python_version()
            }
            for key, value in info.items(): self.write_record(funct, key, value)

            for key, value in dict(os.environ).items(): self.write_record(funct,"environment", key,value)

            return True
        except Exception as ex:
            self.write_record(self.basic_sysinfo.__name__, "[[ E R R O R ]]",ex)
            return False

    def hardware(self) -> bool:

        ran_without_errors = True
        funct = self.hardware.__name__

        try:
            info = {
            "cpu_info":psutil.cpu_times(),
            "memory_info":psutil.virtual_memory(),
            "disk_info":psutil.disk_partitions(),
            "network_info":psutil.net_if_addrs()
            }
            for key, value in info.items(): self.write_record(funct,"psutil", key, value)
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(funct, "psutil", "[[ E R R O R ]]",ex)

        try:
            for key, value in cpuinfo.get_cpu_info():
                self.write_record(funct, "cpuinfo", "cpu_details",key, value)
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(funct, "cpuinfo", "[[ E R R O R ]]",ex)

        try:
            gpus = GPUtil.getGPUs()
            gpu_info = [{gpu.id: gpu.name} for gpu in gpus]
            for key, value in gpu_info.items(): self.write_record(funct,"GPUtil", key, value)
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(funct, "GPUtil", "[[ E R R O R ]]", ex)

        return ran_without_errors

    def network(self) -> bool:
        funct = self.network.__name__

        try:
            interfaces = get_if_list()
            for iface in interfaces:
                self.write_record(funct,"scapy",  "interface", get_if_addr(iface), get_if_hwaddr(iface), get_if_raw_hwaddr(iface))

            # Routing information
            routes = str(conf.route).split("\n")
            for route in routes:
                if route == []: continue
                self.write_record(funct,"scapy",  "route", route)

            return True
        except Exception as ex:
            self.write_record(funct, "scapy", "[[ E R R O R ]]", ex)
            return False


"""
ts = TrackSystem()
ts.basic_sysinfo()
ts.hardware()
ts.network()
"""
