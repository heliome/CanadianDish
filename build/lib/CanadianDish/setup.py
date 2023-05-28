from setuptools import setup, find_packages

setup(name='CanadianDish',
      version='0.1',
      description='CanadianDish',
      author='Hrytsiv Maksym',
      license='MIT',
      packages=find_packages(),
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
      ],
      install_requires=['reportlab']
)