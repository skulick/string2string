from setuptools import find_packages, setup

setup(
    name="string2string",
    version="0.0.145",
    description="String-to-String Algorithms for Natural Language Processing",
    url="https://github.com/suzgunmirac/string2string",
    author="Mirac Suzgun",
    author_email="msuzgun@cs.stanford.edu",
    license="MIT",
    python_requires='>=3.7',
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "transformers",
        "datasets",
        "faiss-cpu==1.7.3",
        "bert_score",
        "fasttext",
        "pandas",
    ],
    tests_require=["pytest"],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
    keywords=[
        "string matching",
        "pattern matching",
        "edit distance",
        "string to string correction",
        "string to string matching",
        "Levenshtein edit distance",
        "Hamming distance",
        "Damerau-Levenshtein distance",
        "Jaro-Winkler distance",
        "longest common subsequence",
        "longest common substring",
        "dynamic programming",
        "approximate string matching",
    ],
)