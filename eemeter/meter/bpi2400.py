from eemeter.meter import MeterBase
from eemeter.config.yaml_parser import load

class BPI2400Meter(MeterBase):
    """Implementation of BPI-2400 standard
    """

    def __init__(self,**kwargs):
        super(self.__class__, self).__init__(**kwargs)
        self.meter = load(self._meter_yaml())

    def _meter_yaml(self):
        meter_yaml = """
            !obj:eemeter.meter.SequentialMeter {
                sequence: [
                    !obj:eemeter.meter.RecentReadingMeter {
                        n_days: 360
                    },
                    !obj:eemeter.meter.EstimatedReadingConsolidationMeter {
                    },
                    !obj:eemeter.meter.AndMeter {
                        inputs: [
                            recent_reading,
                        ]
                    }
                ]
            }
            """
        return meter_yaml

    def evaluate_mapped_inputs(self,**kwargs):
        return self.meter.evaluate(**kwargs)

    def _get_child_inputs(self):
        return self.meter.get_inputs()
