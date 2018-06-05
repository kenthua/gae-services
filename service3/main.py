# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import urllib2
import os
import logging

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info('INFO: service3')
        logging.debug('DEBUG: service3')
        logging.warning('WARNING: service3')

        res1 = urllib2.urlopen('https://' + os.environ['SERVICE1'] + '-dot-' + os.environ['DEFAULT_VERSION_HOSTNAME'] + '/' + os.environ['SERVICE1'])
        html1 = res1.read()
        res2 = urllib2.urlopen('https://' + os.environ['SERVICE2'] + '-dot-' + os.environ['DEFAULT_VERSION_HOSTNAME'] + '/' + os.environ['SERVICE2'])
        html2 = res2.read()
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World! - service3')
        self.response.write('\n')
        self.response.write(html1)
        self.response.write('\n')
        self.response.write(html2)
        self.response.write('\n')
        self.response.write('service3 environment variables')
        self.response.write(os.environ)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
