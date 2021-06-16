# arta_corpus
This repository contains a Japanese corpus used in the following paper:  
Shohei Tanaka, Koichiro Yoshino, Katsuhito Sudoh, Satoshi Nakamura. ``ARTA: Collection and Classification of Ambiguous Requests and Thoughtful Actions'', The 22nd Annual Meeting of the Special Interest Group on Discourse and Dialogue (SIGDIAL), July, 2021, Singapore  
<!-- https://www.aclweb.org/anthology/W19-4106/ -->

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

## Citation
<!-- Please cite the following paper when you use the corpus. -->
TBA

<!-- ```
@inproceedings{tanaka-etal-2019-conversational,
    title = "Conversational Response Re-ranking Based on Event Causality and Role Factored Tensor Event Embedding",
    author = "Tanaka, Shohei  and
      Yoshino, Koichiro  and
      Sudoh, Katsuhito  and
      Nakamura, Satoshi",
    booktitle = "Proceedings of the First Workshop on NLP for Conversational AI",
    month = aug,
    year = "2019",
    address = "Florence, Italy",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W19-4106",
    doi = "10.18653/v1/W19-4106",
    pages = "51--59",
    abstract = "We propose a novel method for selecting coherent and diverse responses for a given dialogue context. The proposed method re-ranks response candidates generated from conversational models by using event causality relations between events in a dialogue history and response candidates (e.g., {``}be stressed out{''} precedes {``}relieve stress{''}). We use distributed event representation based on the Role Factored Tensor Model for a robust matching of event causality relations due to limited event causality knowledge of the system. Experimental results showed that the proposed method improved coherency and dialogue continuity of system responses.",
}
``` -->
