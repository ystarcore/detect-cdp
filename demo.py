from nodriver import start, cdp, loop


async def receive_handler(event: cdp.network.ResponseReceived):
    print(event.response)


async def send_handler(event: cdp.network.RequestWillBeSent):
    r = event.request
    s = f"{r.method} {r.url}"
    for k, v in r.headers.items():
        s += f"\n\t{k} : {v}"
    print(s)
    print(event)


async def main():
    browser = await start()
    tab = browser.main_tab
    tab.add_handler(cdp.network.RequestWillBeSent, send_handler)
    tab.add_handler(cdp.network.ResponseReceived, receive_handler)

    tab = await browser.get("https://www.browserscan.net/bot-detection")

    await tab.sleep(30)
    browser.stop()


if __name__ == "__main__":
    loop().run_until_complete(main())
