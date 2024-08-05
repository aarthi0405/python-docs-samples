# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re

from google.api_core.retry import Retry
import pytest

import transcribe_gcs_v2

_TEST_AUDIO_FILE_PATH = "gs://cloud-samples-data/speech/audio.flac"


@Retry()
def test_transcribe_gcs_v2(capsys: pytest.CaptureFixture) -> None:

    response = transcribe_gcs_v2.transcribe_gcs_v2(_TEST_AUDIO_FILE_PATH)

    assert re.search(
        r"how old is the Brooklyn Bridge",
        response.results[0].alternatives[0].transcript,
        re.DOTALL | re.I,
    )
