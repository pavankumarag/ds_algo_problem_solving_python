import requests
import logging
logging.basicConfig(level=logging.INFO)


def log_args(func):
    def run(*args):
        logging.info("Arguments passed to the function %r are %r" %(func, args))
        return func(*args)
    return run


class ApiHelper:
    @log_args
    def star_wars_characters(self, page_nr):
        self.page_nr = page_nr
        resp = requests.get("https://swapi.co/api/people/")
        star_wars_character = []
        for i in resp.json()['results']:
            star_wars_character.append([i['name'], i['height'], i['gender']])
        return star_wars_character

    @staticmethod
    def append_to_file(filepath, name, height, gender):
        fp = open(filepath, "a")
        fp.write(str([name, height, gender]))
        fp.write("\n")
        fp.close()


class TestApiHelper:
    def test_star_wars_characters(self):
        api = ApiHelper()
        out = api.star_wars_characters(1)
        assert len(out) > 1, "WARNING: star_wars_characters method returning empty"

if __name__ == "__main__":
    api = ApiHelper()
    out = api.star_wars_characters(1)
    #print "output is ", out
    for i in out:
        ApiHelper.append_to_file("/Users/pavan.govindraj/vinoth.out", i[0], i[1], i[2])