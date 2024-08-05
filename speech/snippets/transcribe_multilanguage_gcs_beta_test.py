# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.api_core.retry import Retry

import pytest

import transcribe_multilanguage_gcs_beta


@Retry()
def test_transcribe_file_with_multilanguage_gcs(capsys: pytest.CaptureFixture) -> None:
    audio = "gs://cloud-samples-data/speech/multi_es.flac"
    response = transcribe_multilanguage_gcs_beta.transcribe_file_with_multilanguage_gcs(
        audio
    )
    out, err = capsys.readouterr()

    assert response is not None
    assert "estoy" in out
    assert "First alternative" in out
