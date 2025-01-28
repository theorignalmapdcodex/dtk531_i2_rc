# **MQTT-LLM College Data Integration**

An intelligent system that integrates MQTT messaging with Google's Gemini LLM to provide real-time analysis of U.S. college data. This system enables personalized insights for college-bound students by processing and analyzing college information in real-time.

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
python3 -m venv college_data_env
source college_data_env/bin/activate  # On Windows, use `college_data_env\Scripts\activate`
```

3. Install required packages:
```bash
pip install paho-mqtt google-generativeai python-dotenv
```

4. Set up your Gemini API credentials:
   - Create a file named `gemini_myapi.py`
   - Add your API key:
   ```python
   the_api_key = "your-gemini-api-key"
   ```

## Pre-tasks

1. Prepare the college data:
   - Download the latest college data from [NCES IPEDS](https://nces.ed.gov/ipeds/use-the-data)[7].
   - Convert the data to JSON format using a tool like [Mockaroo](https://www.sitepoint.com/test-data-json-example/)[5] or by writing a custom script.
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

## Resources

- [NCES IPEDS Data](https://nces.ed.gov/ipeds/use-the-data)
- [Python Virtual Environments Guide](https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/)
- [MQTT with Eclipse Paho Python](https://dev.to/ndutared/understanding-mqtt-with-eclipse-paho-python-664)
- [Google Generative AI Setup Guide](https://priyanshu.com.np/genai/)

For more information on IPEDS data and its usage, visit the [NCES IPEDS website](https://nces.ed.gov/ipeds/use-the-data/new-to-ipeds)[7].

[1][2][3][4][5][6][7][8]

Citations:
[1] https://nces.ed.gov
[2] https://www.dataquest.io/blog/a-complete-guide-to-python-virtual-environments/
[3] https://dev.to/ndutared/understanding-mqtt-with-eclipse-paho-python-664
[4] https://priyanshu.com.np/genai/
[5] https://www.sitepoint.com/test-data-json-example/
[6] https://docs.datacommons.org/custom_dc/custom_data.html
[7] https://nces.ed.gov/ipeds/use-the-data/new-to-ipeds
[8] https://developer.vonage.com/en/blog/a-comprehensive-guide-on-working-with-python-virtual-environments
[9] http://www.steves-internet-guide.com/into-mqtt-python-client/
[10] https://www.goldyarora.com/blog/python-virtual-environments
[11] https://docs.python.org/ko/3.6/library/venv.html
[12] https://pypi.org/project/paho-mqtt/
[13] https://stackoverflow.com/questions/77868611/modulenotfounderror-no-module-named-google-generative
[14] https://blog.inedo.com/python/python-environment-management-best-practices/
[15] https://cedalo.com/blog/configuring-paho-mqtt-python-client-with-examples/
[16] https://www.youtube.com/watch?v=xBRzb5LqXTY
[17] https://realpython.com/python-virtual-environments-a-primer/
[18] https://communities.sas.com/t5/SAS-Communities-Library/How-to-read-JSON-data-in-SAS/ta-p/849000
[19] https://stackoverflow.com/questions/60473360/how-to-implement-test-data-in-json-file-in-data-driven-unit-test-in-net-using-c
[20] https://donnees-data.tpsgc-pwgsc.gc.ca/dd/json_df-eng.html
[21] https://webservices.it.ufl.edu/t4/uf-2015-template/content-types/build-json-file/
[22] https://worldbank.github.io/connectivity_mapping/facebook_nbs/creating_a_json_for_collection.html
[23] https://nces.ed.gov/ipeds/use-the-data/new-to-ipeds
[24] https://www.youtube.com/watch?v=XM6kh_jnUSY