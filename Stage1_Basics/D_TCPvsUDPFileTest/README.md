## 📄 README.md

```markdown
# 📡 TCP vs UDP File Transfer Test

This project compares file transmission using **TCP** and **UDP** sockets in Python. It measures performance, correctness, and reliability of both protocols under identical file transfer conditions.

---

## 🎯 Project Objective

To implement two client-server applications that:

- Send and receive files using **TCP** (reliable) and **UDP** (unreliable)
- Measure **transfer time**, **file size**, and **file integrity (MD5 hash)**
- Detect and report packet loss or corruption in UDP
- Provide practical insight into transport-layer protocol behavior

---

## 🧰 Technologies

- Python 3.6+
- Standard libraries: `socket`, `time`, `hashlib`, `os`

No external dependencies required ✅

---

## 🗂️ Project Structure

```

D\_TCPvsUDPFileTest/
├── tcp\_server.py      # TCP file receiver
├── tcp\_client.py      # TCP file sender
├── udp\_server.py      # UDP file receiver
├── udp\_client.py      # UDP file sender
├── utils.py           # Shared utilities (hashing, timer)
└── test\_file.txt      # Sample file to transfer

````

---

## 🚀 How to Run

### 1. Prepare a test file

You can use any `.txt` file or generate one manually:

```bash
echo "this is a test line" > test_file.txt
````

---

### 2. Run TCP test

🖥️ Terminal 1 (TCP Server):

```bash
python tcp_server.py
```

📤 Terminal 2 (TCP Client):

```bash
python tcp_client.py
```

---

### 3. Run UDP test

🖥️ Terminal 1 (UDP Server):

```bash
python udp_server.py
```

📤 Terminal 2 (UDP Client):

```bash
python udp_client.py
```

---

## ✅ Sample Output

```
[ TCP ]
Transfer completed in 0.24s
Size: 102400 bytes
MD5: 38fdee1aa...

[ UDP ]
Transfer completed in 0.17s
Size: 100352 bytes
MD5: 7a9e5d12a...

Warning: file corrupted in UDP (MD5 mismatch)
```

---

## ⚖️ TCP vs UDP: Practical Comparison

| Feature         | TCP                     | UDP                          |
| --------------- | ----------------------- | ---------------------------- |
| Reliability     | Guaranteed (ACK)        | Not guaranteed (no ACK)      |
| Order           | Preserved               | May be out of order          |
| Speed           | Slower due to overhead  | Faster but lossy             |
| Use Cases       | Files, websites, emails | Streaming, games, VoIP       |
| Integrity Check | Built-in                | Must be implemented manually |

---

## 📌 Notes

* UDP transmission uses a custom end-of-transfer marker: `__END__`
* For high reliability, you can implement packet numbering + acknowledgments
* File integrity is verified using MD5 hash on both client and server sides
* To simulate packet loss, test on wireless or congested networks

---

