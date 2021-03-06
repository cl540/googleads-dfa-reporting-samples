#!/usr/bin/python
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""This example creates a creative field value for a given creative field.

To get the creative field ID, run get_creative_fields.py.

Tags: creativeFieldValues.insert
"""

__author__ = ('api.jimper@gmail.com (Jonathon Imperiosi)')

import argparse
import sys

from apiclient import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'profile_id', type=int,
    help='The ID of the profile to add a creative field value for')
argparser.add_argument(
    'field_id', type=int,
    help='The ID of the creative field to add a value for')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  profile_id = flags.profile_id
  field_id = flags.field_id

  try:
    # Construct and save creative field value
    field_value = {
        'value': 'Test Creative Field Value'
    }

    request = service.creativeFieldValues().insert(
        profileId=profile_id, creativeFieldId=field_id, body=field_value)

    # Execute request and print response.
    response = request.execute()

    print ('Created creative field value with ID %s and value "%s".'
           % (response['id'], response['value']))

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main(sys.argv)
