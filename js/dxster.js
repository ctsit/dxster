// -*- coding: utf-8 -*-
// """
//   _____        _____ _
//  |  __ \      / ____| |
//  | |  | |_  __ (___ | |_ ___ _ __
//  | |  | \ \/ /\___ \| __/ _ \ '__|
//  | |__| |>  < ____) | |_  __/ |
//  |_____//_/\_\_____/ \__\___|_|
//
// Copyright 2016 Christopher P. Barnes <senrabc@gmail.com>
// Copyright 2016 Kevin Hanson <kshanson@ufl.edu>
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// # create a test calc function.
// def calc_dxster(CDR_sb, NPDx):
//     """
// +--------+---------------------+---------------+-------------+-------------+----------------------+
// | CDR_SB |    NPDX - NORMAL    | NPDX - PREMCI | NPDX - EMCI | NPDX - LMCI |   NPDX - DEMENTIA    |
// +--------+---------------------+---------------+-------------+-------------+----------------------+
// |        |                     |               |             |             |                      |
// | 0      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
// |        |                     |               |             |             |                      |
// | 2      | Normal              | PreMCI - NP   | eMCI - NP   | LMCI - NP   | Consensus Conference |
// |        |                     |               |             |             |                      |
// | 2.5    | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
// |        |                     |               |             |             |                      |
// | 4      | PreMCI - CDR        | PreMCI        | eMCI        | LMCI        | LMCI                 |
// |        |                     |               |             |             |                      |
// | >4.5   | Consesus Conference | Dementia      | Dementia    | Dementia    | Dementia             |
// +--------+---------------------+---------------+-------------+-------------+----------------------+
//
//     """

// JS fiddle : https://jsfiddle.net/senrabc/mr6nqgj8/
//
//

DxsterCalcModule = (function(){

  var calc_dxster = {};
  var AlgDx = '';


  calc_dxster.calculate = function(CDR_sb, NPDx){
    //console.log('in calculate function', a, b);
    //return a+b;

    switch (NPDx) {

      case "normal":
        console.log("In case: normal, calculating ...");

        if (CDR_sb >= 0 &&  CDR_sb <= 2.0){ AlgDx='Normal' };
        if (CDR_sb >= 2.5 &&  CDR_sb <= 4.0){ AlgDx='PreMCI-CDR' };
        if (CDR_sb >= 4.5) { AlgDx='Consensus Conference'};
        // need better error handling here for condition fallouts

        return AlgDx;
        break;
      case "premci":
        console.log("In case: premci, calculating ...");

        if (CDR_sb >= 0 &&  CDR_sb <= 2.0){ AlgDx='PreMCI - NP' };
        if (CDR_sb >= 2.5 &&  CDR_sb <= 4.0){ AlgDx='PreMCI' };
        if (CDR_sb >= 4.5){ AlgDx='Dementia'};
        // need better error handling here for condition fallouts

        return AlgDx;
        break;
      case "emci":
        console.log("In case: emci, calculating ...");

        if (CDR_sb >= 0 &&  CDR_sb <= 2.0){ AlgDx='eMCI - NP' };
        if (CDR_sb >= 2.5 &&  CDR_sb <= 4.0){ AlgDx='eMCI' };
        if (CDR_sb >= 4.5){ AlgDx='Dementia'};
        // need better error handling here for condition fallouts

        return AlgDx;
        break;
      case "lmci":
        console.log("In case: lmci, calculating ...");

        if (CDR_sb >= 0 &&  CDR_sb <= 2.0){ AlgDx='LMCI - NP' };
        if (CDR_sb >= 2.5 &&  CDR_sb <= 4.0){ AlgDx='LMCI' };
        if (CDR_sb >= 4.5){ AlgDx='Dementia'};
        // need better error handling here for condition fallouts


        return AlgDx;
        break;
      case "dementia":
        console.log("In case: dementia, calculating ...");

        if (CDR_sb >= 0 &&  CDR_sb <= 2.0){ AlgDx='Consensus Conference' };
        if (CDR_sb >= 2.5 &&  CDR_sb <= 4.0){ AlgDx='LMCI' };
        if (CDR_sb >= 4.5){ AlgDx='Dementia'};
        // need better error handling here for condition fallouts

        return AlgDx;
        break;

    }
  };

  return calc_dxster;

})();
