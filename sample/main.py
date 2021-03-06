from growbot import Remote, RPCType
import asyncio

def main():
    r = Remote("35ae6830-d961-4a9c-937f-8aa5bc61d6a3", "ws://localhost:8080")
    r.add_callback(RPCType.MOVE_IN_DIRECTION, lambda direction: print("Moving in direction", direction))
    print("Listening for updates...")
    asyncio.get_event_loop().run_until_complete(r.connect())

if __name__ == "__main__":
    main()
