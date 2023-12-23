"""csv.sample_interface"""
#########################################################
# Builtin packages
#########################################################
import abc

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
# (None)


class RepoInterface(metaclass=abc.ABCMeta):
    """csv repository interface"""
    @abc.abstractmethod
    def all(self) -> list:
        """"all"""
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_id(self, id_: int):
        """find by id"""
        raise NotImplementedError()

    @abc.abstractmethod
    def add(self, data: dict):
        """add"""
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, data: dict):
        """update"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_by_id(self, id_: int):
        """delete by id"""
        raise NotImplementedError()

    @abc.abstractmethod
    def delete_all(self):
        """delete all"""
        raise NotImplementedError()
