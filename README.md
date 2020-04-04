# costco_monitoring
How to use:
1.	Got to https://sameday.costco.com/ to add anything you want into shopping cart
2.	Run the script monitoring_shopping_cart.py, when there is delivery times available, the script will send SMS message to your phone.

Chrome extension https://chrome.google.com/webstore/detail/distill-web-monitor/inlikjemeeknofckkjolnjbpehgadgge?hl=en has similar function, please use Chrome extension Distill Web Monitor if you feel it is too many technical settings.

#Setting up
1.Download webdriver.Chrome

2.Install osx

3.run the following cmds
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
```