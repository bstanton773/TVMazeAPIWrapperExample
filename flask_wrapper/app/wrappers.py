import requests

class TVMazeAPI:
    
    def __init__(self):
        self.base_url = 'http://api.tvmaze.com'
        self.api_key = ''
        
    def _get(self, url, headers={}):
        response = requests.get(url, headers=headers)
        return response
    
    def _post(self, url):
        response = requests.post(url)
        return response
    
    def _create_show_obj(self, info):
        show_id = info['id']
        title = info['name']
        img = info['image']['medium'] if info['image'] else None
        summary = info['summary']
        network = info['network']['name'] if info['network'] else None
        show = TVShow(show_id, title, img, summary, network)
        return show
    
    def search_shows(self, query):
        url = self.base_url + f'/search/shows?q={query}'
        res = self._get(url)
        if res.status_code == 200:
            searched_shows = res.json()
            return [self._create_show_obj(show['show']) for show in searched_shows]
        return res
    
    def get_show_info(self, show_id):
        url = self.base_url + f'/shows/{show_id}'
        res = self._get(url)
        if res.status_code == 200:
            info = res.json()
            show = self._create_show_obj(info)
            return show
        return res
    
    def get_episode_list(self, show_id):
        url = self.base_url + f'/shows/{show_id}/episodes'
        res = self._get(url)
        if res.status_code == 200:
            return res.json()
        return res


class TVShow:
    def __init__(self, show_id, title, img, summary, network):
        self.id = show_id
        self.title = title
        self.image = img
        self.summary = summary
        self.network = network
        self.episodes = self.get_episodes()
        
    def __repr__(self):
        return f'<TV Show | {self.title} >'
    
    def __str__(self):
        return f'{self.id} - {self.title}'
    
    def get_episodes(self):
        api = TVMazeAPI()
        episodes = api.get_episode_list(self.id)
        all_eps = []
        for episode in episodes:
            episode_id = episode['id']
            title = episode['name']
            season = episode['season']
            number = episode['number']
            airdate = episode['airdate']
            summary = episode['summary']
            all_eps.append(Episode(episode_id, title, season, number, airdate, summary))
        return all_eps
             
        
class Episode:
    def __init__(self, episode_id, title, season, number, airdate, summary):
        self.id = episode_id
        self.title = title
        self.season = season
        self.number = number
        self.airdate = airdate
        self.summary = summary
        
    def __repr__(self):
        return f'<Episode | {self.title}>'
    
    def __str__(self):
        return f'{self.id} - {self.title}'