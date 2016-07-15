# coding: utf-8

"""
    Process Registry API

    Register processes with the Process Registry API.

    OpenAPI spec version: 0.1.5
    
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


class ProcessImpl(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        ProcessImpl - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'name': 'str',
            'appliance': 'str',
            'process_definition': 'int',
            'archive_url': 'str',
            'executable': 'str',
            'cwd': 'str',
            'environment': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'appliance': 'appliance',
            'process_definition': 'process_definition',
            'archive_url': 'archive_url',
            'executable': 'executable',
            'cwd': 'cwd',
            'environment': 'environment'
        }

        self._id = None
        self._name = None
        self._appliance = None
        self._process_definition = None
        self._archive_url = None
        self._executable = None
        self._cwd = None
        self._environment = None

    @property
    def id(self):
        """
        Gets the id of this ProcessImpl.
        Unique ID of the process implementation

        :return: The id of this ProcessImpl.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ProcessImpl.
        Unique ID of the process implementation

        :param id: The id of this ProcessImpl.
        :type: int
        """
        
        self._id = id

    @property
    def name(self):
        """
        Gets the name of this ProcessImpl.
        Name given to the process implementation

        :return: The name of this ProcessImpl.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProcessImpl.
        Name given to the process implementation

        :param name: The name of this ProcessImpl.
        :type: str
        """
        
        self._name = name

    @property
    def appliance(self):
        """
        Gets the appliance of this ProcessImpl.
        Name of the appliance on which the process implementation must be run

        :return: The appliance of this ProcessImpl.
        :rtype: str
        """
        return self._appliance

    @appliance.setter
    def appliance(self, appliance):
        """
        Sets the appliance of this ProcessImpl.
        Name of the appliance on which the process implementation must be run

        :param appliance: The appliance of this ProcessImpl.
        :type: str
        """
        
        self._appliance = appliance

    @property
    def process_definition(self):
        """
        Gets the process_definition of this ProcessImpl.
        Id of the process definition linked with this new implementation

        :return: The process_definition of this ProcessImpl.
        :rtype: int
        """
        return self._process_definition

    @process_definition.setter
    def process_definition(self, process_definition):
        """
        Sets the process_definition of this ProcessImpl.
        Id of the process definition linked with this new implementation

        :param process_definition: The process_definition of this ProcessImpl.
        :type: int
        """
        
        self._process_definition = process_definition

    @property
    def archive_url(self):
        """
        Gets the archive_url of this ProcessImpl.
        URL of the archive to download and extract on the worker before starting the job

        :return: The archive_url of this ProcessImpl.
        :rtype: str
        """
        return self._archive_url

    @archive_url.setter
    def archive_url(self, archive_url):
        """
        Sets the archive_url of this ProcessImpl.
        URL of the archive to download and extract on the worker before starting the job

        :param archive_url: The archive_url of this ProcessImpl.
        :type: str
        """
        
        self._archive_url = archive_url

    @property
    def executable(self):
        """
        Gets the executable of this ProcessImpl.
        Path to the executable

        :return: The executable of this ProcessImpl.
        :rtype: str
        """
        return self._executable

    @executable.setter
    def executable(self, executable):
        """
        Sets the executable of this ProcessImpl.
        Path to the executable

        :param executable: The executable of this ProcessImpl.
        :type: str
        """
        
        self._executable = executable

    @property
    def cwd(self):
        """
        Gets the cwd of this ProcessImpl.
        Working directory to be in when ruing the process implementation

        :return: The cwd of this ProcessImpl.
        :rtype: str
        """
        return self._cwd

    @cwd.setter
    def cwd(self, cwd):
        """
        Sets the cwd of this ProcessImpl.
        Working directory to be in when ruing the process implementation

        :param cwd: The cwd of this ProcessImpl.
        :type: str
        """
        
        self._cwd = cwd

    @property
    def environment(self):
        """
        Gets the environment of this ProcessImpl.
        JSON-formatted dictonary to give values to environment variables (can contain parameters)

        :return: The environment of this ProcessImpl.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """
        Sets the environment of this ProcessImpl.
        JSON-formatted dictonary to give values to environment variables (can contain parameters)

        :param environment: The environment of this ProcessImpl.
        :type: str
        """
        
        self._environment = environment

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

