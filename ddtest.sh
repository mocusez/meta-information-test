dd if=/dev/zero of=testfile bs=1G count=10 oflag=direct
dd if=testfile of=/dev/null bs=1G iflag=direct