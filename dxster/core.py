# -*- coding: utf-8 -*-
"""
  _____        _____ _
 |  __ \      / ____| |
 | |  | |_  __ (___ | |_ ___ _ __
 | |  | \ \/ /\___ \| __/ _ \ '__|
 | |__| |>  < ____) | |_  __/ |
 |_____//_/\_\_____/ \__\___|_|

Copyright 2016 Christopher P. Barnes <senrabc@gmail.com>
Copyright 2016 Kevin Hanson <kshanson@ufl.edu>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

"""

def get_hmm():
    """Get a thought."""
    return 'hmmm...'

def hmm():
    """Contemplation..."""
    print get_hmm()

# create a test calc function.
def calc_dxster(CDR_sb, NPDx):
    """
+--------+---------------------+---------------+-------------+-------------+----------------------+
| CDR_SB |    NPDX - NORMAL    | NPDX - PREMCI | NPDX - EMCI | NPDX - LMCI |   NPDX - DEMENTIA    |
+--------+---------------------+---------------+-------------+-------------+----------------------+
|        |                     |               |             |             |                      |
| 0      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
|        |                     |               |             |             |                      |
| 2      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
|        |                     |               |             |             |                      |
| 2.5    | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
|        |                     |               |             |             |                      |
| 4      | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
|        |                     |               |             |             |                      |
| >4.5   | Consesus Conference | Dementia      | Dementia    | Dementia    | Dementia             |
+--------+---------------------+---------------+-------------+-------------+----------------------+

    """

    # Initialize AlgDx empty to prevent wrong value returning.
    AlgDx = ''

    if (NPDx=='normal'):
        if (0 <= CDR_sb <= 2.0):
            AlgDx='Normal'
        elif (2.5 <= CDR_sb <= 4.0):
            AlgDx='PreMCI-CDR'
        elif (CDR_sb >= 4.5):
            AlgDx='Consensus Conference'
        else:
            AlgDx = 'ERROR normal' # need better error handling here for condition fallouts
    elif (NPDx=='premci'):
        if (0 <= CDR_sb <= 2.0):
            AlgDx='PreMCI - NP'
        elif (2.5 <= CDR_sb <= 4.0):
            AlgDx='PreMCI'
        elif (CDR_sb >= 4.5):
            AlgDx='Dementia'
        else:
            AlgDx = 'ERROR premci' # need better error handling here for condition fallouts
    elif (NPDx=='emci'):
        if (0 <= CDR_sb <= 2.0):
            AlgDx='eMCI - NP'
        elif (2.5 <= CDR_sb <= 4.0):
            AlgDx='eMCI'
        elif (CDR_sb >= 4.5):
            AlgDx='Dementia'
        else:
            AlgDx = 'ERROR emci' # need better error handling here for condition fallouts
    elif (NPDx=='lmci'):
        if (0 <= CDR_sb <= 2.0):
            AlgDx='LMCI - NP'
        elif (2.5 <= CDR_sb <= 4.0):
            AlgDx='LMCI'
        elif (CDR_sb >= 4.5):
            AlgDx='Dementia'
        else:
            AlgDx = 'ERROR lmci' # need better error handling here for condition fallouts
    elif (NPDx=='dementia'):
        if (0 <= CDR_sb <= 2.0):
            AlgDx='Consensus Conference'
        elif (2.5 <= CDR_sb <= 4.0):
            AlgDx='LMCI'
        elif (CDR_sb >= 4.5):
            AlgDx='Dementia'
        else:
            AlgDx = 'ERROR dementia' # need better error handling here for condition fallouts

    else:
        AlgDx = 'ERROR else:' + 'CDR_sb=' + str(CDR_sb), 'NPDX=' +  NPDx  # need better error handling here for condition fallouts

    return AlgDx
