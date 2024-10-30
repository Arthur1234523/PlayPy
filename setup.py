from setuptools import setup, find_packages

setup(
    name='PlayPy',
    version='0.1',
    description='A simple library for audio and video playback in Python',
    author='Arthur', 
    author_email='arthur.greghi2105@gmail.com',  
    packages=find_packages(),  
    install_requires=[
        'pygame',  # Dependency for audio playback
        'opencv-python'  # Dependency for video playback
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',  # Replace with the license you choose
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the required Python version
)
