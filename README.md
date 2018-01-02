# CoinCheck
A simple Alexa skill that allows users to check the current prices of various cryptocurrencies ("coins").

## Usage
There are two steps to getting the skill "running": generating the information needed for Amazon's Apps & Services Developer Portal and generating the Amazon Lambda Function endpoint.

To get the Apps & Services Developer Portal information (which then needs to be pasted into the appropriate sections of the Portal), run the following command in the root directory:
```
python generate_amazon_info.py
```

To get the Lambda Function endpoint as a .zip archive (which then needs to be uploaded to the Amazon Lambda Management Console), run the following command in the root directory: 
```
python complete_function_package.py
```

The results of the setup commands will be found in the /output/ directory.