# How to write universal script

CMD, Powershell and bash use different commands.
As there is usually bash installed on Windows and not vice versa, it's possible to use one script everywhere.

```bash
bash -c "echo 5 && echo 9"
```

## Multiline code

Not working on cmd

```bash
bash -c ("

echo 5 &&
echo 9 &&

echo 'Press key to exit' && read EXIT
")
```

# Bash

netstat -ap | grep http

# Powershell

## Simple script

```powershell
try {
    # something
} catch {
    $_
    Read-Host -Prompt "Error, Press Enter to exit"
}
    Read-Host -Prompt "Finished, Press Enter to exit"
```

## Exec powershell script

    ./script_name.ps1

## Answer Yes to all User inputs

    -Confirm:$false

# cmd - .bat

## Open bat and see result

    cmd /k my_script.bat