import os, sys, platform
#optional: cpuinfo, psutil, GPUtil

if __name__ != "__main__": from .Track import Track as tk
else: from Track import Track as tk

class TrackSystem(tk):

    def basic_sysinfo(self) -> bool:
        try:
            info = {
                "system": platform.system(),
                "node": platform.node(),
                "release": platform.release(),
                "version": platform.version(),
                "machine": platform.machine(),
                "processor": platform.processor(),
                "python_version": platform.python_version()
            }
            for key, value in info.items(): self.write_record(self.basic_sysinfo.__name__, key, value)

            for key, value in dict(os.environ).items(): self.write_record(self.basic_sysinfo.__name__,"environment", key,value)

            return True
        except Exception as ex:
            self.write_record(self.basic_sysinfo.__name__, "[[ E R R O R ]]",ex)
            return False

    def hardware(self) -> bool:

        ran_without_errors = True

        try:
            import psutil
            info = {
            "cpu_info":psutil.cpu_times(),
            "memory_info":psutil.virtual_memory(),
            "disk_info":psutil.disk_partitions(),
            "network_info":psutil.net_if_addrs()
            }
            for key, value in info.items(): self.write_record(self.hardware.__name__,"psutil", key, value)
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(self.hardware.__name__, "psutil", "[[ E R R O R ]]",ex)

        try:
            import cpuinfo
            self.write_record(self.hardware.__name__, "cpuinfo", "cpu_details",cpuinfo.get_cpu_info())
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(self.hardware.__name__, "cpuinfo", "[[ E R R O R ]]",ex)

        try:
            import GPUtil
            gpus = GPUtil.getGPUs()
            gpu_info = [{gpu.id: gpu.name} for gpu in gpus]
            for key, value in gpu_info.items(): self.write_record(self.hardware.__name__,"GPUtil", key, value)
        except Exception as ex:
            ran_without_errors = False 
            self.write_record(self.hardware.__name__, "GPUtil", "[[ E R R O R ]]", ex)

        return ran_without_errors

    def networking(self) -> bool:
        ran_without_errors = True

        try:
            from scapy.all import *


            interfaces = get_if_list()
            for iface in interfaces:
                self.write_record(self.networking.__name__,"scapy",  "interface", get_if_addr(iface), get_if_hwaddr(iface), get_if_raw_hwaddr(iface))

            # Routing information
            routes = str(conf.route).split("\n")
            for route in routes:
                if route == []: continue
                self.write_record(self.networking.__name__,"scapy",  "route", route)


            arp_cache = str(ARP().cache).split("\n")
            for cache in arp_cache:
                if route == []: continue
                self.write_record(self.networking.__name__,"scapy",  "arp_cache", cache)


        except Exception as ex:
            self.write_record(self.networking.__name__, "scapy", "[[ E R R O R ]]", ex)
            ran_without_errors = False

        return ran_without_errors



#TrackSystem().basic_sysinfo()
#TrackSystem().hardware()
#TrackSystem().network()
