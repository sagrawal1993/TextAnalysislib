from distutils.core import setup
setup(
    name = "TextAnalysislib",
    packages = ["TextAnalysislib", "TextAnalysislib.TextEmbedding", "TextAnalysislib.ArticleSpinner", "TextAnalysislib.LanguageModel", "TextAnalysislib.TextProcessing", "TextAnalysislib.TextProcessing.English", "TextAnalysislib.TextSummarization", "TextAnalysislib.TopicExtraction", "TextAnalysislib.SimmilarTextRemover"],
    version = "0.0.2",
    description = "General function required for personal uses.",
    author = "Suraj Agrawal",
    author_email = "s.agrawal1993@gmail.com",
    url = "http://weekendtrip.co.in/",
    download_url = "",
    keywords = ["encoding", "i18n", "xml"],
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        ],
    long_description = """\
Universal character encoding detector
-------------------------------------

Detects
 - ASCII, UTF-8, UTF-16 (2 variants), UTF-32 (4 variants)
 - Big5, GB2312, EUC-TW, HZ-GB-2312, ISO-2022-CN (Traditional and Simplified Chinese)
 - EUC-JP, SHIFT_JIS, ISO-2022-JP (Japanese)
 - EUC-KR, ISO-2022-KR (Korean)
 - KOI8-R, MacCyrillic, IBM855, IBM866, ISO-8859-5, windows-1251 (Cyrillic)
 - ISO-8859-2, windows-1250 (Hungarian)
 - ISO-8859-5, windows-1251 (Bulgarian)
 - windows-1252 (English)
 - ISO-8859-7, windows-1253 (Greek)
 - ISO-8859-8, windows-1255 (Visual and Logical Hebrew)
 - TIS-620 (Thai)

This version requires Python 3 or later; a Python 2 version is available separately.
"""
)
