# 🏎️ F1 Race Strategy Dashboard

An interactive web dashboard analyzing Formula 1 tire strategies and race pace using Python, FastF1 API, and Streamlit.

## 📊 Features

- **Strategy Timeline Visualization**: See tire compound choices for all drivers across the race
- **Pace Comparison**: Compare lap times between multiple drivers
- **Strategy Classification**: Analyze one-stop vs two-stop vs three-stop strategies
- **Interactive Filtering**: Select specific drivers to compare performance

## 🌐 Live Demo
**[Try the live dashboard here!](https://your-app.streamlit.app](https://f1racestrategydashboard.streamlit.app/
)**

## 🛠️ Technologies Used

- **Python 3.12**
- **FastF1**: Official F1 data API
- **Streamlit**: Interactive web dashboard framework
- **Plotly**: Interactive visualizations
- **Pandas**: Data manipulation and analysis

## 🚀 Installation
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/f1_race_strategy_dashboard.git
cd f1_race_strategy_dashboard

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 💻 Usage
```bash
# Run the dashboard
streamlit run app.py
```

The dashboard will open in your browser at `http://localhost:8501`

## 📁 Project Structure
```
f1_race_strategy_dashboard/
├── src/
│   ├── data_loader.py          # Load race data from FastF1 API
│   ├── strategy_analyzer.py    # Analyze tire strategies
│   └── visualizer.py            # Create interactive visualizations
├── app.py                       # Main Streamlit application
├── requirements.txt             # Project dependencies
└── README.md
```

## 🎯 Key Insights

This dashboard reveals:
- How tire strategy affects race outcomes
- Pace differences between teammates
- Tire degradation patterns across different compounds
- Strategic decisions during safety cars and virtual safety cars

## 🔮 Future Enhancements

- [ ] Add qualifying vs race pace comparison
- [ ] Implement tire degradation analysis
- [ ] Export race reports to PDF
- [ ] Add historical season comparison
- [ ] Integrate weather data impact on strategy

## 📚 What I Learned

- Working with time-series data from REST APIs
- Building interactive dashboards with Streamlit
- Data visualization best practices with Plotly
- Handling multi-level pandas DataFrames
- Caching strategies for improved performance

## 👤 Author

**Elaine**
- University of Chicago '28 | CS & Economics

## 📝 License

This project is open source and available under the MIT License.
