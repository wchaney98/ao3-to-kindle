import AO3

class AO3_Downloader:
    def __init__(self):
        self._ao3_urls = []
        self.urls_validated = False

    def login(self):
        print("Logging in... (not impl)")

    def add_url(self, url: str):
        if url != None:
            self._ao3_urls.append(url)
            print(self._ao3_urls)

    def clear_urls(self):
        self._ao3_urls = []

    def validate_urls(self):
        print(f"Validating: {self._ao3_urls}\n...")

        self.urls_validated = True

        if self._ao3_urls == None or len(self._ao3_urls) == 0:
            self.urls_validated = False

        try:
            for url in self._ao3_urls:
                work_id = AO3.utils.workid_from_url(url)
                work = AO3.Work(work_id)
                print(f"Chapters: {work.nchapters}")
        except:
            self.urls_validated = False
        
        print(f"Validation result: {self.urls_validated}")
        return self.urls_validated
        

        
        