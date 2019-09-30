from psutil import disk_usage, disk_partitions


class DiskManager:
    @property
    def partitions(self) -> list:
        return disk_partitions()

    def usage(self, partition: str='/'):
        return disk_usage(partition)
