from growbot import Robot
import asyncio

def main():
    r = Robot("35ae6830-d961-4a9c-937f-8aa5bc61d6a3", "ws://localhost:8080")
    asyncio.get_event_loop().run_until_complete(r.connect())

if __name__ == "__main__":
    main()
