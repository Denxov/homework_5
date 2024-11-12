from time import sleep
from types import NoneType


class User:
    def __init__(self,nickname:str,password:int,age:int):
        self.password=password
        self.nickname=nickname
        self.age=age

    def __str__(self):
        return self.nickname

class Video:
    def __init__(self,title:str,duration:int,adult_mode=False):
        self.title=title
        self.duration=duration
        self.time_now=0
        self.adult_mode=adult_mode

class UrTube:
    def __init__(self):
        self.users={} #??
        self.videos=[]
        self.current_user=None
    def log_in(self,nickname,password):
        if nickname in self.users:
            if self.users[nickname].password==hash(password):
                self.current_user=self.users[nickname]
        else:
            print(nickname,'- Не найден')
            return False
    def log_out(self):
        self.current_user=None

    def register(self,nickname,password,age):
        if not nickname in self.users:
            self.users[nickname]=User(nickname,hash(password),age)
            self.current_user=self.users[nickname]
        else: print(f'Пользователь {nickname} уже существует')
        return


    def add(self,*videos:Video):
        for i in range(0,len(videos)):
            if videos[i].title not in self.videos:
                self.videos.append(videos[i])

    def get_videos(self,str2search):
        out=[]
        for i in range(0,len(self.videos)):
            if str2search.lower() in self.videos[i].title.lower():
                out.append(self.videos[i].title)
        return out

    def watch_video(self,str2search):
        if self.current_user!=None:
            count=0;
            for i in range(0,len(self.videos)):
                if self.videos[i].title==str2search:
                    count+=1
                    if self.current_user.age>=18:
                        while self.videos[i].time_now<self.videos[i].duration:
                            sleep(1)
                            print(self.videos[i].time_now,end=' ')
                            self.videos[i].time_now+=1
                        print('Конец видео');
                    else: print('Вам нет 18 лет, пожалуйста покиньте страницу')
            if count == 0: print(f'Видео <{str2search}> не найдены')
        else: print('Войдите в аккаунт, чтобы смотреть видео')

if __name__=='__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')
    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)
    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
