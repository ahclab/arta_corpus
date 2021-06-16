# arta_corpus
This repository contains a Japanese corpus used in the following paper:  
Shohei Tanaka, Koichiro Yoshino, Katsuhito Sudoh, Satoshi Nakamura. ``ARTA: Collection and Classification of Ambiguous Requests and Thoughtful Actions'', The 22nd Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL), July, 2021, Singapore  
<!-- https://www.aclweb.org/anthology/W19-4106/ -->
https://arxiv.org/abs/2106.07999


## Data Format
The corpus containing 27,230 user requests has been split into train.json:valid.json:test.json = 24,430:1,400:1,400.
You can refer to load_data.py for data loading.
Each line is a json format dictionary contains following keys.

- **idx**: unique data idx
- **utterance**: user utterance (request)
- **response**: system response (action)
- **function**: system action function
- **category**: system action category
- **multilabel**: additional system action categories (only the test data and a part of valid data contains this key.)

## License
ARTA Corpus (c) by Shohei Tanaka, Koichiro Yoshino, Katsuhito Sudoh, Satoshi Nakamura  
Copyright (c) 2021- Augmented Human Communication Laboratory, Nara Institute of Science and Technology

ARTA Corpus is licensed under a  
[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

<!-- You should have received a copy of the license along with this work.  
If not, see <https://creativecommons.org/licenses/by/4.0/legalcode>   -->

## Citation
Please cite the following paper when you use the corpus.

``` text
@misc{tanaka2021arta,
      title={ARTA: Collection and Classification of Ambiguous Requests and Thoughtful Actions}, 
      author={Shohei Tanaka and Koichiro Yoshino and Katsuhito Sudoh and Satoshi Nakamura},
      year={2021},
      eprint={2106.07999},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
