#!/usr/bin/env python3
from setuptools import setup
from os import getenv, path

PLUGIN_ENTRY_POINT = 'amazontranslate_plug = amazontranslate_neon_plugin:AmazonTranslatePlugin'
DETECT_PLUGIN_ENTRY_POINT = 'amazontranslate_detection_plug = amazontranslate_neon_plugin:AmazonTranslateDetectPlugin'


def get_requirements(requirements_filename: str):
    requirements_file = path.join(path.abspath(path.dirname(__file__)), "requirements", requirements_filename)
    with open(requirements_file, 'r', encoding='utf-8') as r:
        requirements = r.readlines()
    requirements = [r.strip() for r in requirements if r.strip() and not r.strip().startswith("#")]

    for i in range(0, len(requirements)):
        r = requirements[i]
        if "@" in r:
            parts = [p.lower() if p.strip().startswith("git+http") else p for p in r.split('@')]
            r = "@".join(parts)
        if getenv("GITHUB_TOKEN"):
            if "github.com" in r:
                requirements[i] = r.replace("github.com", f"{getenv('GITHUB_TOKEN')}@github.com")
    return requirements


with open("README.md", "r") as f:
    long_description = f.read()

with open("./version.py", "r", encoding="utf-8") as v:
    for line in v.readlines():
        if line.startswith("__version__"):
            if '"' in line:
                version = line.split('"')[1]
            else:
                version = line.split("'")[1]


setup(
    name='neon-lang-plugin-amazon-translate',
    version=version,
    description='Amazon Translate Language Plugin',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/NeonGeckoCom/neon-lang-plugin-amazon_translate',
    author='Neongecko',
    author_email='developers@neon.ai',
    license='BSD-3-Clause',
    packages=['neon_lang_plugin_amazon_translate'],
    install_requires=get_requirements("requirements.txt"),
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='neon mycroft plugin language detection translation',
    entry_points={
        'neon.plugin.lang.translate': PLUGIN_ENTRY_POINT,
        'neon.plugin.lang.detect': DETECT_PLUGIN_ENTRY_POINT
    }
)
