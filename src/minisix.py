###
# Copyright (c) 2014, Valentin Lorentz
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
###

"""Restricted equivalent to six."""

import sys

if sys.version_info[0] >= 3:
    PY2 = False
    PY3 = True
    intern = sys.intern
    integer_types = (int,)
    string_types = (str,)
    long = int

    import io
    import pickle
    import queue

    u = lambda x:x
else:
    PY2 = True
    PY3 = False
    if isinstance(__builtins__, dict):
        intern = __builtins__['intern']
    else:
        intern = __builtins__.intern
    integer_types = (int, long)
    string_types = (basestring,)
    long = long

    class io:
        # cStringIO is buggy with Python 2.6 (
        # see http://paste.progval.net/show/227/ )
        # and it does not handle unicode objects in Python  2.x
        from StringIO import StringIO
        from cStringIO import StringIO as BytesIO
    import cPickle as pickle
    import Queue as queue

    u = lambda x:x.decode('utf8')
