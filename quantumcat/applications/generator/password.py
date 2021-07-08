# (C) Copyright Artificial Brain 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import requests
from quantumcat.utils import constants, ErrorMessages
from quantumcat.exceptions import PasswordLengthError


class Password:
    def __init__(self, length):
        self.length = length

    def generate(self):
        if not (4 < self.length <= 20):
            raise PasswordLengthError(ErrorMessages.PASSWORD_LENGTH_INCORRECT)

        ANU_QRNG_REQUEST_URL = constants.ANU_QRNG_URL + '?length=1&type=' + \
                               constants.HEX_TYPE + '&size=' + str(self.length)
        response = requests.get(ANU_QRNG_REQUEST_URL)
        if response.status_code != 200:
            return 'Something went wromg'
        data = response.json()
        password = data['data'][0]
        return password[0: self.length]
