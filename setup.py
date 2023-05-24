from setuptools import setup

setup(
    name='sb3-envchecker-bug',
    python_requires='>=3.10',
    install_requires=[
        'stable-baselines3 == 2.0.0a5',
        'gymnasium == 0.28.1',
    ],
)
