```
   _____        _____ _            
  |  __ \      / ____| |           
  | |  | |_  __ (___ | |_ ___ _ __
  | |  | \ \/ /\___ \| __/ _ \ '__|
  | |__| |>  < ____) | |_  __/ |   
  |_____//_/\_\_____/ \__\___|_|

```
# dxster

DxSter, the Alzheimer's Algorithmic Diagnostic Helper.

The DxSter module takes a Clincal  diagnosis (PhyDx) and the Neurophyscological diagnosis (NpDx) to output the algorithmic diagnosis (AlgDx). The idea is that the AlgDx saves time to formulate a diagnosis of an ALZ patient but reducing the need for consensus conferences.

#Support
This work has been supported by the Florida Department of Health's Ed and Ethel Moore Alzheimer's Disease Research Program grant number 66315-UF, the National Institute of Aging, and the 1Florida Alzheimer's Research Center grant number P50AG047266.

#Cite Us
Please reference Clinical and Translational Science - Informatics and Technology group (CTS-IT) in any research report, journal, or publication that requires citation of authors' work. Recognition of CTS-IT resources you used to perform research is important for acquiring funding for the next generation of informatics services and our research and development activities in software development and information science.

At minimum, a citation should include: Clinical and Translational Science Informatics and Technology group at the University of Florida

Our suggested acknowledgement is (select one or more items within the braces, as appropriate): The authors acknowledge the Clinical and Translational Science Informatics and Technology group at the University of Florida for providing {Python software library, code, examples, calculator} resources that have contributed to the research results reported within this paper. URL: http://www.ncbi.nlm.nih.gov/pubmed/20306566

#Examples

## Bash & Python with CSV test data set script example
In the examples/bash folder in the GitHub repository are example files of a sample csv dataset called sample_data.csv that contains a subject ID, NPDx, and CDR score. The file calc_algdx_sample.sh will call Python and the dxster python module to loop through every row in your sample data and output the AlgDx corresponding diagnosis to stdout.

## HTML & Javascript Implementation: DxSter Calculator
Go to DxCalc (https://cts-it.github.io/dxster/) and view page source to see an example implementation of the dxster.js JavaScript AlgDx Module. This module is a port of the Python library. It implements the identical AlgDx truth table and AlgDx calc functions. dxcalc.html serves as a reference implementation of this functionality.

#Literature cited.
Duara, R., Loewenstein, D. A., Greig, M., Acevedo, A., Potter, E., Appel, J., … Potter, H. (2010). Reliability and Validity of an Algorithm for the Diagnosis of Normal Cognition, MCI and Dementia: Implications for Multi-Center Research Studies. The American Journal of Geriatric Psychiatry : Official Journal of the American Association for Geriatric Psychiatry, 18(4), 363–370.http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2844658/
