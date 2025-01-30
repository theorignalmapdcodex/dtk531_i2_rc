# **MQTT-LLM College Data Integration**

An intelligent system that integrates MQTT messaging with Google's Gemini LLM to provide real-time analysis of U.S. college data. This system enables personalized insights, historic and notable information for college-bound students by processing and analyzing college information in real-time.

## Project Overview

This project consists of the following components:
- **Publisher**: Broadcasts U.S. college data via MQTT.
- **Subscriber**: Receives data from the publisher and processes it using Google's Gemini LLM.
- **LLM Integration**: Utilizes Google's Gemini 1.5 Flash model for real-time data analysis.
- **Testing Module**: Facilitates testing LLM interactions with selected college data.

## Prerequisites

- Python 3.8+
- Access to Google's Gemini API (API key required)
- Internet connection for MQTT broker access

## Installation

1. Clone the repository:
```bash
git clone [[your-repository-url](https://github.com/theorignalmapdcodex/dtk531_i2_rc)]
cd [dtk531_i2_rc]
```

2. Create and activate a virtual environment:
```bash
python3 -m venv college_task_env
source college_task_env/bin/activate  # On Windows, use `college_task_env\Scripts\activate`
```

3. Install required packages:
```bash
pip install paho-mqtt google-generativeai
```

4. Set up your Gemini API credentials:
- Create a `.env` file to store your actual Gemini key for it to be accessible globally
   ```python
   YOUR_API_KEY = 'ActualAPIkeyValue'
   ```
   - Next, create a file named `gemini_myapi.py`
   - Load environment variables (in this case your api key) from the .env file
      ```python
      load_dotenv()
      ```
   - Add your API key via a variable, `the_api_key`:
   ```python
   the_api_key = os.getenv("YOUR_API_KEY")
   ```

## Pre-tasks

1. Prepare the college data:
   - Download the college data from [NCES IPEDS](https://nces.ed.gov/ipeds/datacenter/InstitutionList.aspx?goToReportId=1&sid=ed8899d5-439d-45d0-8201-036ffada722b&rtid=1). NB: You would have to select your own variables to create your dataset.
   - Convert the data (usually in csv format) to JSON format using a tool or template like [Mockaroo](https://nces.ed.gov/ipeds/datacenter/InstitutionList.aspx?goToReportId=1&sid=ed8899d5-439d-45d0-8201-036ffada722b&rtid=1) or by editing a custom script from [Google Colab]() for example.
   - Save the JSON file as `schoolsdata.json` in the project directory.

2. Configure MQTT settings:
   - Open `config.json` and set the MQTT broker details:
   ```json
   {
     "mqtt_broker": "test.mosquitto.org",
     "mqtt_port": 1883,
     "mqtt_topic": "gemini_llm_test/uscolleges/schdetails"
   }
   ```

## Usage

### 1. Start the Publisher

```bash
python pub.py
```

### 2. Start the Subscriber

```bash
python sub.py
```

### 3. Test LLM Interactions

```bash
python gemini_api_test.py
```

## Data Format

The system uses JSON messages with the following structure:
```json
{
    "Unit_ID": "...",
    "Institution_Name": "...",
    "Avg_Net_Price": "...",
    "City": "...",
    "State": "...",
    "Zip_Code": "...",
    "Category": "...",
    "SAT_Reading_75th": "...",
    "SAT_Math_75th": "...",
    "timestamp": "..."
}
```

## MQTT Topic Structure

- Main topic: `gemini_llm_test/uscolleges/schdetails`
- QoS Level: 1 (At least once delivery)
- Broker: `test.mosquitto.org:1883`

## Notes

- The system uses the public Mosquitto test broker. For production, consider using a secure, private broker.
- LLM responses are cached in `llm_responses.json` for future reference and analysis.
- The system is designed to run continuously but can be stopped with Ctrl+C.
- All LLM interactions are logged for future reference and improvement of the system.

## Error Handling

The system includes error handling for:
- MQTT connection failures
- API call failures
- Data parsing errors
- File I/O operations

## Future Improvements

- Implement secure MQTT connections (TLS/SSL)
- Add message filtering and prioritization
- Expand college data analysis capabilities
- Implement multi-topic support for different types of college data

## Resources/References

- [NCES IPEDS Data](https://nces.ed.gov/ipeds/use-the-data)
- [Python Virtual Environments Guide](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/)
- [MQTT with Eclipse Paho Python](https://dev.to/ndutared/understanding-mqtt-with-eclipse-paho-python-664)
- [Google Generative AI Setup Guide](https://priyanshu.com.np/genai/)

For more information on IPEDS data and its usage, visit the [NCES IPEDS website](https://nces.ed.gov/ipeds/use-the-data/new-to-ipeds)[7].

---
This project provides an **efficient** way to integrate **[MQTT (Message Queuing Telemetry Transport)](https://mqtt.org/)** with **[Gemini API (Gemini Application Programming Interface)](https://aistudio.google.com/prompts/new_chat?gad_source=1&gclid=Cj0KCQiAwOe8BhCCARIsAGKeD54ZYrTJ_uA03Eo9DlKsfjx4kv_Bvys7A0RxPujgVbyBFwLU6dsP8X0aArU-EALw_wcB) to enhance Human-LLM interactions**. 🚀

📚 **Author:** Michael Dankwah Agyeman-Prempeh [MEng. DTI '25]