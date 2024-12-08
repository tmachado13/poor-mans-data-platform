from src.producer import SimpleProducer

def main():
    # Create a producer with an endpoint URL
    producer = SimpleProducer(
        event_type="test_event",
        endpoint_url="http://localhost:8000/events"  # Replace with your actual endpoint
    )
    
    # Generate and publish an event
    success = producer.publish_event()
    
    if success:
        print("Event published successfully!")
    else:
        print("Failed to publish event.")

    # You can also generate an event first and then publish it
    event = producer.generate_event()
    print("\nGenerated event:")
    print(event.to_dict())
    
    success = producer.publish_event(event)
    if success:
        print("\nEvent published successfully!")
    else:
        print("\nFailed to publish event.")

if __name__ == "__main__":
    main()
