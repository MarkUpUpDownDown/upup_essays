from setuptools import setup, find_packages

from upup_essays import __version__

setup(
    name='upup_essays',
    version=__version__,
    url='http://github.com/MarkUpUpDownDown/upup_essays',
    description="UpUpEssays is an essay listing plugin for MarkUpUpDownDown",
    license='BSD',
    author='Jms Dnns',
    author_email='jdennis@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'markupupdowndown',
    ],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ]
)
