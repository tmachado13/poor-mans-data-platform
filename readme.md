# Poor Man's Data Platform

Poor Man's Data Platform is a lightweight event-driven data platform built with FastAPI, Streamlit, DeltaLake, and message queues. It allows easy event production, event storage, and analytics with a simple, user-friendly interface.

## Overview

The platform includes:
- A producer of events
- An API to receive events
- A message queue to buffer events
- Event storage in DeltaLake
- A Streamlit interface to configure and monitor the system
- Analytical tools to compute metrics from stored data and visualize them

---

## Task Breakdown

### **1. Producer of Events**
   - **Description**: The producer will generate events that will be sent to the API endpoint.
   - **Tasks**:
     - [ ] Implement an event producer (this could be as simple as generating fake events or simulating event data).
     - [ ] Define the event structure (e.g., JSON with fields like timestamp, event type, payload).
     - [ ] Make the producer configurable via a **Streamlit UI** for easy management of event generation parameters.
   
   **Technologies**: Python, Streamlit

### **2. API with FastAPI**
   - **Description**: Create a FastAPI server to receive events and send them to a message queue.
   - **Tasks**:
     - [ ] Set up FastAPI to expose a POST endpoint for receiving events.
     - [ ] Validate incoming event data (e.g., check schema integrity).
     - [ ] Implement a **message queue** to buffer and send events to downstream services (e.g., using RabbitMQ, Kafka, or Redis).
   
   **Technologies**: FastAPI, Pydantic (for validation), message queue library (e.g., `pika` for RabbitMQ or `aiokafka` for Kafka)

### **3. Message Queue**
   - **Description**: Use a message queue to handle event buffering between the API and DeltaLake storage.
   - **Tasks**:
     - [ ] Set up a message queue (choose between RabbitMQ, Kafka, or Redis Pub/Sub).
     - [ ] Integrate FastAPI with the message queue to publish events to the queue.
     - [ ] Set up message consumers to listen to the queue and process incoming events.
   
   **Technologies**: RabbitMQ/Kafka/Redis, Celery (optional for background processing)

### **4. DeltaLake Storage**
   - **Description**: Store incoming events into DeltaLake for reliable, transactional storage.
   - **Tasks**:
     - [ ] Set up **DeltaLake** storage on a local or cloud-based file system (e.g., using Delta format in Spark or with the `deltalake` Python library).
     - [ ] Use the **DeltaRS connector** (for Rust-based Delta Lake integration) or `delta` Python library for DeltaLake interactions.
     - [ ] Design a table schema for storing event data (e.g., partitioning by event timestamp).
     - [ ] Ensure that event data is ingested in real-time into DeltaLake from the message queue.
   
   **Technologies**: DeltaLake, `deltalake` (Python library), Spark or local file system (e.g., S3, HDFS)

### **5. Streamlit UI for Producer Configuration**
   - **Description**: Provide an interface to configure and run the event producer from a **Streamlit app**.
   - **Tasks**:
     - [ ] Create a Streamlit dashboard to configure event parameters like frequency, event types, and payload structure.
     - [ ] Include a button to start and stop the event producer.
     - [ ] Display logs or output showing the events being produced in real-time.
   
   **Technologies**: Streamlit, Python (for logic and configuration)

---

### **Analytics and Monitoring**

### **6. Streamlit Dashboard for Event Monitoring**
   - **Description**: Create a Streamlit dashboard to visualize and monitor events flowing through the platform.
   - **Tasks**:
     - [ ] Build a dashboard that fetches event data from DeltaLake and visualizes it (e.g., count of events, types of events, etc.).
     - [ ] Display a **real-time stream of events** as they are received and processed.
     - [ ] Implement **filters** (e.g., by event type, time range) to explore the event data.
     - [ ] Provide simple charts and graphs (e.g., bar chart for event types, time series for event counts).
   
   **Technologies**: Streamlit, Pandas, Matplotlib/Plotly for visualization

### **7. Compute Metrics from DeltaLake**
   - **Description**: Implement basic data analytics to compute metrics from the DeltaLake event data.
   - **Tasks**:
     - [ ] Calculate metrics like event frequency, event types, and event trends over time.
     - [ ] Use **PySpark** or **Pandas** to perform data transformations and aggregations.
     - [ ] Provide simple insights, such as “Most frequent event types,” “Event distribution over time,” etc.
     - [ ] Display computed metrics on the Streamlit dashboard.
   
   **Technologies**: DeltaLake, PySpark/Pandas, Streamlit, SQL (for querying DeltaLake)

---

### **8. Final Testing and Documentation**
   - **Description**: Ensure that the system works end-to-end, from event production to storage and analytics.
   - **Tasks**:
     - [ ] Test the entire flow from event generation to storage in DeltaLake.
     - [ ] Write tests for each component (API, producer, event storage, etc.).
     - [ ] Provide detailed documentation for installation, setup, and usage (especially for the Streamlit UI and API).
   
   **Technologies**: Pytest, FastAPI, Streamlit

---

## Technologies

- **FastAPI**: For building the API that receives events.
- **Streamlit**: For the dashboard and UI for event production/configuration.
- **Message Queue**: RabbitMQ, Kafka, or Redis for event buffering.
- **DeltaLake**: For event storage and transactional data lake capabilities.
- **Pandas/PySpark**: For data transformation and metrics calculation.
- **Python**: The primary language for building the platform.

---

## Installation

To install and run the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/poor_mans_data_platform.git
    cd poor_mans_data_platform
    ```

2. Install dependencies with uv:
    ```bash
    uv pip install -r requirements.txt
    ```

3. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

4. Start the Streamlit app:
    ```bash
    streamlit run producer_ui.py
    ```

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
