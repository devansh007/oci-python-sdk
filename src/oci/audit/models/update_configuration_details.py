# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConfigurationDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConfigurationDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param retention_period_days:
            The value to assign to the retention_period_days property of this UpdateConfigurationDetails.
        :type retention_period_days: int

        """
        self.swagger_types = {
            'retention_period_days': 'int'
        }

        self.attribute_map = {
            'retention_period_days': 'retentionPeriodDays'
        }

        self._retention_period_days = None

    @property
    def retention_period_days(self):
        """
        Gets the retention_period_days of this UpdateConfigurationDetails.
        The retention period days


        :return: The retention_period_days of this UpdateConfigurationDetails.
        :rtype: int
        """
        return self._retention_period_days

    @retention_period_days.setter
    def retention_period_days(self, retention_period_days):
        """
        Sets the retention_period_days of this UpdateConfigurationDetails.
        The retention period days


        :param retention_period_days: The retention_period_days of this UpdateConfigurationDetails.
        :type: int
        """
        self._retention_period_days = retention_period_days

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other