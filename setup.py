#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'amazontranslate_plug = amazontranslate_neon_plugin:AmazonTranslator'

DETECT_PLUGIN_ENTRY_POINT = 'amazontranslate_detection_plug = amazontranslate_neon_plugin:AmazonDetector'

setup(
    name='amazontranslate_neon_plugin',
    version='0.0.1post1',
    description='',
    url='',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['amazontranslate_neon_plugin'],
    install_requires=["ovos-plugin-manager>=0.0.1a2",
                      "boto3"],
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
