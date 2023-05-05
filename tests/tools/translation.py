# coding=utf-8
# Copyright 2023 HuggingFace Inc.
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

from transformers.tools import TranslationTool

from .test_tools_common import ToolTesterMixin
import unittest


class TranslationToolTester(unittest.TestCase, ToolTesterMixin):
    def setUp(self):
        self.tool = TranslationTool()
        self.tool.setup()

    def test_exact_match_arg(self):
        result = self.tool("Hey, what's up?", src_lang='English', tgt_lang='French')
        self.assertEqual(result, '- Hé, comment ça va?')

    def test_exact_match_kwarg(self):
        result = self.tool(text="Hey, what's up?", src_lang='English', tgt_lang='French')
        self.assertEqual(result, '- Hé, comment ça va?')