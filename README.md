# lambda-update-route53
This script convert all Ec2 machine to Route53 records. If you have a domain, all your Ec2 machines can be accesses by its name.

For instance, if you have the following machines (with Public IP enabled):
- machine number one
- machine number two
- this is another machine

And you have the domain example.org, all the machines will get the following names:

- machine-number-uno.example.org
- machine-number-two.example.org
- this-is-another-machine.example.org

In order for this to work you have to set the trigger (see the INSTALL.md)
