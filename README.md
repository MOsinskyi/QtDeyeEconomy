# ⚡ QtDeyeEconomy

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.13.5-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/PySide6-6.9.1-green?style=for-the-badge&logo=qt&logoColor=white" alt="PySide6">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge" alt="Platform">
</div>

<div align="center">
  <h3>🔋 Smart Deye Inverter Monitoring & Economics Dashboard</h3>
  <p><em>Get the most important data from your Deye inverter and track electricity economics in one beautiful interface</em></p>
</div>

---

## 🌟 Features

### 📊 **Real-time Monitoring**
- Monitor your Deye inverter's most critical metrics
- Live data updates with intuitive visualizations
- Clean, responsive Qt-based interface

### 💰 **Electricity Economics**
- Track current electricity prices
- Monitor your energy costs and savings
- Economic analysis across different time periods

### 📈 **Multi-Period Analytics**
- **Daily**: Hour-by-hour performance tracking
- **Monthly**: Comprehensive monthly reports
- **Yearly**: Long-term trend analysis

### 🎯 **Key Metrics Dashboard**
- Power generation statistics
- Energy consumption patterns
- Cost-benefit analysis
- Performance optimization insights

---

## 🚀 Quick Start

### Prerequisites

- Python 3.13.5 or higher
- Deye inverter with network connectivity
- Windows, Linux, or macOS

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MOsinskyi/QtDeyeEconomy.git
   cd QtDeyeEconomy
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

### Configuration

1. Configure your Deye inverter connection settings
2. Set up your electricity pricing parameters
3. Customize monitoring intervals and alerts

---

## 🛠️ Tech Stack

<div align="center">
  <table>
    <tr>
      <td align="center"><strong>Framework</strong></td>
      <td align="center"><strong>Version</strong></td>
      <td align="center"><strong>Purpose</strong></td>
    </tr>
    <tr>
      <td>🐍 Python</td>
      <td>3.13.5</td>
      <td>Core application logic</td>
    </tr>
    <tr>
      <td>🖥️ PySide6</td>
      <td>6.9.1</td>
      <td>Modern GUI framework</td>
    </tr>
    <tr>
      <td>🌐 Requests</td>
      <td>Latest</td>
      <td>HTTP communication</td>
    </tr>
    <tr>
      <td>📄 JSON</td>
      <td>Built-in</td>
      <td>Data serialization</td>
    </tr>
    <tr>
      <td>📊 XLWings</td>
      <td>Latest</td>
      <td>Excel integration</td>
    </tr>
  </table>
</div>

---

## 🏗️ Architecture

This application is built using the **Model-View-Controller (MVC)** design pattern:

```
QtDeyeEconomy/
├── 📁 models/          # Data models and business logic
├── 📁 views/           # UI components and layouts
├── 📁 controllers/     # Application logic controllers
├── 📁 utils/           # Utility functions and helpers
├── 📁 config/          # Configuration files
└── 📄 main.py          # Application entry point
```

### Key Components

- **Model**: Handles data from Deye inverter and electricity pricing APIs
- **View**: PySide6-based GUI with responsive design
- **Controller**: Manages user interactions and data flow

---

## 📱 Screenshots

### 🌙 Dark
![img_1.png](img_1.png)

### ☀️ Light
![img_2.png](img_2.png)

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone your fork
git clone https://github.com/your-username/QtDeyeEconomy.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements-dev.txt

# Run tests
python -m pytest
```

---

## 🐛 Bug Reports & Feature Requests

Found a bug or have a great idea? We'd love to hear from you!

- 🐛 **Bug Reports**: [Create an issue](https://github.com/MOsinskyi/QtDeyeEconomy/issues/new?template=bug_report.md)
- 💡 **Feature Requests**: [Request a feature](https://github.com/MOsinskyi/QtDeyeEconomy/issues/new?template=feature_request.md)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Deye Technology** for their inverter API documentation
- **Qt Project** for the excellent PySide6 framework
- **Python Community** for the amazing ecosystem
- **Contributors** who help make this project better

---

<div align="center">
  <p>
    <strong>Made with ❤️ by <a href="https://github.com/MOsinskyi">MOsinskyi</a></strong>
  </p>
  <p>
    <a href="https://github.com/MOsinskyi/QtDeyeEconomy/stargazers">⭐ Star this project</a> if you find it useful!
  </p>
</div>

---

<div align="center">
  <sub>🔋 Empowering smart energy management, one inverter at a time</sub>
</div>