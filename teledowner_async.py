import asyncio
import datetime
import sys

async def tele_down(url, loop):
    process = None
    in_progress = False
    while True:
        print(datetime.datetime.now())

        hour = datetime.datetime.now().time().hour
        if (hour in range(0, 7)) or (hour >= 23):
            if not in_progress:
                print("Zeekwat Starting Download Process")
                process = asyncio.create_subprocess_shell("wget %s" % url)
                await process
                in_progress = True
            else:
                print("Zeekwat active but Download in Progress")

        else:
            print("Stopping Download Process")
            process.terminate()
            process = None

        await asyncio.sleep(10)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # python teledowner_async.py http://denver1.renegade-x.com/RenegadeX-Open%20Beta%205G.zip
    loop.run_until_complete(tele_down(sys.argv[1], loop))
    loop.close()
