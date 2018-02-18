# ImundboQuant

OPEN-SOURCE PROJECT | Machine learning in Python and MQL4 for stock market and forex market predictions and fully automated trading.

*by Mikael Furesjö*

## Main project links
- [Get involved @Slack](https://imundboquant.slack.com)
- [Public Project page @Github](https://github.com/MikaelFuresjo/ImundboQuant)
- [Private repository @Dropbox](https://www.dropbox.com/sh/qemina178goedax/AABa0C0JmJpG4hIG8jLaaYaua?dl=0)

### More information
- Email: mailto:mikael[att]furesjo.se)
- Skype: mikaelfuresjo1
- [Homepage](http://www.beststrategies4trading.com/)
- [ZuluTrade Account)[https://www.zulutrade.com/trader/354968/trading]
- [Facebook group](https://www.facebook.com/groups/Borsrobotar/)
- [Youtube Channel](https://www.youtube.com/user/FuresjoFinancialTrad/videos)
- [Twitter](https://twitter.com/Mikael_Furesjo)


## Get all data
- USE DropBox link (above) to download Forex End-Of-Day (EOD) data.
- USE DropBox link (above) to download Forex End-Of-Day (EOD) data with preprocessed matrices in Excel to use with the CrossValidation.py script.

## Usage
- PreProcess.py creates our data matrix with 535 features and 8 targets values.
- CrossValidation.py cross validates the dataset for best possible feature combination.
- PickleProducer.py takes cross validated output and pickles predictions
- Forecaster.py uses pickles to create forecasts to use in MetaTrader 4 in live trading
