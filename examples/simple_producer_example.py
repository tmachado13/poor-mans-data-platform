from src.producer import SimpleProducer

def main():
    # Create a simple producer
    producer = SimpleProducer(event_type="test_event")
    
    # Generate and print a single event
    event = producer.generate_event()
    print("Generated event:")
    print(event.to_dict())

if __name__ == "__main__":
    main()
