import random
import time

def simulate_ping(ip_address="192.168.1.1", total_pings=5):
    packets_sent = 0
    packets_received = 0

    print(f"Pinging {ip_address} with 32 bytes of data:\n")

    for i in range(1, total_pings + 1):
        packets_sent += 1
        print(f"Request {i} -> ", end="")

        # Simulate 20% packet loss
        if random.random() < 0.2:
            print("Request timed out.")
        else:
            packets_received += 1
            delay = round(random.uniform(1, 100), 2)  # Random delay in ms
            print(f"Reply from {ip_address}: time={delay}ms")

        time.sleep(1)

    # Summary
    packets_lost = packets_sent - packets_received
    loss_percent = (packets_lost / packets_sent) * 100

    print("\nPing statistics for", ip_address)
    print(f"    Packets: Sent = {packets_sent}, Received = {packets_received}, Lost = {packets_lost} ({int(loss_percent)}% loss)\n")

# Run the simulation
if __name__ == "__main__":
    simulate_ping()
