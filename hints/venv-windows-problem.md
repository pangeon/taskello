# PowerShell says: “execution of scripts is disabled on this system.”

As an Administrator, you can set the execution policy by typing this into your PowerShell window:

```
Set-ExecutionPolicy RemoteSigned
```

For more information, see Using the Set-ExecutionPolicy Cmdlet.

When you are done, you can set the policy back to its default value with:

```
Set-ExecutionPolicy Restricted
```

You may see an error:

```
Access to the registry key
'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell' is denied.
To change the execution policy for the default (LocalMachine) scope,
  start Windows PowerShell with the "Run as administrator" option.
To change the execution policy for the current user,
  run "Set-ExecutionPolicy -Scope CurrentUser".
```

So you may need to run the command like this (as seen in comments):

```
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

LINK: [https://stackoverflow.com/questions/4037939/](https://stackoverflow.com/questions/4037939/powershell-says-execution-of-scripts-is-disabled-on-this-system)
