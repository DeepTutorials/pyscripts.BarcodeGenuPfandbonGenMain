from setuptools import setup, find_packages

setup(
    name='pyscripts.BarcodeGenuPfandbonGenMain',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'reportlab',
        'python-barcode',
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'generate_pfandbon=pyscripts.BarcodeGenuPfandbonGenMain:main',
        ],
    },
)
