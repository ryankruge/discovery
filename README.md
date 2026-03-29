# Discovery (Network Device Discovery Tool)
Discovery is a Python-written command-line tool that enables host discovery.
## Features
- Passive host scanning to avoid detection by network security systems.
- Aggressive host scanning for swift—but noisy—device discovery.
- Host device identification using a JSON manufacturer database.
- Cross-platform support for Linux, Windows, and macOS.
# Installation
## Guide
1. If not already installed, install [PipX](https://pipx.pypa.io/stable/installation/).
2. In the installation directory of Discovery, execute `pipx install .`
3. After the installation is complete, ensure that `~/.local/bin` is added to PATH. On Linux, append `export PATH=$PATH:~/.local/bin` to `~/.bashrc`. For Windows, `setx PATH "%PATH%;PATH_TO_BINARIES"`.
## Requirements (Manual Installation Only)
- Scapy Library
- [Npcap](npcap.com/#download) (*Windows*)
# Application Usage
## Standard Behaviour
By default, Discovery operates in aggressive scanning mode which is noisy and can lead to a response from an *Intrusion Detection System* (IDS). Passive mode is completely undetectable but is not as effective as aggressive mode and may require a high scan time depending on the activity of devices.
## CLI Flags
`-h` - Displays the help dialogue to reveal usable CLI flags.\
`-p` - Enables passive scanning mode.\
`-d` - Scan duration for passive scanning mode in seconds (default is 30 seconds).
## Legal Disclaimer
The use of this software should be kept within the bounds of local and federal laws and regulations. I will not accept responsibility for any repercussions incurred by unintended misuse of this software.
