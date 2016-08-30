# coding: utf-8

"""
    Resource provisioner API

    Provision Cloud Computing resources via API.

    OpenAPI spec version: 0.1.11
    
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


class User(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id=None, username=None, first_name=None, last_name=None, email=None, credentials=None, clusters=None, is_staff=None, is_superuser=None, is_active=None, date_joined=None):
        """
        User - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'id': 'int',
            'username': 'str',
            'first_name': 'str',
            'last_name': 'str',
            'email': 'str',
            'credentials': 'list[int]',
            'clusters': 'list[int]',
            'is_staff': 'int',
            'is_superuser': 'int',
            'is_active': 'int',
            'date_joined': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'credentials': 'credentials',
            'clusters': 'clusters',
            'is_staff': 'is_staff',
            'is_superuser': 'is_superuser',
            'is_active': 'is_active',
            'date_joined': 'date_joined'
        }

        self._id = id
        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._credentials = credentials
        self._clusters = clusters
        self._is_staff = is_staff
        self._is_superuser = is_superuser
        self._is_active = is_active
        self._date_joined = date_joined

    @property
    def id(self):
        """
        Gets the id of this User.
        Unique identifier representing a specific user

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this User.
        Unique identifier representing a specific user

        :param id: The id of this User.
        :type: int
        """

        self._id = id

    @property
    def username(self):
        """
        Gets the username of this User.
        Name given to the user

        :return: The username of this User.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this User.
        Name given to the user

        :param username: The username of this User.
        :type: str
        """

        self._username = username

    @property
    def first_name(self):
        """
        Gets the first_name of this User.
        First name of the user

        :return: The first_name of this User.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """
        Sets the first_name of this User.
        First name of the user

        :param first_name: The first_name of this User.
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """
        Gets the last_name of this User.
        Last name of the user

        :return: The last_name of this User.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """
        Sets the last_name of this User.
        Last name of the user

        :param last_name: The last_name of this User.
        :type: str
        """

        self._last_name = last_name

    @property
    def email(self):
        """
        Gets the email of this User.
        Email of the user

        :return: The email of this User.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """
        Sets the email of this User.
        Email of the user

        :param email: The email of this User.
        :type: str
        """

        self._email = email

    @property
    def credentials(self):
        """
        Gets the credentials of this User.
        Array of the credentials IDs of the user

        :return: The credentials of this User.
        :rtype: list[int]
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this User.
        Array of the credentials IDs of the user

        :param credentials: The credentials of this User.
        :type: list[int]
        """

        self._credentials = credentials

    @property
    def clusters(self):
        """
        Gets the clusters of this User.
        Array of the clusters IDs of the user

        :return: The clusters of this User.
        :rtype: list[int]
        """
        return self._clusters

    @clusters.setter
    def clusters(self, clusters):
        """
        Sets the clusters of this User.
        Array of the clusters IDs of the user

        :param clusters: The clusters of this User.
        :type: list[int]
        """

        self._clusters = clusters

    @property
    def is_staff(self):
        """
        Gets the is_staff of this User.
        Boolean stating wether the user is a staff member or not

        :return: The is_staff of this User.
        :rtype: int
        """
        return self._is_staff

    @is_staff.setter
    def is_staff(self, is_staff):
        """
        Sets the is_staff of this User.
        Boolean stating wether the user is a staff member or not

        :param is_staff: The is_staff of this User.
        :type: int
        """

        self._is_staff = is_staff

    @property
    def is_superuser(self):
        """
        Gets the is_superuser of this User.
        Boolean stating wether the user is a superuser or not

        :return: The is_superuser of this User.
        :rtype: int
        """
        return self._is_superuser

    @is_superuser.setter
    def is_superuser(self, is_superuser):
        """
        Sets the is_superuser of this User.
        Boolean stating wether the user is a superuser or not

        :param is_superuser: The is_superuser of this User.
        :type: int
        """

        self._is_superuser = is_superuser

    @property
    def is_active(self):
        """
        Gets the is_active of this User.
        Boolean stating wether the user is active or not

        :return: The is_active of this User.
        :rtype: int
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """
        Sets the is_active of this User.
        Boolean stating wether the user is active or not

        :param is_active: The is_active of this User.
        :type: int
        """

        self._is_active = is_active

    @property
    def date_joined(self):
        """
        Gets the date_joined of this User.
        Date and time of creation of the user

        :return: The date_joined of this User.
        :rtype: datetime
        """
        return self._date_joined

    @date_joined.setter
    def date_joined(self, date_joined):
        """
        Sets the date_joined of this User.
        Date and time of creation of the user

        :param date_joined: The date_joined of this User.
        :type: datetime
        """

        self._date_joined = date_joined

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
