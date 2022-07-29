# Multi Threaded Python Network Calls

Scripts which enable users to run concurrent network & API calls. This is beneficial because concurrency enables devs to significantly reduce their scripts' execution times. 

## API Vs CLI

If the host you're connecting to provides an API and a CLI, you should always prefer the API. This is because:
1. It returns structured data. This means you won't have to manually parse outputs
2. It is consistent and versioned, therefore it will never break your script. On the other hand, CLI output formats can change over time
3. It has useful features built into it (e.g searching, pagination, etc). CLI parsing requires you to code these features yourself 

## Parsing CLI output

If CLI is your only option, you'll need to parse the output in order to extract the data you need. The easiest ways to do this are:
1. Set Netmiko's `use_textfsm` argument to `True`
2. Use the `textfsm` module directly

See [this post](https://pynet.twb-tech.com/blog/netmiko-and-textfsm.html) for more information.

# multimiko

The multimiko script can be found in the **"src"** directory of this repo. It uses [Netmiko](https://github.com/ktbyers/netmiko) and multithreading to connect to multiple network devices concurrently. Below is an example of its output.

Because the script was configured to use 3 threads, it completed its execution approximately 3 times faster than it would have without multithreading.

```
6 hosts provided. Logging into them in batches of 3
**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user

**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user
**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user


**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user

**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user

**************************************************
3.106.140.245 outputs
**************************************************
Command: ls -a
.  ..  .bash_history  .bash_logout  .bash_profile  .bashrc  .ssh

Command: pwd
/home/ec2-user

Command: whoami
ec2-user

**************************************************
Ran 18 commands across 6 hosts in 5 seconds
**************************************************
```

# Old school vs new style multithreading

The primary methods of multithreading are:
1. Using the `threading` module and `queue` modules
2. Using the `concurrent.futures` module

The latter provides a much simpler, higher level interface. That is to say, it requires much less code. This of course enables devs to write quicker and cleaner code.

## Examples

If you're interested in seeing the difference between these methods, I wrote [this post](https://oznetnerd.com/2020/06/28/multithreading-with-python-netmiko/) which breaks down a script I wrote using the "old school" method. And [this post](https://oznetnerd.com/2020/10/15/python-automating-network-health-checks/) is a breakdown of a script I wrote using the "new" style.