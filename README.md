🐍 Python GUI Port Scanner 💻🔍
===============================

A simple, multi-threaded port scanner with a graphical user interface (GUI) built using Python and Tkinter. This tool allows you to scan a target IP address or domain for open TCP ports within a specified range.

⚠️ Disclaimer ⚠️
----------------

**This tool is intended for educational and professional purposes only.** Using this script for unauthorized scanning of networks is illegal. Ensure you have explicit, written permission from the network owner before scanning any system. The author is not responsible for any misuse or damage caused by this program.

✨ Features ✨
------------

-   **🎨 User-Friendly GUI:** A clean and simple interface built with Python's native Tkinter library.

-   **🌐 IP and Domain Support:** Scan either a direct IP address or a domain name (which will be resolved automatically).

-   **🎯 Custom Port Range:** Specify the exact range of ports you wish to scan (e.g., 1-1024).

-   **⚡ Multi-threaded Scanning:** Each port is scanned in a separate thread, which prevents the GUI from freezing during the scan and significantly speeds up the process.

-   **📈 Real-time Results:** Open ports are displayed in the results box as they are discovered.

🚀 How to Use 🚀
----------------

1.  **Prerequisites:** You need to have Python 3 installed on your system.

2.  **Download:** Clone this repository or download the `port_scanner_gui.py` script.

3.  **Run the script:** Open your terminal or command prompt, navigate to the directory containing the script, and run:

    ```
    python port_scanner_gui.py

    ```

4.  **Enter Scan Details:**

    -   In the "Target" field, enter the IP address or domain name (e.g., `192.168.1.1` or `example.com`).

    -   In the "Port Range" field, enter the range in the format `start-end` (e.g., `1-1024`).

5.  **Start Scan:** Click the "Start Scan" button to begin!

⚙️ How It Works ⚙️
------------------

This application combines three core Python concepts:

-   **🔌 Sockets (`socket` library):** This is the low-level networking library used to perform the actual connection attempts. For each port, the script creates a new TCP socket and tries to connect to the target. A successful connection (`connect_ex` returning `0`) indicates an open port.

-   **🖼️ GUI (`tkinter` library):** This is Python's standard library for creating graphical user interfaces. It is used to build the main window, input fields, buttons, and the scrollable text box for displaying results.

-   **🧵 Concurrency (`threading` library):** To avoid locking up the GUI while a potentially long scan is running, each port scan is launched in its own **thread**. This allows the main application to remain responsive and for many ports to be checked simultaneously, making the scan much faster than a sequential approach. The `daemon=True` setting ensures that these background threads are automatically closed when the main application exits.

🔮 Future Additions & Improvements 🔮
-------------------------------------

This is a foundational tool with a lot of potential for growth. Future enhancements planned include:

-   **💾 Save Results:** Implement functionality to save the scan results to a file (e.g., `.txt` or `.csv`).

-    **📦 UDP Scanning:** Add an option to perform UDP scans, which is more complex as UDP is a connectionless protocol.

-    **🕵️ Service & Version Detection:** Attempt "banner grabbing" on open ports to identify the service (e.g., HTTP, FTP) and its version number running on that port.

-   **📊 GUI Progress Bar:** Add a progress bar to provide a visual indication of how much of the scan is complete.

-   **⭐ Common Ports Option:** Add a button to automatically scan a list of the most commonly used ports.

-   [ ] **⏱️ Adjustable Timeout:** Allow the user to set the connection timeout value from the GUI.

📜 License 📜
-------------

This project is licensed under the MIT License. See the `LICENSE` file for details.