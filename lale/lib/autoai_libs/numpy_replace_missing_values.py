# Copyright 2020 IBM Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import lale.docstrings
import lale.helpers
import lale.operators
import autoai_libs.transformers.exportable

class NumpyReplaceMissingValuesImpl():
    def __init__(self, missing_values, filling_values):
        self._hyperparams = {
            'missing_values': missing_values,
            'filling_values': filling_values}
        self._autoai_tfm = autoai_libs.transformers.exportable.NumpyReplaceMissingValues(**self._hyperparams)

    def fit(self, X, y=None):
        return self._autoai_tfm.fit(X, y)

    def transform(self, X):
        return self._autoai_tfm.transform(X)

_hyperparams_schema = {
    'allOf': [{
        'description': 'This first object lists all constructor arguments with their types, but omits constraints for conditional hyperparameters.',
        'type': 'object',
        'additionalProperties': False,
        'required': ['missing_values', 'filling_values'],
        'relevantToOptimizer': [],
        'properties': {
            'missing_values': {
                'description': 'List of values considered as "missing" for the array.',
                'anyOf': [
                {   'type': 'array',
                    'items': {'laleType': 'Any'}},
                {   'enum': [None]}],
                'default': None},
            'filling_values': {
                'description': 'Value to replace the missing values.',
                'laleType': 'Any',
                'default': None}}}]}

_input_fit_schema = {
    'type': 'object',
    'required': ['X'],
    'additionalProperties': False,
    'properties': {
        'X': {
            'type': 'array',
            'items': {'type': 'array', 'items': {'laleType': 'Any'}}},
        'y': {
            'laleType': 'Any'}}}

_input_transform_schema = {
    'type': 'object',
    'required': ['X'],
    'additionalProperties': False,
    'properties': {
        'X': {
            'type': 'array',
            'items': {'type': 'array', 'items': {'laleType': 'Any'}}}}}

_output_transform_schema = {
    'description': 'Features; the outer array is over samples.',
    'type': 'array',
    'items': {'type': 'array', 'items': {'laleType': 'Any'}}}

_combined_schemas = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': """Operator from `autoai_libs`_. Given a numpy array and a reference list of missing values for it, replaces missing values with a special value (typically a special missing value such as np.nan).

.. _`autoai_libs`: https://pypi.org/project/autoai-libs""",
    'documentation_url': 'https://lale.readthedocs.io/en/latest/modules/lale.lib.autoai.numpy_replace_missing_values.html',
    'type': 'object',
    'tags': {
        'pre': [],
        'op': ['transformer'],
        'post': []},
    'properties': {
        'hyperparams': _hyperparams_schema,
        'input_fit': _input_fit_schema,
        'input_transform': _input_transform_schema,
        'output_transform': _output_transform_schema}}

if (__name__ == '__main__'):
    lale.helpers.validate_is_schema(_combined_schemas)

lale.docstrings.set_docstrings(NumpyReplaceMissingValuesImpl, _combined_schemas)

NumpyReplaceMissingValues = lale.operators.make_operator(NumpyReplaceMissingValuesImpl, _combined_schemas)
