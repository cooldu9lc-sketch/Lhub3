from concurrent import futures
from urllib.parse import urlsplit

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:

        host = urlsplit(startUrl).hostname
        seen = {startUrl}

        with futures.ThreadPoolExecutor(max_workers=16) as executor:

            pending = {
                executor.submit(htmlParser.getUrls, startUrl)
            }

            while pending:

                done, pending = futures.wait(
                    pending,
                    return_when=futures.FIRST_COMPLETED
                )

                for future in done:
                    for url in future.result():

                        if url not in seen and urlsplit(url).hostname == host:
                            seen.add(url)

                            pending.add(
                                executor.submit(htmlParser.getUrls, url)
                            )

        return list(seen)