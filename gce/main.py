# Copyright 2019 Google LLC All Rights Reserved.
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

from flask import Flask, make_response, jsonify
import tensorflow as tf
import keras
import os
import time
import datetime
from tensorflow import keras
import random

from flask import Flask, jsonify

from datetime import datetime, date, time, timezone

app = Flask(__name__)


@app.route('/', methods=['GET'])
def say_hello():
    return "Hello, TEST/9/3/23/world!"

@app.route('/2', methods=['GET'])
def say_hello2():
    listv = []
    
    time1 = str(datetime.now())
    listv.append(time1)
    time.sleep(1)
    
    time2 = str(datetime.now())
    listv.append(time2)
    time.sleep(2.3)
    
    time3 = datetime.now()
    listv.append(time3)
    listV = jsonify(listv)
    
    
    return listV


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
