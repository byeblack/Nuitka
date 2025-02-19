#     Copyright 2024, Kay Hayen, mailto:kay.hayen@gmail.com find license text at end of file


from PyQt5 import QtGui

# nuitka-skip-unless-imports: PyQt5.QtGui

# nuitka-project: --mode=standalone
# nuitka-project: --enable-plugin=pyqt5
#
# nuitka-project-if: {OS} == "Darwin":
#   nuitka-project: --mode=app

print(QtGui.QImageReader.supportedImageFormats())

# nuitka-project: --enable-plugin=pyqt5

# nuitka-skip-unless-imports: PyQt5.QtGui

print(QtGui.QImageReader.supportedImageFormats())

#     Python test originally created or extracted from other peoples work. The
#     parts from me are licensed as below. It is at least Free Software where
#     it's copied from other people. In these cases, that will normally be
#     indicated.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
