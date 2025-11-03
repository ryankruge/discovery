# Discovery (Network Device Discovery Tool)
Discovery is a Python-written host discovery tool that operates via the CLI.
## Features
- Passive host scan to avoid detection by network security systems.
- Aggressive host scan for swift, but noisy, device discovery.
- Host device identification using a JSON manufacturer database.
- Cross-platform support for Linux, Windows, and macOS.
# Installation
## Guide
1. If not already installed, install [PipX](https://pipx.pypa.io/stable/installation/).
2. In the root directory of the application, execute `pipx install .`
3. After the installation is complete, ensure that `~/.local/bin` is added to PATH. Simply append `export PATH=$PATH:~/.local/bin` to `~/.bashrc`.
## Requirements (Manual Installation Only)
- Scapy
- [Npcap](npcap.com/#download) (Windows)
# Application Usage
## General CLI Usage
This application operates by default in aggressive mode, therefore, passive scanning will need to manually enabled.
## CLI Flags
`-h` - Displays the help dialogue to reveal usable CLI flags.\
`-p` - Enables passive scan mode.\
`-d` - Specifies the time (in seconds) that the scan will be terminated in passive mode.
## Summary
This is a reconnaissance tool which, if used incorrectly, will be detected by networks with basic security measures in place. The use of this software should be kept within the bounds of local and federal laws and regulations. I will not accept responsibility for any repercussions incurred by such misuse.
