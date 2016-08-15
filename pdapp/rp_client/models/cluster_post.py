# coding: utf-8

"""
    Resource provisioner API

    Provision Cloud Computing resources via API.

    OpenAPI spec version: 0.1.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class ClusterPost(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, user_id=None, appliance=None):
        """
        ClusterPost - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'name': 'str',
            'user_id': 'int',
            'appliance': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'user_id': 'user_id',
            'appliance': 'appliance'
        }

        self._name = name
        self._user_id = user_id
        self._appliance = appliance

    @property
    def name(self):
        """
        Gets the name of this ClusterPost.
        Name given to the cluster

        :return: The name of this ClusterPost.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ClusterPost.
        Name given to the cluster

        :param name: The name of this ClusterPost.
        :type: str
        """

        self._name = name

    @property
    def user_id(self):
        """
        Gets the user_id of this ClusterPost.
        ID of the user that create the cluster

        :return: The user_id of this ClusterPost.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ClusterPost.
        ID of the user that create the cluster

        :param user_id: The user_id of this ClusterPost.
        :type: int
        """

        self._user_id = user_id

    @property
    def appliance(self):
        """
        Gets the appliance of this ClusterPost.
        Appliance of the cluster

        :return: The appliance of this ClusterPost.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this ClusterPost.
        Appliance of the cluster

        :param appliance: The appliance of this ClusterPost.
        :type: str
        """

        self._appliance = appliance

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
