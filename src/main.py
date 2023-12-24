"""Entry point"""
#########################################################
# Builtin packages
#########################################################
# (None)

#########################################################
# 3rd party packages
#########################################################
# (None)

#########################################################
# Own packages
#########################################################
from common.log import initialize_logger
from controllers import SleepController
from controllers import DailySleepController


def main():
    """main"""
    initialize_logger()
    sc = SleepController()
    dsc = DailySleepController()

    # sc.add()
    dsc.add()


if __name__ == "__main__":
    main()
